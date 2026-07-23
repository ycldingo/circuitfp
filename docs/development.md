# Development notes

**Current version: 0.1.2**

## Implemented

- overlap function and overlap matrix
- effective dimensionality estimation
    - automatic dimension selection: user-defined dimension support
    - protection against insufficient basis dimension
    - uniform phase-grid generatioin
- phase basis construction
- operators in phase space, including
    - identity operator
    - phase operator

### Documentation

- API example notebook:
    - `examples/BCS_overlap.ipynb`
    - `examples/phase_basis_and_phase_operators.ipynb`

## Next milestone

- Fourier transform
- Number operator
- Hamiltonian

## Coding conventions

- `numpy` style
- `pytest` required
- Examples provided as Jupyter notebooks