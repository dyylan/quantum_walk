import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from qualk.functions import fits
from scipy.optimize import curve_fit

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

 
def marked_state_amplitudes_against_time_with_noise(dimensions, chain, end_time):
    index = 'times'
    noises = [0.01, 0.05, 0.1, 0.2]
    noise_files = [f'data/p2_{chain}/alpha=1_noise={noise}_lat_dim=1_dim={dimensions}.csv' 
            for noise in noises]
    noise_data = [pd.read_csv(noise_file, index_col=index) for noise_file in noise_files]
    times = noise_data[0][:end_time].index
    amplitude_data = [data[['norm_overlaps']][:end_time] for data in noise_data]
    fig, ax = plt.subplots()
    for i, y in enumerate(amplitude_data):
        ax.plot(times, y)
    ax.legend([f'noise = {noise}' for noise in noises])
    ax.set(xlabel='$time~(s/\hbar)$')
    ax.set(ylabel='$|\langle m| U |s\\rangle|^2$')
    ax.grid()
    plt.savefig(save_directory + f'{chain}_marked_state_amplitudes_against_time_with_noise_dim={dimensions}_comparison.png')
    plt.show()


def p2_various_alpha(dimensions, chain):
    index = 'times'
    alphas = [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
    alpha_files = [f'data/p2_{chain}/alpha={alpha}_lat_dim=1_dim={dimensions}.csv' 
                    for alpha in alphas]
    data = [pd.read_csv(alpha_file, index_col=index) for alpha_file in alpha_files] 
    times = data[0][:120].index
    data = [datum[['norm_overlaps']][:120] for datum in data]
    fig, ax = plt.subplots()
    for i, y in enumerate(data):
        ax.plot(times, y)
    ax.legend([f'$\\alpha = {alpha}$' for alpha in alphas])
    ax.set(xlabel='time$~(s/\hbar)$')
    ax.set(ylabel='$|\langle m| U |s\\rangle|^2$')
    ax.grid()
    plt.savefig(save_directory + f'{chain}_amplitude_against_times_alpha_comparison.png')
    plt.show()    


def p2_various_m(dimensions, chain):
    index = 'times'
    marked_states = [2, 5, 21, 40, 72]
    marked_files = [f'data/p2_{chain}/alpha=1_m={marked_state}_lat_dim=1_dim={dimensions}.csv' 
                    for marked_state in marked_states]
    data = [pd.read_csv(marked_file, index_col=index) for marked_file in marked_files] 
    times = data[0].index
    data = [datum[['norm_overlaps']] for datum in data]
    fig, ax = plt.subplots()
    for i, y in enumerate(data):
        ax.plot(times, y)
    ax.legend([f'm = {m}' for m in marked_states])
    ax.set(xlabel='time$~(s/\hbar)$')
    ax.set(ylabel='$|\langle m| U |s\\rangle|^2$')
    ax.grid()
    plt.savefig(save_directory + f'{chain}_amplitude_against_times_marked_state_comparison.png')
    plt.show()


def p4_various_alpha(chain, logplot=False):
    index = 'dimensions'
    alphas = [1, 1.1, 1.4, 1.5]
    # alphas = [1, 1.1, 1.2, 1.3, 1.4]
    alpha_files = [f'data/p4_{chain}/alpha={alpha}_lat_dim=1.csv' 
                    for alpha in alphas]
    data = [pd.read_csv(alpha_file, index_col=index) for alpha_file in alpha_files] 
    data = [datum[:31] for datum in data]
    dimensions = data[0].index
    
    scaling = []
    for i, datum in enumerate(data):    
        popt, pcov = curve_fit(fits.power_fit, dimensions, datum['opt_times'].to_list(), bounds=(0, [10., 1., 0.8]))        
        print(f'Fit for alpha={alphas[i]} gives: y = {popt[0]} * x^{popt[1]} + {popt[2]}')
        scaling.append(popt)
    popt = scaling[0]
    sqrt_N_fit = fits.power_fit(dimensions, popt[0], 0.5, popt[2])
    N_three_quarters_fit = fits.power_fit(dimensions, popt[0], 0.55, popt[2])

    N_fits = [sqrt_N_fit, N_three_quarters_fit]

    fig, ax = plt.subplots()
    for i, y in enumerate(data):
        ax.plot(dimensions, y)
    for y in N_fits:
        ax.plot(dimensions, y, linestyle='dotted')
    ax.legend([f'$\\alpha = {alpha}$, fit $N^{{ {scaling[i][1]:.4f} }}$' for i, alpha in enumerate(alphas)] + ['$N^{0.50}$ fit', '$N^{0.55}$ fit'])
    if logplot:
        ax.set(xscale='log')
        ax.set(yscale='log')        
    ax.set(xlabel='$N$')
    ax.set(ylabel='optimum time$~(s/\hbar)$')
    ax.grid()
    plt.savefig(save_directory + f'{chain}_times_against_dimensions_alpha_comparison.png')
    plt.show()    


def p3_alpha_0_and_1(chain):
    index = 'dimensions'
    alphas = [0, 1]
    # alphas = [1, 1.1, 1.2, 1.3, 1.4]
    alpha_files = [f'data/p3_{chain}/alpha={alpha}_lat_dim=1.csv' 
                    for alpha in alphas]
    data = [pd.read_csv(alpha_file, index_col=index) for alpha_file in alpha_files] 
    dimensions = data[0].index
    min_gaps = [datum[['min_gaps']] for datum in data]

    popt, pcov = curve_fit(fits.inverse_power_fit, dimensions, min_gaps[0]['min_gaps'].to_list(), bounds=(0, [10., 1., 1.]))
    print(f'Fit for inverse power gives: y = {popt[0]} / x^{popt[1]} + {popt[2]}')

    inverse_sqrt_N = fits.inverse_power_fit(dimensions, popt[0], 0.5, popt[2])

    inverse_N_three_quarters = fits.inverse_power_fit(dimensions, popt[0], 0.75, popt[2])

    inverse_N = fits.inverse_power_fit(dimensions, popt[0], 1, popt[2])

    ys = min_gaps + [inverse_sqrt_N, inverse_N_three_quarters, inverse_N]
    
    fig, ax = plt.subplots()
    linestyles = ['solid', 'solid', 'dotted', 'dotted', 'dotted']
    for i, y in enumerate(ys):
        ax.plot(dimensions, y, linestyle=linestyles[i])
    ax.legend(['min($E_1-E_0$) for $\\alpha=0$',
               'min($E_1-E_0$) for $\\alpha=1$',
                '$N^{-0.5}$',
                '$N^{-0.75}$',
                '$N^{-1}$'])
    ax.set(xlabel='$N$')
    ax.grid() 
    plt.savefig(save_directory + f'{chain}_p3_alpha_0_and_1.png')
    plt.show()    


def eigenvalues_function_plots_for_ring():
    # Eigenvalues of 
    pass


def time_against_N(chain, alpha):
    index = 'dimensions'
    alphas = 1
    alpha_file = f'data/p4_{chain}/alpha={alpha}_lat_dim=1.csv'
    data = pd.read_csv(alpha_file, index_col=index)
    data = data[-30:]
    dimensions = data.index
    data = data[['opt_times']]

    popt1, pcov1 = curve_fit(fits.power_fit, dimensions, data['opt_times'].to_list(), bounds=(0, [10., 1., 1.]))
    print(f'Fit for power gives: y = {popt1[0]} * x^{popt1[1]} + {popt1[2]}')
    sqrt_N_fit = fits.power_fit(dimensions, popt1[0], 0.5, popt1[2])

    popt, pcov = curve_fit(fits.power_fit_over_log, dimensions, data['opt_times'].to_list(), bounds=(0, [1., 1., 10.]))
    print(f'Fit for power gives: y = {popt[0]} * x^{popt[1]} / log(x)^0.25 + {popt[2]}')
    power_over_log_fit = fits.power_fit_over_log(dimensions, popt[0], 0.75, popt[2])

    # popt2, pcov2 = curve_fit(fits.power_fit_over_log, dimensions, data['opt_times'].to_list(), bounds=(0, [10., 10.,]))
    # print(f'Fit for power gives: y = {popt2[0]} * x^0.75 / log(x)^0.25 + {popt2[1]}')
    # power_over_log_fit = fits.power_fit_over_log(dimensions, popt2[0], popt2[1])

    N_fits = [sqrt_N_fit, power_over_log_fit]

    fig, ax = plt.subplots()
    ax.plot(dimensions, data)
    for y in N_fits:
        ax.plot(dimensions, y, linestyle='dotted')
    ax.legend([f'$\\alpha = {alpha}$'] + ['$1/N^{0.50}$ fit', '$N^{0.75}/\log(N)^{0.25}$ fit'])
    ax.set(xlabel='$N$')
    ax.set(ylabel='optimum time$~(s/\hbar)$')
    ax.grid()
    plt.savefig(save_directory + f'{chain}_times_against_dimensions_alpha_comparison.png')
    plt.show()    


def time_against_N_log_plot(chain, alpha):
    index = 'dimensions'
    alphas = 1
    alpha_file = f'data/p4_{chain}/alpha={alpha}_lat_dim=1.csv'
    data = pd.read_csv(alpha_file, index_col=index)
    dimensions = data.index
    data = data[['opt_times']]

    popt1, pcov1 = curve_fit(fits.power_fit, dimensions, data['opt_times'].to_list(), bounds=(0, [10., 1., 1.]))
    print(f'Fit for power gives: y = {popt1[0]} * x^{popt1[1]} + {popt1[2]}')

    sqrt_N_fit = fits.power_fit(dimensions, popt1[0], 0.5, popt1[2])

    six_five_N_fit = fits.power_fit(dimensions, popt1[0], 0.55, popt1[2])

    three_quarters_N_fit = fits.power_fit(dimensions, popt1[0], 0.75, popt1[2])

    popt, pcov = curve_fit(fits.power_fit_over_log, dimensions, data['opt_times'].to_list(), bounds=(0, [10., 1., 10.]))
    print(f'Fit for power gives: y = {popt[0]} * x^{popt[1]} / log(x)^0.25 + {popt[2]}')
    power_over_log_fit = fits.power_fit_over_log(dimensions, popt[0], 0.75, popt[2])

    # popt2, pcov2 = curve_fit(fits.power_fit_over_log, dimensions, data['opt_times'].to_list(), bounds=(0, [10., 10.,]))
    # print(f'Fit for power gives: y = {popt2[0]} * x^0.75 / log(x)^0.25 + {popt2[1]}')
    # power_over_log_fit = fits.power_fit_over_log(dimensions, popt2[0], popt2[1])

    N_fits = [sqrt_N_fit, six_five_N_fit, three_quarters_N_fit]

    fig, ax = plt.subplots()
    ax.plot(dimensions, data)
    for y in N_fits:
        ax.plot(dimensions, y, linestyle='dotted')
    ax.legend([f'$\\alpha = {alpha}$'] + ['$N^{0.50}$ fit', '$N^{0.55}$ fit', '$N^{0.75}$ fit'])
    ax.set(xscale='log')
    ax.set(yscale='log')
    ax.set(xlabel='$N$')
    ax.set(ylabel='optimum time$~(s/\hbar)$')
    ax.grid()
    plt.savefig(save_directory + f'{chain}_times_against_dimensions_alpha_comparison_log_plot.png')
    plt.show()    


def time_against_N_log_plot_ring_chord():
    index = 'dimensions'
    alphas = 1
    ring_file = f'data/p4_ring/alpha=1_lat_dim=1.csv'
    chord_file = f'data/p4_chord/alpha=1_lat_dim=1.csv'
    ring_data = pd.read_csv(ring_file, index_col=index)
    chord_data = pd.read_csv(chord_file, index_col=index)
    dimensions = ring_data.index

    popt1, pcov1 = curve_fit(fits.power_fit, dimensions, ring_data['opt_times'].to_list(), bounds=(0, [10., 1., 1.]))
    print(f'Fit for power gives: y = {popt1[0]} * x^{popt1[1]} + {popt1[2]}')

    sqrt_N_fit = fits.power_fit(dimensions, popt1[0], 0.5, popt1[2])

    six_five_N_fit = fits.power_fit(dimensions, popt1[0], 0.51, popt1[2])

    N_fits = [sqrt_N_fit, six_five_N_fit]

    fig, ax = plt.subplots()
    ax.plot(dimensions, ring_data)
    ax.plot(dimensions, chord_data)
    for y in N_fits:
        ax.plot(dimensions, y, linestyle='dotted')
    ax.legend([f'ring, $\\alpha = 1$', f'chord, $\\alpha = 1$'] + ['$N^{0.50}$ fit', '$N^{0.51}$ fit'])
    ax.set(xscale='log')
    ax.set(yscale='log')
    ax.set(xlabel='$N$')
    ax.set(ylabel='optimum time$~(s/\hbar)$')
    ax.grid()
    plt.savefig(save_directory + f'ring_and_chord_times_against_dimensions_log_plot.png')
    plt.show()    


if __name__ == "__main__":
    # open_ring_chord_decoherence(8)
    marked_state_amplitudes_against_time_with_noise(8, 'ring', 20)
    # p2_various_alpha(1024, 'ring')
    # p2_various_m(1024, 'open')
    # p4_various_alpha('ring', True)
    # time_against_N('ring', 1)
    # p3_alpha_0_and_1('open')
    # time_against_N_log_plot('open', 1)
    # time_against_N_log_plot_ring_chord()
