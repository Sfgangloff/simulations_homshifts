import numpy as np
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graphs import neighbors

def test_neighbors_valid():
    arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
    result = list(neighbors(1, 1, arr))
    assert result == [2, 8, 4, 6]  # up, down, left, right

@pytest.mark.parametrize("i,j", [
    (-1, 0),  # Negative index
    (3, 1),   # i out of bounds
    (1, 3),   # j out of bounds
])
def test_neighbors_outside_error(i, j):
    arr = np.zeros((3, 3))
    with pytest.raises(ValueError, match="outside of the array"):
        list(neighbors(i, j, arr))

@pytest.mark.parametrize("i,j", [
    (0, 1),   # Top border
    (2, 1),   # Bottom border
    (1, 0),   # Left border
    (1, 2),   # Right border
])
def test_neighbors_border_error(i, j):
    arr = np.zeros((3, 3))
    with pytest.raises(ValueError, match="on the border of the array"):
        list(neighbors(i, j, arr))