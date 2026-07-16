import numpy as np

class Overlap:

    def __init__(self, B=None, gap=None, n=None, basis=None, phase1, phase2):
        self.bandwidth = B
        self.gap = gap
        self.num_modes = n
        self.phase1 = np.asarray(phase1)
        self.phase2 = np.asarray(phase2)

        if basis is not None:
            self.bandwidth = basis.bandwidth
            self.gap = basis.gap
            self.num_modes = basis.num_modes
        else:
            self.bandwidth = B
            self.gap = gap
            self.num_modes = n

    

    def overlap(self):
        # Calculate the overlap value based on the phase difference
        phase_difference = self.phase1 - self.phase2
        overlap_value = np.exp(self.num_modes * (
            1j * phase_difference / 2
            -
            np.pi * self.gap / (16 * self.bandwidth)
            *
            phase_difference**2
        )
        )
        return overlap_value
    

    def overlap_matrix(self):
        # Check if phase1 and phase2 are 1D arrays
        if self.phase1.ndim != 1 or self.phase2.ndim != 1:
            raise ValueError("phase1 and phase2 must be 1D arrays")
        
        # Check if phase1 and phase2 have the same length
        if self.phase1.shape != self.phase2.shape:
            raise ValueError(
                "overlap_matrix() requires phase1 and phase2 to have the same length."
            )
        
        # Check if phase and phase are identical
        if not np.allclose(self.phase1, self.phase2):
            raise ValueError(
                "overlap_matrix() requires phase1 and phase2 to be identical."
            )
            
        # Create an overlap matrix for the given num_modes in phase space
        dph = self.phase1[:, None] - self.phase2[None, :]
        overlap_matrix = np.exp(self.num_modes * (
            1j * dph / 2
            -
            np.pi * self.gap / (16 * self.bandwidth)
            *
            dph**2
        )
        )
        return overlap_matrix   