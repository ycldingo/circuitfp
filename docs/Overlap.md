# Overlap module

```
circuitfp.Overlap
```

The `Overlap` class evaluates the overlap bwteen two BCS phase states.


# Mathematical background

The overlap between two BCS phase states is given by

$$\mathcal{W}(\phi_1,\phi_2)\equiv \langle \Psi(\phi_1) | \Psi(\phi_2) \rangle = \exp \Big[ n \Big( \frac{i}{2}\varphi - \frac{\pi\Delta}{16 \mathcal{B}} \varphi^2 \Big) \Big] = \mathcal{W}(\varphi)$$,

where $\varphi = \phi_2 - \phi_1$ is the phase difference.


# Class

```python
Overlap(B, gap, n, phase1, phase2)
```

# Parameters

- `B`: half electronic bandwidth, type `float`
- `gap`: superconducting gap amplitude, type `float`
- `n`: number of electronic modes, type `int`
- `phase1`: phase coordinate, allowed input: `float` and `ndarray`
- `phase1`: phase coordinate, allowed input: `float` and `ndarray`


# Method

## overlap()

Returnd $\mathcal{W} (\phi_1, \phi_2)$

| Input | Output |
|--------|---------|
| scalar | complex |
| ndarray | ndarray |

Example

```python
Overlap(B=1, gap=0.001, n=10**3, phase1=0, phase2=np.pi/3).overlap()
```

## overlap_matrix()

This function constructs the overlap matrix $\mathcal{W}_{ij} = \mathcal{W}(\phi_i,\phi_j)$.

Requirements

- `phase1` and `phase2` must both be one-dimensional array
- `phase1` and `phase2` must have identical grids

Returns `complex ndarray` of shape `(N,N)`, where `N` is the number of elements in `phase1` or `phase2` array

Example

```python
phase = np.linspace(-np.pi, ip.pi, 501)

Overlap(B=1, gap=0.001, n=10**3, phase1=phase, phase2=phase).overlap_matrix()
```

outputs a `(501,501)` array.

### Exceptios

Raises `ValueError` when 
- phase arrays are not one-dimensional
- phase grids have different lengths
- phase grids are not identical

