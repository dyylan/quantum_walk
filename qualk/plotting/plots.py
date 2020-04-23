import matplotlib.pyplot as plt 
import numpy as np
from scipy.optimize import curve_fit
from ..config import parameters
from ..functions import fits


def save_insert():
    return '_' + parameters['save_tag'] if parameters['save_tag'] else ''


def p1_amplitudes_plot(alpha, dimensions, gammasN, amps, e1_minus_e0, save=False, chain='open', lattice_d=1):
    fig, ax = plt.subplots()
    linestyles = ['solid', 'solid', 'dashed', 'dashed']
    for i, amp in enumerate(amps):
        ax.plot(gammasN, amp, linestyle=linestyles[i])
    ax.plot(gammasN, e1_minus_e0)
    ax.legend(['$|\langle m|\psi_0 \\rangle |^2$', 
                '$|\langle m|\psi_1 \\rangle |^2$', 
                '$|\langle s|\psi_0 \\rangle |^2$', 
                '$|\langle s|\psi_1 \\rangle|^2$',
                '$E_1 - E_0$'])
    ax.set(xlabel='$\gamma  N$')
    ax.grid()
    if save:
        chain_tag = '_' + chain
        plt.savefig(f'plots/p1{chain_tag}/alpha={alpha}{save_insert()}_lat_dim={lattice_d}_dim={dimensions}.png')
    plt.show()


def p2_overlaps_plot(times, overlaps, alpha, gammaN, dimensions, marked, save=False, chain='open', lattice_d=1):
    norm_overlaps = np.abs(np.multiply(np.conj(overlaps), overlaps))
    real_overlaps = np.real(overlaps)
    imag_overlaps = np.imag(overlaps)
    ys = [real_overlaps, imag_overlaps, norm_overlaps]
    fig, ax = plt.subplots()
    linestyles = ['dashed', 'dashed', 'solid']
    for i, y in enumerate(ys):
        ax.plot(times, y, linestyle=linestyles[i])
    ax.legend(['Re$(\langle m| U |s\\rangle)$',
                'Im$(\langle m| U |s\\rangle)$',
                '$|\langle m| U |s\\rangle|^2$'])
    ax.set(xlabel='$time~(s/\hbar)$')
    ax.grid()
    if save:
        chain_tag = '_' + chain
        plt.savefig(f'plots/p2{chain_tag}/alpha={alpha}{save_insert()}_gammaN={gammaN}_m={marked}_lat_dim={lattice_d}_N={dimensions}.png')
    plt.show()


def p2_d_overlaps_plot(times, overlaps, alpha, gammaN, dimensions, marked, kappa, save=False, chain='open', lattice_d=1):
    probabilites = np.real(overlaps)
    fig, ax = plt.subplots()
    ax.plot(times, overlaps, linestyle='solid')
    ax.set(xlabel='$time~(s/\hbar)$')
    ax.set(ylabel='$|\langle m| U |s\\rangle|^2$')
    ax.grid()
    if save:
        chain_tag = '_' + chain
        plt.savefig(f'plots/p2_d{chain_tag}/alpha={alpha}{save_insert()}_gammaN={gammaN}_m={marked}_lat_dim={lattice_d}_N={dimensions}_k={kappa}.png')
    plt.show()


def p3_min_gap_against_N_plot(dimensions, min_gaps, alpha, gammaN, save=False, chain='open', lattice_d=1):
    
    popt, pcov = curve_fit(fits.inverse_power_fit, dimensions, min_gaps, bounds=(0, [10., 1., 1.]))
    print(f'Fit for inverse power gives: y = {popt[0]} / x^{popt[1]} + {popt[2]}')

    inverse_sqrt_N = fits.inverse_power_fit(dimensions, popt[0], 0.5, popt[2])

    inverse_N_three_quarters = fits.inverse_power_fit(dimensions, popt[0], 0.75, popt[2])

    inverse_N = fits.inverse_power_fit(dimensions, popt[0], 1, popt[2])

    ys = [min_gaps, inverse_sqrt_N, inverse_N_three_quarters, inverse_N]
    
    fig, ax = plt.subplots()
    linestyles = ['solid', 'dotted', 'dotted', 'dotted']
    for i, y in enumerate(ys):
        ax.plot(dimensions, y, linestyle=linestyles[i])
    ax.legend(['min($E_1-E_0$)',
                '$1/N^{1/2}$',
                '$1/N^{3/4}$',
                '$1/N$'])
    ax.set(xlabel='$N$')
    ax.grid() 
    if save:
        chain_tag = '_' + chain
        lat_d_tag = '_lat_dim=2' if lattice_d==2 else ''
        plt.savefig(f'plots/p3{chain_tag}/min_gaps_alpha={alpha}{lat_d_tag}{save_insert()}.png')
    plt.show()


def p4_time_against_N_plot(dimensions, times, alpha, gammaN, save=False, chain='open', lattice_d=1):
    
    popt, pcov = curve_fit(fits.power_fit, dimensions, times, bounds=(0, [10., 1., 1.]))
    print(f'Fit for power gives: y = {popt[0]} * x^{popt[1]} + {popt[2]}')

    sqrt_N_fit = fits.power_fit(dimensions, popt[0], 0.5, popt[2])

    N_three_quarters_fit = fits.power_fit(dimensions, popt[0], 0.75, popt[2])

    N_fit = fits.power_fit(dimensions, popt[0], 1, popt[2])

    ys = [times, sqrt_N_fit, N_three_quarters_fit, N_fit]
    
    fig, ax = plt.subplots()
    linestyles = ['solid', 'dotted', 'dotted', 'dotted']
    for i, y in enumerate(ys):
        ax.plot(dimensions, y, linestyle=linestyles[i])
    ax.legend(['time',
                '$1/N^{1/2}$',
                '$1/N^{3/4}$',
                '$1/N$'])
    ax.set(xlabel='$N$')
    ax.grid()
    if save:
        chain_tag = '_' + chain
        lat_d_tag = '_lat_dim=2' if lattice_d==2 else ''
        plt.savefig(f'plots/p4{chain_tag}/times_alpha={alpha}{lat_d_tag}{save_insert()}.png')
    plt.show()


def p5_probability_against_N_plot(dimensions, probabilities, alpha, gammaN, marked, save=False, chain='open', lattice_d=1):
    
    hundred_percent = [1 for _ in range(len(probabilities))]
    ninety_percent = [0.9 for _ in range(len(probabilities))]
    eighty_percent = [0.8 for _ in range(len(probabilities))]

    ys = [probabilities, hundred_percent, ninety_percent, eighty_percent]
    
    fig, ax = plt.subplots()
    linestyles = ['solid', 'dashed', 'dashed', 'dashed']
    for i, y in enumerate(ys):
        ax.plot(dimensions, y, linestyle=linestyles[i])
    ax.legend(['fidelity',
                '$100\%$',
                '$90\%$',
                '$80\%$'])
    ax.set(xlabel='$N$')
    ax.grid()
    if save:
        chain_tag = '_' + chain
        lat_d_tag = '_lat_dim=2' if lattice_d==2 else ''
        plt.savefig(f'plots/p5{chain_tag}/probs_alpha={alpha}{lat_d_tag}_m={marked}{save_insert()}.png')
    plt.show()


def p6_fidelity_against_marked_state(marked_states, fidelities, alpha, time, dimensions, gammaN, save=False, chain='open', lattice_d=1):
    
    hundred_percent = [1 for _ in range(len(fidelities))]
    ninety_percent = [0.9 for _ in range(len(fidelities))]
    eighty_percent = [0.8 for _ in range(len(fidelities))]

    ys = [fidelities, hundred_percent, ninety_percent, eighty_percent]
    
    fig, ax = plt.subplots()
    linestyles = ['solid', 'dashed', 'dashed', 'dashed']
    for i, y in enumerate(ys):
        ax.plot(marked_states, y, linestyle=linestyles[i])
    ax.legend(['fidelity',
                '$100\%$',
                '$90\%$',
                '$80\%$'])
    ax.set(xlabel='Marked state')
    ax.grid()
    if save:
        chain_tag = '_' + chain
        lat_d_tag = '_lat_dim=2' if lattice_d==2 else ''
        plt.savefig(f'plots/p6{chain_tag}/alpha={alpha}{lat_d_tag}_N={dimensions}_time={time}_gammaN={gammaN}{save_insert()}.png')
    plt.show()