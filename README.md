# G11: A Third of the Ground Truth Is Wrong — Reproduction Package

Author: Prabhu Rangaraju. License: MIT (see `LICENSE`).

This package lets any reader re-verify the headline numbers of the
benchmark-audit paper "A Third of the Ground Truth Is Wrong: A 127-Instance
Audit of Optimization-Modeling Benchmarks."

## What it contains

- `cleaned_release_v1.0.0.jsonl` — the cleaned benchmark release (v1.0.0):
  109 instances (NL4Opt 40, MAMO 35, IndustryOR 34) with per-instance
  shipped vs. audited optima, verdicts, error classes, and root-cause
  categories. Every record carries a canary GUID. 77 dev records ship with
  audited optima; 32 test records have optima withheld (hash-committed).
- `verify.py` — checks every headline number against the release file.
- `reproduce.sh` — one-command runner for the verifier.
- `paper.pdf` — the manuscript.
- `CITATION.md` — how to cite this work.

## Reproduce

```bash
bash reproduce.sh
```

Runs in seconds (Python 3 only, no solver needed). Expected output ends
with "All checks passed."

## What the verifier checks

- 35/109 = 32.1% material errors (Wilson 95% CI 24.1–41.4%)
- Per-family rates: NL4Opt 11/40 = 27.5%, MAMO 16/35 = 45.7%,
  IndustryOR 8/34 = 23.5% (each with its Wilson 95% CI)
- Error classes: 34 WRONG_GT + 1 INPUT_TEXT_CONTRADICTION
- Root causes: 25 undocumented_integrality + 9 unclassified_wrong_gt +
  1 float_truncation
- 77/32 dev/test split with test optima withheld
- Canary GUIDs on all 109 records

## Method note

The audit itself (hand-encoding each instance from the problem text alone
and solving with SCIP) is documented in the paper's method section and the
release's PROTOCOL. Re-running the full solver audit from scratch is
described in the paper; this package verifies the reported numbers from
the shipped release, which is the checkable artifact.
