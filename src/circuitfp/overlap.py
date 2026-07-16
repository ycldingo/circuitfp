import numpy as np

class Overlap:

    def __init__(self, B, gap, n, phase1, phase2):
        self.bandwidth = B
        self.gap = gap
        self.num_modes = n
        self.phase1 = phase1
        self.phase2 = phase2
        self.phase_difference = self.phase1 - self.phase2
    

    def overlap(self):
        # Calculate the overlap value based on the phase difference
        overlap_value = np.exp(self.num_modes * (
            1j * self.phase_difference / 2
            +
            np.pi * self.gap / (16 * self.bandwidth)
        ))
        return overlap_value