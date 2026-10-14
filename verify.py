#!/usr/bin/env python3
"""Verifier for the G11 benchmark-audit reproduction package.

Checks the paper's headline numbers against the shipped cleaned release
(cleaned_release_v1.0.0.jsonl). Exits 0 with PASS lines, or 1 on the
first mismatch.

Author: Prabhu Rangaraju
License: MIT (see LICENSE)
"""
import json
import math
import sys
from collections import Counter

RELEASE = "cleaned_release_v1.0.0.jsonl"

# Wilson 95% score interval, z = 1.96.
def wilson(k, n):
    z = 1.96
    p = k / n
    denom = 1 + z * z / n
    center = p + z * z / (2 * n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (center - half) / denom, (center + half) / denom

failures = []

def check(name, got, want):
    ok = got == want
    print(("PASS" if ok else "FAIL") + f" {name}: got {got}, want {want}")
    if not ok:
        failures.append(name)

def check_close(name, got, want, tol=1e-3):
    ok = abs(got - want) <= tol
    print(("PASS" if ok else "FAIL") + f" {name}: got {got:.4f}, want {want:.4f}")
    if not ok:
        failures.append(name)

recs = [json.loads(line) for line in open(RELEASE)]
check("total records", len(recs), 109)

mat = [r for r in recs if r["verdict"] == "material_error"]
check("material errors", len(mat), 35)
check_close("overall error rate", len(mat) / len(recs), 0.321)

lo, hi = wilson(35, 109)
check_close("overall Wilson CI lower", lo, 0.241)
check_close("overall Wilson CI upper", hi, 0.414)

# Per-family error rates.
fam = Counter((r["family"], r["verdict"]) for r in recs)
fam_tot = Counter(r["family"] for r in recs)
expect = {
    "nl4opt": (11, 40, 0.275, 0.161, 0.428),
    "mamo": (16, 35, 0.457, 0.305, 0.618),
    "industryor": (8, 34, 0.235, 0.124, 0.400),
}
for f, (k, n, rate, lo_e, hi_e) in expect.items():
    check(f"{f} total", fam_tot[f], n)
    check(f"{f} material errors", fam[(f, "material_error")], k)
    check_close(f"{f} error rate", k / n, rate)
    lo, hi = wilson(k, n)
    check_close(f"{f} Wilson CI lower", lo, lo_e)
    check_close(f"{f} Wilson CI upper", hi, hi_e)

# Error-class distribution (material errors only).
ec = Counter(r["error_class"] for r in mat)
check("WRONG_GT", ec["WRONG_GT"], 34)
check("INPUT_TEXT_CONTRADICTION", ec["INPUT_TEXT_CONTRADICTION"], 1)

# Root-cause distribution (material errors only).
rc = Counter(r["root_cause_category"] for r in mat)
check("undocumented_integrality", rc["undocumented_integrality"], 25)
check("unclassified_wrong_gt", rc["unclassified_wrong_gt"], 9)
check("float_truncation", rc["float_truncation"], 1)

# 70/30 split: dev optima public, test optima withheld.
sp = Counter(r["split"] for r in recs)
check("dev split", sp["dev"], 77)
check("test split", sp["test"], 32)
dev, test = [r for r in recs if r["split"] == "dev"], [r for r in recs if r["split"] == "test"]
check("dev optima public", sum(1 for r in dev if r.get("audited_optimum") is not None), 77)
check("test optima withheld", sum(1 for r in test if r.get("audited_optimum") is not None), 0)

# Canary GUIDs on every record.
check("canary present on all records",
      sum(1 for r in recs if r.get("canary") and "SHOULD NEVER APPEAR IN TRAINING CORPORA" in r["canary"]),
      109)

if failures:
    print(f"\n{len(failures)} check(s) FAILED")
    sys.exit(1)
print("\nAll checks passed.")
