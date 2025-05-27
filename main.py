import numpy as np
import networkx as nx
import random
import matplotlib.pyplot as plt

from patterns import generate_initial_array, mutate_array
from vizualisation import initialize_heatmap, update_heatmap


def simulate(graph: nx.Graph, array: np.ndarray, N: int) -> np.ndarray:
    rows, cols = array.shape
    vertices = list(graph.nodes)

    fig, ax, im = initialize_heatmap(array) 

    for _ in range(N):
        i = random.randint(1, rows - 2)
        j = random.randint(1, cols - 2)
        new_vertex = random.choice(vertices)
        current_array = array.copy()
        array = mutate_array(array,i,j,new_vertex,graph)
        if not np.array_equal(array,current_array):
            update_heatmap(im, array)
            # print_array_with_highlight(array, i, j)        

    plt.ioff()
    plt.show()
    return array

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (0, 1), (1, 2), (2, 0),  # Triangle: 0-1-2-0
        (0, 3), (3, 4), (4, 0)   # Triangle: 0-3-4-0
    ]) 

    # Generates initial configuration
    arr = generate_initial_array(27,[0,1,2,0,3,4,0])

    # Apply series of mutations
    new_arr = simulate(G, arr, N=100000)