# PhaseBasis module
```
circuitfp.PhaseBasis
```

The `PhaseBasis` class defines a discrete phase basis for representing superconducting low-energy phase states. It determines an appropriate phase-space dimension based on the effective dimensionality of the low-energy phase Hilbert space given in the reference paper. If the user does not specify the basis dimension, the effective dimensionality is automatically used.

This class is designed for constructing the phase basis used in microscopic circuit quantization calculations.

# Physical background

For a superconducting degree of freedom, the phase variable can be represented in a finite-dimensional Hilbert space when only the relevant low-energy subspace is considered. The required number of basis states is controlled by the effective dimensionality:
$$
\mathsc{d}_\text{eff} = \frac{\pi}{2} \sqrt{\frac{n\Delta}{2\mathcal{B}}},
$$
where $n$ is the number of electronic modes, $\Delta$ is the superconducting gap, and $\mathcal{B}$ is half of the electron bandwidth.

The implementation uses the ceiling value, $\lceil \frac{\pi}{2} \sqrt{\frac{n\Delta}{2\mathcal{B}}} \rceil$ to ensure that the basis dimension is sufficient.

# Usage

```python
from circuitfp.phase_basis import PhaseBasis

basis = PhaseBasis(bandwidth=1.0, gap=0.1,num_modes=100)
print(basis)
```

outputs 

```
PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000, effective_dimension=12, dimension=12)
```

When `dimension` is not provided, the class automatically uses the effective dimensionality.

## Parameters

- `B`: half electronic bandwidth, type `float`
- `gap`: superconducting gap amplitude, type `float`
- `n`: number of electronic modes, type `int`
- `dimension`: number of phase states, tyoe `int` (optional)
    - If `dimension=None`, use $\mathsc{d} = \mathsc{d}_\text{eff}$
    - If $\mathsc{d} <> \mathsc{d}_\text{eff}$, a warning is issued and $\mathsc{d} = \mathsc{d}_\text{eff}$
    - If $\mathsc{d} > \mathsc{d}_\text{eff}$, the user-defined demension is accepted.

## Phase grid

The phase basis is constructed on a uniform grid, $\phi_j = -\pi + \delta\phi j$, where 
$$
\delta\phi = \frac{2\pi}{\mathsc{d}}.
$$
An example implementation is 

```python
basis = PhaseBasis(bandwidth=1, gap=0.1, num_modes=100,dimension=8)
print(basis.phase_grid)
```

returns `[-3.1415, -2.3561, -1.5708, -0.7854, 0, 0.7854, 1.5708, 2.3561]`.

## Attributes

`bandwidth`, `gap`, `num_modes`, `effective_dimension`, `dimension`, `phase_spacing`, `phase_grid`.

## Dictionary representation

The basis information can be exported using `basis.to_dict()`, which outputs

```python
{
    "bandwidth": 1.0,
    "gap": 0.1,
    "num_modes": 100,
    "effective_dimension": 4,
    "dimension": 4,
    "phase_spacing": 1.5708
}
```


# Relationship with Overlap

`PhaseBasis` generates the phase grid used by overlap calculations. For example,

```python
from circuitfp.overlap import Overlap

basis = PhaseBasis(bandwidth=1, gap=0.1, num_modes=100, dimension=20)

ov = Overlap(B=basis.bandwidth, gap=basis.gap, n=basis.num_modes, phase_grid=basis.phase_grid)

matrix = ov.overlap_matrix()
```

The resulting output represents the overlap matrix $\mathcal{W}_{ij}$.
