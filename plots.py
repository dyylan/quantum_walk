import matplotlib.pyplot as plt 
import numpy as np
import fits
from scipy.optimize import curve_fit


def amplitudes_plot(alpha, dimensions, gammasN, amps, e1_minus_e0, save=False):
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
        plt.savefig(f'plots/p1/alpha={alpha}_dim={dimensions}.png')
    plt.show()


def overlaps_plot(times, overlaps, alpha, gammaN, dimensions, save=False):
    norm_overlaps = np.abs(np.multiply(np.conj(overlaps), overlaps))
    real_overlaps = np.real(overlaps)
    imag_overlaps = np.imag(overlaps)
    ys = [real_overlaps, imag_overlaps, norm_overlaps]
    fig, ax = plt.subplots()
    linestyles = ['dashed', 'dashed', 'solid']
    for i, y in enumerate(ys):
        ax.plot(times, y, linestyle=linestyles[i])
    ax.legend(['$Re(\langle m| U |s\\rangle)$',
                '$Im(\langle m| U |s\\rangle)$',
                '$|\langle m| U |s\\rangle|^2$'])
    ax.set(xlabel='$time~(s/\hbar)$')
    ax.grid() 
    if save:
        plt.savefig(f'plots/p2/overlaps_alpha={alpha}_gammaN={gammaN}_N={dimensions}.png')
    plt.show()


def p3_min_gap_against_N_plot(dimensions, min_gaps, alpha, gammaN, save=False):
    
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
    ax.legend(['$min(E_1-E_0)$',
                '$1/N^{1/2}$',
                '$1/N^{3/4}$',
                '$1/N$'])
    ax.set(xlabel='$N$')
    ax.grid() 
    if save:
        plt.savefig(f'plots/p3/min_gaps_alpha={alpha}.png')
    plt.show()


def p4_time_against_N_plot(dimensions, times, alpha, gammaN, save=False):
    
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
    ax.legend(['$time$',
                '$1/N^{1/2}$',
                '$1/N^{3/4}$',
                '$1/N$'])
    ax.set(xlabel='$N$')
    ax.grid() 
    if save:
        plt.savefig(f'plots/p4/times_alpha={alpha}.png')
    plt.show()


def p5_probability_against_N_plot(dimensions, probabilities, alpha, gammaN, save=False):
    
    hundred_percent = [1 for _ in range(len(probabilities))]
    ninety_percent = [0.9 for _ in range(len(probabilities))]
    eighty_percent = [0.8 for _ in range(len(probabilities))]

    ys = [probabilities, hundred_percent, ninety_percent, eighty_percent]
    
    fig, ax = plt.subplots()
    linestyles = ['solid', 'dashed', 'dashed', 'dashed']
    for i, y in enumerate(ys):
        ax.plot(dimensions, y, linestyle=linestyles[i])
    ax.legend(['$fidelity$',
                '$100\%$',
                '$90\%$',
                '$80\%$'])
    ax.set(xlabel='$N$')
    ax.grid() 
    if save:
        plt.savefig(f'plots/p5/times_alpha={alpha}.png')
    plt.show()