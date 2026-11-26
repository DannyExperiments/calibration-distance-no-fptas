# An inverse-polynomial approximation gap for calibration distance

Let a finite alphabet have positive rational masses, label means μ_x and supplied forecasts f_x. A deterministic calibrated predictor partitions the alphabet into blocks and predicts the block's mass-weighted label mean. Conversely, any partition implements a calibrated predictor, because combining blocks with the same mean preserves that mean and loss. Thus the minimum is attained among partitions. We show strong NP-hardness of inverse-polynomial additive approximation, not just exact NP-hardness.

Start with strongly NP-complete 3-PARTITION: positive integer weights a_i with B/4<a_i<B/2 and total mB, for 3m items. The hard instances may be taken with B polynomially bounded. Treat all weights below as unnormalized, and divide the final costs by T=m(M+B). Each ordinary item is a distinct alphabet atom of weight a_i, label 1 and forecast 0. For j=1,…,m define
```
q_j=1/4+j/(12m),   M=120 m² B,
μ_j=q_j−(1−q_j) B/M.
```
Create two distinct anchor atoms for j, each forecast q_j: a label-1 atom of weight Mμ_j and a label-0 atom of weight M(1−μ_j). These are strictly positive, each ≥M/5. Thus labels are deterministic, all data are rational, and the total mass is T.

Write K=B Σ_j q_j. A block containing anchor pieces of different indices costs at least (M/5)/(12m)=2mB by triangle inequality on the two distinct forecasts. This exceeds K+1/6. If there is no such mixing but some anchor pair is split, its label-1 piece is in a block containing only label-1 atoms, since its partner is absent and no distinct anchor pieces are allowed. Its mean is 1 so the cost is at least (M/5)(1−q_j)≥2M/15>K+1/6. Consequently any partition with cost below K+1/6 consists of intact and separated anchor pairs, each with some ordinary items, and possibly ordinary-only blocks.

An intact anchor j grouped with ordinary items of aggregate weight s has mean p(s)=(Mμ_j+s)/(M+s) and cost
```
F_j(s) = s p(s)+M |p(s)−q_j|.
```
At s=B the mean is q_j and cost Bq_j. For s≥B, p(s)≥q_j and direct substitution gives F_j(s)=Bq_j+(s−B). For 0≤s<B, p(s)<q_j, p'(s)>0, and F_j'(s)=p(s)+(s−M)p'(s)≤q_j≤1/3 since B<M. By integration, for all s≥0,
```
F_j(s) ≥ Bq_j+(s−B)/2 + (B−s)_+/6 + (s−B)_+/2.
```
Ordinary-only blocks have mean 1 and cost equal to their combined mass s_0. Since Σ_j(s_j−B)=−s_0, the total loss is at least
```
K+s_0/2+Σ_j[(B−s_j)_+/6+(s_j−B)_+/2].
```
Thus if any item is unassigned to anchors or any load is off B, integrality makes the excess at least 1/6. Conversely if all loads equal B there is a 3-partition (the weight bounds force triples), and the calibrated cost is K. Hence the normalized optimum is K/T in YES and at least (K+1/6)/T in NO.

An FPTAS at ε=1/(100T), compared to threshold (K+1/12)/T, would solve this promised strong 3-PARTITION in time polynomial in the input length, because T is polynomially bounded. Conversely if P=NP, the rational threshold decision is polynomial by its partition certificate in NP; binary search of [0,1] yields an additive scheme (indeed polynomial in log(1/ε)). If a witness is required, recover a partition with a nearly optimal cost by prefix restriction of its NP certificate. Therefore an additive FPTAS as stated exists iff P=NP. This is compatible with a PTAS. It is a deterministic complexity statement; a bounded-error randomized scheme instead implies NP⊆BPP.

Primary source: [Mingda Qiao, *Computational and Statistical Hardness of Calibration Distance*, §4, “An FPTAS?”](https://arxiv.org/html/2603.18391#S4). Existing exact-hardness and PTAS results are credited; their weaker computational gap does not rule out such a scheme. The construction here supplies the inverse-polynomial gap for the exact deterministic calibration distance, not for fractional calibration or the separate estimation and testing questions.

This file records the original \(1/6\) unnormalized gap. The [revised manuscript](../paper/manuscript.pdf) derives a derivative-free \(2/3\) gap by balancing the total deficit, excess and ordinary-only load.
