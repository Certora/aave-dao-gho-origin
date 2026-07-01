// The (unverified) summary for OpenZeppelin's `Math.mulDiv`.
// Use with care!

methods {
  function Math.mulDiv(uint256 x, uint256 y, uint256 denominator) internal returns (uint256) => mulDivSummary(x, y, denominator);
  // The 4-arg rounding overload: `Math.Rounding` is ambiguous (two `Math` libraries with different
  // members), so we qualify by the originating contract that imports the OZ v5 Math (Floor/Ceil/Trunc/Expand).
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
