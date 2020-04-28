import numpy as np
import pandas as pd
from .plots import p2_overlaps_plot, save_insert, noise_insert
from ..config import parameters
from ..quantum.hamiltonian import Hamiltonian
from ..quantum.ket import Ket


def p2(dimensions, gamma, alpha, marked, end_time, time_step, chain, lat_dim, print_status=False):
    noise = parameters['noise']
    samples = parameters['samples']
    H = Hamiltonian(dimensions, gamma, alpha, marked, chain, lat_dim, noise, samples)
    use_init_state = parameters['use_init_state']
    init_state = parameters['init_state']
    initial_state = init_state if use_init_state else 's'
    states, times = H.unitary_evolution(end_time, dt=time_step, print_status=print_status, initial_state=initial_state)
    overlaps = [np.vdot(H.m_ket, state) for state in states]
    return times, overlaps


def run():
    p2_parameters = parameters['p2']

    # Parameters
    chain = parameters['chain']
    alpha = parameters['alpha']     
    dimensions = parameters['dimensions']
    marked_state = parameters['marked_state']
    lattice_dimension = parameters['lattice_dimension']

    optimum_gammaN = p2_parameters['optimum_gammaN']
    end_time = p2_parameters['end_time'] 
    time_step = p2_parameters['time_step'] 
    save_plots = p2_parameters['save_plots'] 

    gamma = optimum_gammaN/dimensions

    # State probability over time
    times, overlaps = p2(dimensions, gamma, alpha, marked_state, end_time, time_step, chain, lattice_dimension, True)

    # Plot
    p2_overlaps_plot(times, overlaps, alpha, optimum_gammaN, dimensions, marked_state, save_plots, chain, lattice_dimension)

    # CSV
    if save_plots:
        norm_overlaps = np.abs(np.multiply(np.conj(overlaps), overlaps))
        real_overlaps = np.real(overlaps)
        imag_overlaps = np.imag(overlaps)
        p2_data = {
            'times'                 : times,
            'norm_overlaps'         : norm_overlaps,
            'real_overlaps'         : real_overlaps,
            'imag_overlaps'         : imag_overlaps
        }
        p2_df = pd.DataFrame(data=p2_data)
        
        p2_df.to_csv(f'data/p2_{chain}/alpha={alpha}{save_insert()}{noise_insert()}_lat_dim={lattice_dimension}_dim={dimensions}.csv', index=False)

