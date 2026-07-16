from circuitfp.overlap import Overlap
import numpy as np


def test_phase_difference():
    ov = Overlap(B=1.0, gap=0.1, n=100, 
                 phase1=np.pi/4, 
                 phase2=np.pi/6
    )
    expected_phase_difference = np.pi/4 - np.pi/6
    
    assert np.isclose(
        ov.phase_difference, 
        expected_phase_difference
    )


def test_same_phase():
    B=1.0
    gap=0.1
    n=100

    ov = Overlap(B=B, gap=gap, n=n, phase1=np.pi/7,phase2=np.pi/7)
    expected_overlap = 1
    assert np.isclose(ov.overlap(), expected_overlap)


def test_phase_reversal():
    B=1.0
    gap=0.1
    n=100

    ov1 = Overlap(B=B, gap=gap, n=n, phase1=np.pi/4, phase2=np.pi/6)
    ov2 = Overlap(B=B, gap=gap, n=n, phase1=np.pi/6, phase2=np.pi/4)

    assert np.isclose(ov1.overlap(), np.conj(ov2.overlap()))


def test_overlap_magnitude_less_than_one():

    ov = Overlap(
        B=1.0,
        gap=0.1,
        n=100,
        phase1=np.pi/2,
        phase2=0
    )

    assert abs(ov.overlap()) <= 1


def test_larger_phase_difference_smaller_overlap():

    B=1
    gap=0.1
    n=100
    phase1=0

    ov1 = Overlap(B=B, gap=gap, n=n, phase1=phase1, phase2=0.1)
    ov2 = Overlap(B=B, gap=gap, n=n, phase1=phase1, phase2=1.0)

    assert abs(ov2.overlap()) < abs(ov1.overlap())