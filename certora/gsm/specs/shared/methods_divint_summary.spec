// The (unverified) summary for OpenZeppelin's `Math.mulDiv`.
// Conflict variant: two `Math` libraries with different `Rounding` members are in scene
// (OZ v5 {Floor,Ceil,Trunc,Expand} vs vendored OZ v4 {Down,Up,Zero}), so `Math.Rounding`
// is ambiguous and must be qualified by an originating contract that imports the OZ v5 Math.
// FixedFeeStrategyHarness is present in every conflicting conf that imports this spec.
// (See methods_divint_summary_single_math.spec for the unqualified single-`Math` variant.)
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
  // Mirror OZ Math.mulDiv: reuse the single floor division and bump by 1 on a remainder for Ceil.
  // (Avoid a second independent `(x*y+d-1)/d` division term, which the solver handles far worse.)
  uint256 base = mulDivSummary(x, y, denominator);
  if (rounding == FixedFeeStrategyHarness.Rounding.Ceil && (x * y) % denominator > 0) {
    return require_uint256(base + 1);
  }
  return base;
}
