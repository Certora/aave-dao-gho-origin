// The (unverified) summary for OpenZeppelin's `Math.mulDiv`.
// Use with care!

methods {
  function Math.mulDiv(uint256 x, uint256 y, uint256 denominator) internal returns (uint256) => mulDivSummary(x, y, denominator);
}

function mulDivSummary(uint256 x, uint256 y, uint256 denominator) returns uint256 {
  require denominator > 0;
  return require_uint256((x*y)/denominator);
}
