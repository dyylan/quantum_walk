import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from .p2_marked_state_probability_against_time import p2
from .plots import p5_probability_against_N_plot
from ..config import parameters
from ..optimise.optimum_gammaNs import read_optimum_gammaNs, lookup_gamma, check_optimum_gammaNs_parameter_type


def p5(start_N, end_N, end_time, time_step, opt_gammaNs, alpha, marked, chain, lat_dim, step_N=1):
    dimensions = list(range(start_N, end_N+1, step_N))
    max_probs = []
    for N in dimensions:
        gamma = lookup_gamma(opt_gammaNs, N)
        _, marked_amplitude = p2(N, gamma, alpha, marked, end_time, time_step, chain, lat_dim)
        marked_probability = np.abs(np.multiply(np.conj(marked_amplitude), marked_amplitude))
        peaks, _ = find_peaks(marked_probability, height=(0.5, 1.05))
        max_prob = marked_probability[peaks[0]]
        max_probs.append(max_prob)
        print(f'Computed max probability of {max_prob} for {N} dimensions (up to {end_N}) '
              f'with gammaN = {gamma*N}')
    return dimensions, max_probs


def run():    
    p5_parameters = parameters['p5']

    # Parameters
    lattice_dimension = parameters['lattice_dimension']
    chain = parameters['chain']
    marked_state = parameters['marked_state']
    alpha = parameters['alpha'] 

    start_N = p5_parameters['start_dimensions']
    end_N = p5_parameters['end_dimensions']
    step_N = p5_parameters['step_dimensions']
    end_time = p5_parameters['end_time'] 
    time_step = p5_parameters['time_step'] 
    save_plots = p5_parameters['save_plots']

    lat_d_tag = '_lat_dim=2' if lattice_dimension==2 else ''
    chain_tag = '_' + chain
    optimum_gammaNs = f'optimum_gamma/alpha={alpha}{lat_d_tag}{chain_tag}/optimum_gammaNs.csv'
    optimum_gammaNs = check_optimum_gammaNs_parameter_type(optimum_gammaNs)

    # Minimum gaps against dimensions
    dimensions, max_probs = p5(start_N, end_N, end_time, time_step, optimum_gammaNs, alpha, marked_state, chain, lattice_dimension, step_N)

    p5_probability_against_N_plot(dimensions, max_probs, alpha, optimum_gammaNs, marked_state, save_plots, chain, lattice_dimension)