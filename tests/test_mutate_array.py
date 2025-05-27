import numpy as np
import networkx as nx
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import mutate_array

def test_mutate_array_success():
    G = nx.cycle_graph(5)
    array = np.array([[1, 2, 3],
                      [2, 0, 2],
                      [3, 2, 1]])
    # Vertex 2 is adjacent to all 4-neighbors of (1,1): 2,2,2,2
    new_array = mutate_array(array.copy(), 1, 1, 1, G)
    assert new_array[1, 1] == 1

def test_mutate_array_failure():
    G = nx.path_graph(5)
    array = np.array([[0, 0, 0],
                      [0, 1, 4],
                      [0, 0, 0]])
    # Vertex 1 is not adjacent to 4 in G (in path_graph, edges are only between n and n±1)
    new_array = mutate_array(array.copy(), 1, 1, 2, G)
    assert new_array[1, 1] == 1  # should stay unchanged