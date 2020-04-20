import numpy as np
import pandas as pd
from .plots import p6_fidelity_against_marked_state
from ..config import parameters
from ..quantum.hamiltonian import Hamiltonian
from ..optimise.optimum_gammaNs import check_optimum_gammaNs_parameter_type, lookup_gamma


def p6(lat_dim, dimensions, alpha, gamma, time, ring, save_plots):
    fidelities = []
    marked_states = list(range(1, dimensions+1, 1))
    for marked in marked_states:
        H = Hamiltonian(dimensions, gamma, alpha, marked, ring, lat_dim)
        state, _ = H.unitary_evolution(time)
        marked_amplitude = np.vdot(H.m_ket, state)
        fidelity = np.abs(np.multiply(np.conj(marked_amplitude), marked_amplitude))
        fidelities.append(fidelity)
        print(f'Computed fidelity of {fidelity} for marked state {marked} (out of {dimensions})')
    return fidelities, marked_states


def run():
    p6_parameters = parameters['p6']

    # Parameters
    lattice_dimension = parameters['lattice_dimension']
    ring = parameters['ring']
    alpha = parameters['alpha']
    dimensions = parameters['dimensions']
    
    time = p6_parameters['time']
    save_plots = p6_parameters['save_plots']   

    lat_d_tag = '_lat_dim=2' if lattice_dimension==2 else ''
    ring_tag = '_ring' if ring else ''
    optimum_gammaNs = f'optimum_gamma/alpha={alpha}{lat_d_tag}{ring_tag}/optimum_gammaNs.csv'
    optimum_gammaNs = check_optimum_gammaNs_parameter_type(optimum_gammaNs)

    gamma = lookup_gamma(optimum_gammaNs, dimensions)
    gammaN = gamma * dimensions 

    fidelities, marked_states = p6(lattice_dimension, dimensions, alpha, gamma, time, ring, save_plots)

    p6_fidelity_against_marked_state(marked_states, fidelities, alpha, time, dimensions, gammaN, save_plots, ring, lattice_dimension)

