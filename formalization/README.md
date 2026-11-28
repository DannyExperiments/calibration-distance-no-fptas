# Lean certificate

`CalibrationGap.gap` is checked using Lean 4.30.0 and its standard library.

Lean checks the underloaded-anchor inequality, the overloaded-anchor identity, exact balance of integer deficits and excesses including outside mass, and the two-thirds additive gap given the aggregate loss bound and a positive deficit. The statement uses rational anchor data. The structural reduction to intact anchor pairs, the hardness source and the polynomial encoding are proved in the paper.

[Source](Q460Gap.lean) · [Verification workflow](../.github/workflows/lean.yml)

To replay from the repository root with Lean 4.30.0 installed, run

```sh
lean -DwarningAsError=true formalization/Q460Gap.lean
```

The source requests an axiom report. The GitHub Actions workflow downloads the pinned compiler, verifies its SHA-256 and checks the source with warnings treated as errors.
