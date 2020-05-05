import numpy as np
import pandas as pd
from .plots import p3_min_gap_against_N_plot, save_insert, noise_insert
from ..config import parameters
from ..quantum.hamiltonian import Hamiltonian
from ..optimise.optimum_gammaNs import read_optimum_gammaNs, lookup_gamma, check_optimum_gammaNs_parameter_type
 

def p3(start_N, end_N, opt_gammaNs, alpha, marked, chain, lat_d, step_N=1):
    noise = parameters['noise']
    samples = parameters['samples']
    dimensions = list(range(start_N, end_N+1, step_N))
    min_gaps = []
    for N in dimensions:
        gamma = lookup_gamma(opt_gammaNs, N)
        H = Hamiltonian(N, gamma, alpha, marked, chain, lat_d, noise, samples)
        min_gap = (H.energy_1 - H.energy_0)
        min_gaps.append(min_gap)
        print(f'Computed minimum gap for {N} dimensions (up to {end_N}) '
              f'with gammaN = {gamma*N}')
    return dimensions, min_gaps


def run():
    p3_parameters = parameters['p3']

    # Parameters
    chain = parameters['chain']
    lattice_dimension = parameters['lattice_dimension']
    marked_state = parameters['marked_state']
    alpha = parameters['alpha']
    
    start_N = p3_parameters['start_dimensions']
    end_N = p3_parameters['end_dimensions']
    step_N = p3_parameters['step_dimensions']
    save_plots = p3_parameters['save_plots'] 
    
    lat_d_tag = '_lat_dim=2' if lattice_dimension==2 else ''
    chain_tag = '_' + chain
    optimum_gammaNs = f'optimum_gamma/alpha={alpha}{lat_d_tag}{chain_tag}/optimum_gammaNs.csv'
    optimum_gammaNs = check_optimum_gammaNs_parameter_type(optimum_gammaNs)

    # Minimum gaps against dimensions
    dimensions, min_gaps = p3(start_N, end_N, optimum_gammaNs, alpha, marked_state, chain, lattice_dimension, step_N)

    # Plot
    p3_min_gap_against_N_plot(dimensions, min_gaps, alpha, optimum_gammaNs, save_plots, chain)

    # CSV
    if save_plots:
        p3_data = {
            'dimensions'                : dimensions,
            'min_gaps'                  : np.real(min_gaps)
        }
        p3_df = pd.DataFrame(data=p3_data)
        
        p3_df.to_csv(f'data/p3_{chain}/alpha={alpha}_lat_dim={lattice_dimension}{save_insert()}{noise_insert()}.csv', index=False)