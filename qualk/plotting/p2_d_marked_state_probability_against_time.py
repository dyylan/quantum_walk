import numpy as np
import pandas as pd
from .plots import p2_d_overlaps_plot, save_insert
from ..config import parameters
from ..quantum.hamiltonian import Hamiltonian
from ..quantum.ket import Ket
from ..quantum.density_matrix import Rho


def p2_d(dimensions, gamma, alpha, marked, kappa, end_time, time_step, grain, chain, lat_dim, print_status=False):

    H = Hamiltonian(dimensions, gamma, alpha, marked, chain, lat_dim)
    H.full_hamiltonian()
    rho = Rho(dimensions,H)
    states, times = rho.time_evolution(kappa, end_time, grain, dt=time_step, print_status=print_status)
    overlaps = [np.inner(H._m_ket.ket,np.matmul(state,H._m_ket.ket)) for state in states]
    return times, overlaps


def run():
    p2_d_parameters = parameters['p2_d']

    # Parameters
    chain = parameters['chain']
    alpha = parameters['alpha']     
    dimensions = parameters['dimensions']
    marked_state = parameters['marked_state']
    lattice_dimension = parameters['lattice_dimension']
    kappa = parameters['kappa']

    optimum_gammaN = p2_d_parameters['optimum_gammaN']
    end_time = p2_d_parameters['end_time'] 
    time_step = p2_d_parameters['time_step'] 
    grain = p2_d_parameters['grain']
    save_plots = p2_d_parameters['save_plots'] 

    gamma = optimum_gammaN/dimensions

    # State probability over time
    times, overlaps = p2_d(dimensions, gamma, alpha, marked_state, kappa, end_time, time_step, grain, chain, lattice_dimension, True)

    # Plot
    p2_d_overlaps_plot(times, overlaps, alpha, optimum_gammaN, dimensions, marked_state, kappa, save_plots, chain, lattice_dimension)

    # CSV
    if save_plots:
        p2_data = {
            'times'                 : times,
            'overlaps'              : np.real(overlaps)
        }
        p2_df = pd.DataFrame(data=p2_data)
        
        p2_df.to_csv(f'data/p2_d_{chain}/alpha={alpha}{save_insert()}_lat_dim={lattice_dimension}_dim={dimensions}.csv', index=False)