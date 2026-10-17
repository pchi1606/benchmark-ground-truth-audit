# Citation

If you use this release or the audit results, please cite:

> Prabhu Rangaraju. "A Third of the Ground Truth Is Wrong: A 127-Instance
> Audit of Optimization-Modeling Benchmarks." 2026.

```bibtex
@misc{rangaraju2026groundtruth,
  author = {Prabhu Rangaraju},
  title = {A Third of the Ground Truth Is Wrong: A 127-Instance Audit of
           Optimization-Modeling Benchmarks},
  year = {2026},
}
```

## Benchmarks audited

- NL4Opt competition (NeurIPS 2022 Competitions Track, PMLR 220): data via
  the LLM4OR collection.
- MAMO (Xuhan Huang et al., arXiv:2405.13144).
- IndustryOR (introduced in ORLM; Chenyu Huang et al., Operations
  Research 73(6), 2025).
- ComplexOR (extension audit; Ziyang Xiao et al., ICLR 2024).

## Source-data licenses

Problem texts and shipped optima in the release are derived from the
upstream benchmarks above and remain subject to their original terms
(e.g., MAMO is released by its authors under CC-BY-SA-4.0; cite the
original works listed above when using these records). The MIT license
covers the new material in this package (audit annotations, release
tooling, verifier, manuscript). Each record's `source` field pins the
exact upstream commit or access point it was drawn from.

## License

MIT License, Copyright (c) 2026 Prabhu Rangaraju. See `LICENSE`.
