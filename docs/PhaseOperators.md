# PhaseBasis module
```
circuitfp.PhaseOperators
```

The `PhaseOperators` module provides matrix representations of quantum operators in the discretised phase basis.

Current version includes

- identity operator $\mathbb{I}$
- phase operator $\hat{\phi} = \sum_j \phi_j |\phi_j\rangle\langle\phi_j|$
<!-- - phase derivative operator $\hat{\phi}' = \sum_j \phi_j' |\phi_j\rangle\langle\phi_j|$ -->


## Identity ioerator

Mathematical definition: $\mathbb{I} |\phi_j\rangle = |\phi_j\rangle$.

Matrix representation: $\mathbb{I}_{jk} = \delta_{jk}$.

Usage:

```python
Id = operators.identity(dim)
```

returns an identity matrix of dimension `dim`.

## Phase operators

Physics definition: $\hat{\phi} |\phi_j\rangle = \phi_j |\phi_j\rangle$.

Matrix representation: $\hat{\phi} = \operatorname{diag} (\phi_1, \phi_2, \cdots)$.

Usage: 

```python
phi = operators.phase(phase_grid)
```

returns a diagonal matrix with diagonal elements `phase_grid`.


## Examples

```python
from circuitfp.phase_basis import PhaseBasis
from circuitfp.operators import PhaseOperators

basis = PhaseBasis(
    bandwidth=1.0,
    gap=0.1,
    num_modes=100,
)

operators = PhaseOperators(basis)

Id = operators.identity()

phiOP = operators.phase()
```