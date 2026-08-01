import numpy as np
import warnings


class PhaseBasis:
    def __init__(self, bandwidth, gap, num_modes, dimension=None):
        self.bandwidth = float(bandwidth)
        self.gap = float(gap)
        self.num_modes = int(num_modes)

        self._validate_input()

        self.effective_dimension = (
            self._compute_effective_dimension()
        )

        if dimension is None:
            self.dimension = self.effective_dimension
        elif dimension is not None and dimension <=0:
            raise ValueError("Dimension must be a positive integer.")
        elif dimension < self.effective_dimension:
            warnings.warn(
                (
                    f"Requested dimension ({dimension}) is smaller than the effective dimensionality ({self.effective_dimension}). "
                    f"Using the effective dimensionality instead."
                ),
                UserWarning,
            )
            self.dimension = self.effective_dimension
        else:
            self.dimension = int(dimension)
        
        self.phase_spacing = 2 * np.pi / self.dimension
        self.phase_grid = np.linspace(-np.pi, np.pi, self.dimension, endpoint=False)


    def _validate_input(self):
        if self.bandwidth <= 0:
            raise ValueError("Bandwidth must be positive.")
        if self.gap <= 0:
            raise ValueError("Gap must be positive.")
        if self.num_modes <= 0:
            raise ValueError("Number of modes must be positive.")
        
    
    def _compute_effective_dimension(self):
        effective_dim = (np.pi / 2 * 
                         np.sqrt(
                             self.num_modes * self.gap
                             /
                             (2 * self.bandwidth)
                         ))
        return max(1, int(np.ceil(effective_dim)))


    @property
    def number_grid(self):
        """ 
        Retun the number-basis indices.

        The discrete number basis is labelled by
            N = 0, 1, ..., d-1, 
        where d is the dimension of the Hilbert space.
        """
        return np.arange(self.dimension)


    def fourier_matrix(self):
        """
        Construct the discrete Fourier transformation matrix between the phase basis and the number basis.

        The transformation is defined as

            |N> = (1/sqrt(d))  Σ_j exp(-i N φ_j) |φ_j>,

        where d : Hilbert-space dimension.
        """

        phase = self.phase_grid[:, None]
        number = self.number_grid[None, :]
        
        # Compute the Fourier transformation matrix
        matrix = np.exp(-1j * number * phase) / np.sqrt(self.dimension)
        return matrix

    def to_dict(self):
        return {
            "bandwidth": self.bandwidth,
            "gap": self.gap,
            "num_modes": self.num_modes,
            "effective_dimension": self.effective_dimension,
            "dimension": self.dimension,
            "phase_spacing": self.phase_spacing
        }
    

    def __repr__(self):
        return (
            "PhaseBasis(\n"
            f"    bandwidth={self.bandwidth},\n"
            f"    gap={self.gap},\n"
            f"    num_modes={self.num_modes},\n"
            f"    effective_dimension={self.effective_dimension},\n"
            f"    dimension={self.dimension}\n"
            ")"
        )

    

    