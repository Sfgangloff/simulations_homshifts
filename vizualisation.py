import matplotlib.pyplot as plt


def initialize_heatmap(array):
    plt.ion()
    fig, ax = plt.subplots()
    im = ax.imshow(array, cmap='viridis', interpolation='none', vmin=array.min(), vmax=array.max())
    plt.colorbar(im, ax=ax)
    return fig, ax, im

def update_heatmap(im, array):
    im.set_data(array)
    im.set_clim(vmin=array.min(), vmax=array.max())  # Optional: rescale color map
    plt.draw()
    plt.pause(0.01)