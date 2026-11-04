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

## Source data: provenance, license, and terms

Per-suite pins (each record in the release JSONL also carries its own
`source` field with the same pin):

| Suite | Source (pinned) | License / terms basis |
|---|---|---|
| NL4Opt (40 instances) | github.com/LLM4OR/LLM4OR @ 75962df5ddf531906fda76f8708c658114e63c0e (`static/clean_benchmarks/NL4Opt`), accessed 2026-10-14 | Upstream terms of the NL4Opt competition data (NeurIPS 2022 Competitions Track) as distributed in the LLM4OR collection; no separate dataset license is stated upstream. Records are redistributed here for audit reproducibility; the original work must be cited. |
| MAMO (35 instances) | github.com/FreedomIntelligence/Mamo @ 2c91069dee5c1e4db4b899eb176ec987d0251bb3 | Released by its authors under CC-BY-SA-4.0 (see CITATION.md). The derivative records here are shared under the same share-alike terms. |
| IndustryOR (34 instances) | huggingface.co/datasets/CardinalOperations/IndustryOR @ b00811923f167cdf4ae1677c33cd61d4eea78f48, accessed 2026-10-14 | Upstream terms of the IndustryOR dataset as published with the ORLM work (Operations Research 73(6), 2025); no separate dataset license is stated upstream. Records are redistributed here for audit reproducibility; the original work must be cited. |
| ComplexOR | Extension audit only (Xiao et al., ICLR 2024); NOT part of the cleaned release | Not redistributed in this package. |

The MIT license in this package covers only the new material (audit
annotations, release tooling, verifier, manuscript), never the
upstream problem texts or shipped optima.

## Split hygiene

The verdict taxonomy was frozen from the pilot before the main audit
began (PROTOCOL.md §3) and was not revised by the audit outcomes; the
20-instance NL4Opt pilot did not change it. Solver configuration and
tolerances were fixed for the whole audit and were NOT tuned on the
audited instances. The 109 release records split 77 dev / 32 test
(seed 42, stratified by family); the test optima were sha256-committed
and withheld before the test-phase audit ran, and every record carries
a canary GUID.
