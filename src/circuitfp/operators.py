import numpy as np

class PhaseOperators:
    """
    Construct operators in the phase basis.
    
    Parameters
    ----------
    basis : PhaseBasis
        The phase basis in which the operator is defined.
    """


    def __init__(self, basis):
        self.basis = basis
        self.dimension = basis.dimension
        self.phase_grid = basis.phase_grid
        self.phase_spacing = basis.phase_spacing

    
    def identity(self):
        return np.eye(self.dimension, dtype=float)


    def phase(self):
        return np.diag(self.phase_grid)
    

    # def phase_derivative(self):
    #     """
    #     Central finite-difference approximation
    #         d / dphi
    #     with periodic boundary conditions
    #     """

    #     phase_spacing = self.phase_spacing
    #     derivative = np.zeros(
    #         (self.dimension, self.dimension)
    #     )

    #     for i in range(self.dimension):
    #         derivative[
    #             i, (i+1) % self.dimension
    #         ] = 1 / (2*phase_spacing)

    #         derivative[
    #             i, (i-1) % self.dimension
    #         ] = -1 / (2*phase_spacing)

    #     return derivative


    def to_dict(self):
        return {
            "dimension": self.dimension,
            "phase_spacing": self.phase_spacing
        }



    def __repr__(self):
        return(
            "PhaseOperator(\n)"
            f" dimension={self.dimension},\n"
            f" phase_spacing={self.phase_spacing}\n"
            ")"
        )