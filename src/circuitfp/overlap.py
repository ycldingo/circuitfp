import numpy as np

class Overlap:

    def __init__(self, phase1=None, phase2=None, phase_grid=None, bandwidth=None, gap=None, num_modes=None, basis=None):
        self.basis = basis
        self.phase1 = (
            np.asarray(phase1)
            if phase1 is not None
            else None
        )
        self.phase2 = (
            np.asarray(phase2)
            if phase2 is not None
            else None
        )
        self.phase_grid = np.asarray(phase_grid) if phase_grid is not None else None
        if basis is not None:
            self.bandwidth = float(basis.bandwidth)
            self.gap = float(basis.gap)
            self.num_modes = int(basis.num_modes)
            self.phase_grid = basis.phase_grid
        else:
            if bandwidth is None or gap is None or num_modes is None:
                raise ValueError("If basis is not provided, bandwidth, gap, and num_modes must be specified.")
            self.bandwidth = float(bandwidth)
            self.gap = float(gap)
            self.num_modes = int(num_modes)

    

    def overlap(self):
        # Calculate the overlap value based on the phase difference
        if self.phase_grid is not None:
            raise ValueError("For overlap calculation, phase1 and phase2 must be provided, not phase_grid.")
        else:
            phase_difference = np.asarray(self.phase1) - np.asarray(self.phase2)
        
        overlap_value = np.exp(self.num_modes * (
            1j * phase_difference / 2
            -
            np.pi * self.gap / (16 * self.bandwidth)
            *
            phase_difference**2
        )
        )

        if np.ndim(overlap_value) == 0:
            return overlap_value.item()  # Return as a scalar if it's a single value
        
        return overlap_value
    

    def overlap_matrix(self):
        # Check if phase_grid id 1D arrays
        if self.phase_grid.ndim != 1:
            raise ValueError("phase_grid must be 1D arrays")
        
            
        # Create an overlap matrix for the given num_modes in phase space
        phase_difference = np.asarray(self.phase_grid)[:, None] - np.asarray(self.phase_grid)[None, :]
        overlap_matrix = np.exp(self.num_modes * (
            1j * phase_difference / 2
            -
            np.pi * self.gap / (16 * self.bandwidth)
            *
            phase_difference**2
        )
        )
        return overlap_matrix   