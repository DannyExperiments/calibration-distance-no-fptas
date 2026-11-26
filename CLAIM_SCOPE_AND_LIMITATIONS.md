# Claim scope and limitations

The theorem concerns additive approximation of the exact L1 distance to a deterministic calibrated predictor on the original finite feature space. The input supplies rational masses, conditional label means and forecasts explicitly. Runtime is polynomial in the input bit length and the numerical accuracy parameter 1/epsilon. The hard family has nonuniform masses and noiseless labels. All masses can be made integral before normalization.

The result is conditional on P versus NP. Under bounded-error randomization the same gap would imply NP is contained in BPP. The known uniform-mass/noiseless exact algorithm and the general PTAS remain applicable under their respective hypotheses. The theorem leaves uniform masses with noisy labels, fractional splitting or randomized prediction, statistical estimation and tolerant testing outside its scope.
