import matplotlib.pyplot as plt 
import numpy as np


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
    norm_overlaps = np.multiply(np.conj(overlaps), overlaps)
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