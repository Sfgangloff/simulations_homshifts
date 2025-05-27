import numpy as np

def print_array_with_highlight(array: np.ndarray, hi: int, hj: int):
    for i in range(array.shape[0]):
        row = ""
        for j in range(array.shape[1]):
            value = array[i, j]
            if i == hi and j == hj:
                row += f"\033[91m{value:3d}\033[0m "  # red
            else:
                row += f"\033[97m{value:3d}\033[0m "  # white
        print(row)
    print()  # Extra line for readability