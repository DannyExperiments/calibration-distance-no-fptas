# Claims and evidence

| Claim | Evidence |
| --- | --- |
| Partition objective equals deterministic calibration distance | Manuscript §1 and Qiao's Fact 1. Equal-mean blocks may be pooled. |
| Low-cost partitions keep anchor pairs intact and separate | Manuscript §2. Forecast separation and the loss of a split positive-label anchor. |
| Incorrect loads create inverse-polynomial additive separation | Manuscript §3. Exact derivative-free formulas and integer deficit balance. |
| A deterministic FPTAS would decide strongly hard 3-PARTITION | Manuscript §4. The total unnormalized mass is polynomially bounded in the strongly hard family. |
| P = NP suffices | Manuscript §4. Partition threshold certificates and binary search. |
| Evidence on finite instances | The exact standard-library replay enumerates all partitions of three small examples and separately checks the load identities. |

### Scoped Lean result

Lean checks the underloaded-anchor inequality, the overloaded-anchor identity, exact balance of integer deficits and excesses including outside mass, and the two-thirds additive gap given the aggregate loss bound and a positive deficit. The statement uses rational anchor data. The structural reduction to intact anchor pairs, the hardness source and the polynomial encoding are proved in the paper. [Declaration and replay](formalization/README.md)
