import pytest
import numpy as np
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import generate_initial_array

def test_shape_correctness():
    M = 3
    cycle = [1, 2, 3]
    arr = generate_initial_array(M, cycle)
    assert arr.shape == (2*M + 1, 2*M + 1)

def test_center_value():
    M = 4
    cycle = [10, 20, 30, 40, 50]
    arr = generate_initial_array(M, cycle)
    center_val = arr[M, M]
    assert center_val == 50  # cycle[M - M] = cycle[0]

def test_symmetry():
    M = 3
    cycle = [1, 2, 3, 4]
    arr = generate_initial_array(M, cycle)
    assert np.array_equal(arr, np.flip(arr, axis=0))
    assert np.array_equal(arr, np.flip(arr, axis=1))

def test_wrapping_cycle_short():
    M = 4
    cycle = [9, 8]  # Very short cycle, will wrap
    arr = generate_initial_array(M, cycle)
    # All values must be 9 or 8
    unique_values = np.unique(arr)
    assert set(unique_values).issubset({9, 8})

def test_wrapping_cycle_one_element():
    M = 5
    cycle = [7]
    arr = generate_initial_array(M, cycle)
    # Should be filled with 7s everywhere
    assert np.all(arr == 7)

def test_empty_cycle_raises():
    M = 2
    cycle = []
    with pytest.raises(ValueError, match="empty list"):
        generate_initial_array(M, cycle)