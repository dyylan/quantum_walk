import numpy as np
import pandas as pd
from .plots import p3_min_gap_against_N_plot
from ..config import p3_parameters
from ..quantum.hamiltonian import Hamiltonian
from ..optimise.optimum_gammaNs import read_optimum_gammaNs, lookup_gamma, check_optimum_gammaNs_parameter_type
 

def p3(start_N, end_N, opt_gammaNs, alpha, marked, step_N=1):
    dimensions = list(range(start_N, end_N+1, step_N))
    min_gaps = []
    for N in dimensions:
        gamma = lookup_gamma(opt_gammaNs, N)
        H = Hamiltonian(N, gamma, alpha, marked)
        min_gap = (H.energy_1 - H.energy_0)
        min_gaps.append(min_gap)
        print(f'Computed minimum gap for {N} dimensions (up to {end_N}) '
              f'with gammaN = {gamma*N}')
    return dimensions, min_gaps


def run():
    # Parameters
    start_N = p3_parameters['start_dimensions']
    end_N = p3_parameters['end_dimensions']
    step_N = p3_parameters['step_dimensions']
    marked_state = p3_parameters['marked_state']
    alpha = p3_parameters['alpha']                             
    optimum_gammaNs = p3_parameters['optimum_gammaNs']
    save_plots = p3_parameters['save_plots'] 

    optimum_gammaNs = check_optimum_gammaNs_parameter_type(optimum_gammaNs)

    # Minimum gaps against dimensions
    dimensions, min_gaps = p3(start_N, end_N, optimum_gammaNs, alpha, marked_state, step_N)

    # Plot
    p3_min_gap_against_N_plot(dimensions, min_gaps, alpha, optimum_gammaNs, save_plots)