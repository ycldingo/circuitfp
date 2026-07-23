# Changelog

## v0.1.3

### Added
- Added `PhaseOperators`:
  - identity operator
  - phase operator
- Added unit tests for all modules above.
- Added `to_dict()` and `__repr__()` support for basis inspection.
- Added notebook `examples/BCS_overlap.ipynb`.


## v0.1.2

### Added

- Added `PhaseBasis` class for constructing finite-dimensional phase bases.
- Added automatic estimation of effective phase-space dimensionality.
- Added validation for physical parameters:
  - bandwidth
  - superconducting gap
  - number of modes
- Added automatic dimension selection based on effective dimensionality.
- Added warning mechanism when requested dimension is smaller than the effective dimension.
- Added phase grid generation and phase spacing calculation.
- Added `to_dict()` and `__repr__()` support for basis inspection.

### Testing

- Added unit tests covering:
  - effective dimension calculation
  - dimension selection logic
  - phase grid construction
  - invalid parameter handling
  - dictionary representation

## v0.1.1

### Added

- First example notebook (`examples/BCS_overlap.ipynb`)
- Examples README.md


## v0.1.0

### Added

- Overlap class
- overlap()
- overlap_matrix()
- Unit tests