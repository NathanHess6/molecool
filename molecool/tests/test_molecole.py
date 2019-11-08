import molecool
import numpy as np
import pytest

def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = molecool.data.atomic_weights['C'] + molecool.data.atomic_weights['H'] +\
         molecool.data.atomic_weights['H'] + molecool.data.atomic_weights['H']

    assert actual_mass == calculated_mass

def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])

    assert np.array_equal(center_of_mass, expected_center)
