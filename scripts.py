import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

save_directory = 'plots/script_plots/'


def open_ring_chord_decoherence(dimensions):
    open_file = f'data/p2_d_open/alpha=1_lat_dim=1_dim={dimensions}.csv'
    ring_file = f'data/p2_d_ring/alpha=1_lat_dim=1_dim={dimensions}.csv'
    chord_file = f'data/p2_d_chord/alpha=1_lat_dim=1_dim={dimensions}.csv'
    index = 'times'
    
    open_df = pd.read_csv(open_file, index_col=index)
    ring_df = pd.read_csv(ring_file, index_col=index)
    chord_df = pd.read_csv(chord_file, index_col=index)

    times = open_df.index
    open_overlaps = open_df[['overlaps']]
    ring_overlaps = ring_df[['overlaps']]
    chord_overlaps = chord_df[['overlaps']]

    ys = [open_overlaps, ring_overlaps, chord_overlaps]
    fig, ax = plt.subplots()
    linestyles = ['dashed', 'dashed', 'dashed']
    for i, y in enumerate(ys):
        ax.plot(times, y, linestyle=linestyles[i])
    ax.legend(['open chain',
                'ring chain',
                'chord chain'])
    ax.set(xlabel='$time~(s/\hbar)$')
    ax.set(ylabel='$|\langle m| U |s\\rangle|^2$')
    ax.grid()
    plt.savefig(save_directory + f'decoherence_open_ring_chord_dim={dimensions}_comparison.png')
    plt.show()


if __name__ == "__main__":
    open_ring_chord_decoherence(8)