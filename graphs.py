import numpy as np

def neighbors(i:int,j:int,array:np.ndarray):
    rows, cols = array.shape
    if i < 0 or i > rows - 1 or j < 0 or j > cols - 1: 
        raise ValueError(f"Position ({i}, {j}) is outside of the array of shape {array.shape}. Must be an interior point.")
    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
        raise ValueError(f"Position ({i}, {j}) is on the border of the array of shape {array.shape}. Must be an interior point.")
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        yield array[ni, nj]