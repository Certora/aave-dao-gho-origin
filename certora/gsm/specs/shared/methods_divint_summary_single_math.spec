// The (unverified) summary for OpenZeppelin's `Math.mulDiv`.
// Single-`Math` variant: used where only one `Math` library is in scene (no conflict),
// so the rounding enum is referenced unqualified as `Math.Rounding`.
// (See methods_divint_summary.spec for the conflict variant used when two `Math`
// libraries are in scene and the enum must be qualified by the originating contract.)
// Use with care!

methods {
  function Math.mulDiv(uint256 x, uint256 y, uint256 denominator) internal returns (uint256) => mulDivSummary(x, y, denominator);
  function _.mulDiv(uint256 x, uint256 y, uint256 denominator, Math.Rounding rounding) internal => mulDivSummaryWithRounding(x, y, denominator, rounding) expect (uint256);
}

function mulDivSummary(uint256 x, uint256 y, uint256 denominator) returns uint256 {
  require denominator > 0;
  return require_uint256((x*y)/denominator);
}

function mulDivSummaryWithRounding(uint256 x, uint256 y, uint256 denominator, Math.Rounding rounding) returns uint256 {
  require denominator > 0;
  uint256 base = mulDivSummary(x, y, denominator);
  if (rounding == Math.Rounding.Ceil && (x * y) % denominator > 0) {
    return require_uint256(base + 1);
  } else return base;
}
