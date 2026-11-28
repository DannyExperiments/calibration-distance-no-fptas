import Std
namespace CalibrationGap

/-- An underloaded anchor has mean p at or below its reference q.  These
two identities express the paper's mean equation and its absolute-loss
formula after selecting that sign. -/
theorem underloaded (M B s p q F : Rat) (heavy : s ≤ M) (low : s ≤ B)
    (mean_le_ref : p ≤ q) (small : 3*q ≤ 1)
    (loss : F = s*p + M*(q-p)) : 3*F ≥ 3*B*q - (B-s) := by
  have h₁ := Rat.mul_nonneg (show 0 ≤ M-s by grind) (show 0 ≤ q-p by grind)
  have h₂ := Rat.mul_nonneg (show 0 ≤ B-s by grind) (show 0 ≤ 1-3*q by grind)
  grind

/-- For an overloaded anchor the signed mean equation cancels the denominator. -/
theorem overloaded (M B s p q F : Rat)
    (mean : (M+s)*(p-q) = (1-q)*(s-B))
    (loss : F = s*p + M*(p-q)) : F = B*q + (s-B) := by grind

def deficit (B : Nat) (loads : List Nat) := (loads.map (fun s => B - s)).sum
def excess (B : Nat) (loads : List Nat) := (loads.map (fun s => s - B)).sum

theorem balance (B : Nat) (loads : List Nat) :
    deficit B loads + loads.sum = excess B loads + loads.length * B := by
  induction loads with
  | nil => simp [deficit,excess]
  | cons s tail ih =>
    change (B - s + deficit B tail) + (s + tail.sum) =
      (s - B + excess B tail) + (tail.length+1)*B
    rw [Nat.succ_mul]
    omega

theorem total_deficit (B outside : Nat) (loads : List Nat)
    (total : loads.sum + outside = loads.length * B) :
    deficit B loads = excess B loads + outside := by
  have h := balance B loads
  omega

/-- Three times the total loss avoids fractions. A nonzero integer
deficit forces the inverse-polynomial gap used by the reduction. -/
theorem gap (B outside : Nat) (loads : List Nat) (F K : Rat)
    (total : loads.sum + outside = loads.length * B)
    (incorrect : 0 < deficit B loads)
    (bound : 3*F ≥ 3*K - (deficit B loads : Rat) +
      3*((excess B loads : Rat) + (outside : Rat))) : 3*F ≥ 3*K + 2 := by
  have hd := total_deficit B outside loads total
  have hc : (deficit B loads : Rat) = (excess B loads : Rat) + (outside : Rat) := by
    rw [hd]; simp
  have pos : (1 : Rat) ≤ (deficit B loads : Rat) := by
    exact_mod_cast incorrect
  grind
#print axioms underloaded
#print axioms overloaded
#print axioms gap
end CalibrationGap
