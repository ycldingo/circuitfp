from circuitfp.phase_basis import PhaseBasis
import numpy as np
import pytest


def test_initialisation():
    basis = PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000)
    assert basis.bandwidth == 1.0
    assert basis.gap == 0.1
    assert basis.num_modes == 1000


# tests for the dimensionality
def test_effective_dimension():
    basis = PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000)
    
    expected = int(
        np.ceil(
            np.pi/2 *
            np.sqrt(
                basis.num_modes*basis.gap/(2*basis.bandwidth)
            )
        )
    )
    
    assert basis.effective_dimension == expected


def test_default_dimension():
    basis = PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000)
    assert basis.dimension == basis.effective_dimension


def test_user_dimension_more_than_effective():
    basis = PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000, dimension=2000)
    assert basis.dimension == 2000


def test_small_dimension_warning():
    with pytest.warns(UserWarning):
        basis = PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000, dimension=10)
    assert basis.dimension == basis.effective_dimension


# tests for phase spacing and phase grid
def test_phase_spacing():
    basis = PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000, dimension=100)

    assert np.isclose(basis.phase_spacing, 2 * np.pi / 100)


def test_phase_grid_length():
    basis = PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000, dimension=100)

    assert len(basis.phase_grid) == 100


def test_phase_grid_start():
    basis = PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000, dimension=100)

    assert np.isclose(basis.phase_grid[0], -np.pi)


def test_phase_grid_spacing():
    basis = PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000, dimension=100)
    expected = np.diff(basis.phase_grid)

    assert np.allclose(expected, basis.phase_spacing)


# test for system parameters
def test_invalid_param():
    with pytest.raises(ValueError):
        PhaseBasis(bandwidth=0, gap=0.1, num_modes=1000)
    with pytest.raises(ValueError):
        PhaseBasis(bandwidth=1.0, gap=0, num_modes=1000)
    with pytest.raises(ValueError):
        PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=0)

# test for dictionary
def test_to_dict():
    basis = PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000, dimension=100)
    basis_dict = basis.to_dict()

    assert basis_dict["bandwidth"] == 1.0
    assert basis_dict["gap"] == 0.1
    assert basis_dict["num_modes"] == 1000

    assert isinstance(basis_dict, dict)


# test for __repr__
def test_repr():
    basis = PhaseBasis(bandwidth=1.0, gap=0.1, num_modes=1000, dimension=100)
    repr_str = repr(basis)

    assert "PhaseBasis" in repr_str
    assert "bandwidth" in repr_str
    assert "gap" in repr_str

