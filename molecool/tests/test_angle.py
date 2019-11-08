"""
Unit testing for the measure module.
"""

import molecool
import numpy as np

def test_calculate_angle():

    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees = 'true')

    assert expected_angle == calculated_angle
