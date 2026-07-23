import numpy as np
import pytest

from circuitfp.phase_basis import PhaseBasis
from circuitfp.operators import PhaseOperators


@pytest.fixture
def test_basis():
    return PhaseBasis(
        bandwidth = 1.0,
        gap = 0.1,
        num_modes = 100,
        dimension = 51
    )


@pytest.fixture
def operators(test_basis):
    return PhaseOperators(test_basis)



# test for identity operator
def test_identity_matrix(operators):
    Id = operators.identity()

    np.testing.assert_allclose(
        Id, np.eye(Id.shape[0])
    )


# tests for phase operator
def test_phase_operator_diagonal(test_basis, operators):
    phi = operators.phase()

    np.testing.assert_allclose(np.diag(phi), test_basis.phase_grid)


def test_phase_operator_offdiagonal(operators):
    phi = operators.phase()
    phi_off = phi - np.diag(np.diag(phi))

    np.testing.assert_allclose(phi_off, np.zeros_like(phi_off))


# # tests for phase derivative operator
# def test_phase_derivative_periodic(test_basis,operators):
#     Dphase = operators.phase_derivative()
#     dphi = test_basis.phase_spacing

#     assert np.isclose(
#         Dphase[0,-1], -1 / (2*dphi)
#     )

#     assert np.isclose(
#         Dphase[-1,0], 1 / (2*dphi)
#     )


# def test_phase_derivative_trace(operators):
#     Dphase = operators.phase_derivative()

#     assert np.isclose(np.trace(Dphase), 0)