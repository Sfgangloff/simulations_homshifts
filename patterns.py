import numpy as np 
import networkx as nx

from graphs import neighbors

def mutate_array(array:np.ndarray,i:int,j:int,new_vertex:int,graph:nx.Graph):
    if new_vertex not in list(graph.nodes):
        raise ValueError(f"The vertex {new_vertex} is not in the provided graph.")
    if all(graph.has_edge(new_vertex, neighbor) for neighbor in neighbors(i, j,array)):
        array[i, j] = new_vertex
    return array

def generate_initial_array(M: int, cycle: list) -> np.ndarray:
    if len(cycle)==0:
        raise ValueError(f"The provided cycle must not be an empty list.")
    size = 2 * M + 1
    arr = np.zeros((size, size), dtype=int)
    center = M

    # Create grids of indices
    y, x = np.ogrid[:size, :size]
    d = np.abs(x - center) + np.abs(y - center)  # Manhattan distance from center

    # Build index array from d
    index = np.where(d <= M, M - d, d - M)

    # Apply cycle values via indexing
    arr = np.array(cycle)[index % len(cycle)]

    return arr