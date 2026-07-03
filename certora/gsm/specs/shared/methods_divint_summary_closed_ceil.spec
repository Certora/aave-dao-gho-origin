// The (unverified) summary for OpenZeppelin's `Math.mulDiv`.
// Closed-form-ceil variant of methods_divint_summary.spec: computes Ceil as the single
// expression `(x*y + d - 1)/d`. The optimality proofs reason about this closed form far
// better than about a floor + remainder-bump, so optimality.spec imports this variant.
// Conflict variant: two `Math` libraries make `Math.Rounding` ambiguous, so the enum is
// qualified by FixedFeeStrategyHarness (imports the OZ v5 Math), present in optimality.conf.
// Use with care!

methods {
  function Math.mulDiv(uint256 x, uint256 y, uint256 denominator) internal returns (uint256) => mulDivSummary(x, y, denominator);
  function _.mulDiv(uint256 x, uint256 y, uint256 denominator, FixedFeeStrategyHarness.Rounding rounding) internal => mulDivSummaryWithRounding(x, y, denominator, rounding) expect (uint256);
}

function mulDivSummary(uint256 x, uint256 y, uint256 denominator) returns uint256 {
  require denominator > 0;
  return require_uint256((x*y)/denominator);
}

function mulDivSummaryWithRounding(uint256 x, uint256 y, uint256 denominator, FixedFeeStrategyHarness.Rounding rounding) returns uint256 {
  require denominator > 0;
  if (rounding == FixedFeeStrategyHarness.Rounding.Ceil) {
    return require_uint256((x * y + denominator - 1) / denominator);
  } else return require_uint256((x * y) / denominator);
}
