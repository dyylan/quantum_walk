import numpy as np
from .plots import p2_overlaps_plot
from ..config import p2_parameters, lattice_dimension, init_state, use_init_state
from ..quantum.hamiltonian import Hamiltonian
from ..quantum.ket import Ket


def p2(dimensions, gamma, alpha, marked, end_time, time_step, print_status=False):
    H = Hamiltonian(dimensions, gamma, alpha, marked, lattice_dimension)
    initial_state = init_state if use_init_state else 's'
    states, times = H.unitary_evolution(end_time, dt=time_step, print_status=print_status, initial_state=initial_state)
    overlaps = [np.vdot(H.m_ket, state) for state in states]
    return times, overlaps


def run():
    # Parameters
    dimensions = p2_parameters['dimensions']
    marked_state = p2_parameters['marked_state']
    alpha = p2_parameters['alpha']                             
    optimum_gammaN = p2_parameters['optimum_gammaN']
    end_time = p2_parameters['end_time'] 
    time_step = p2_parameters['time_step'] 
    save_plots = p2_parameters['save_plots'] 

    gamma = optimum_gammaN/dimensions

    # State probability over time
    times, overlaps = p2(dimensions, gamma, alpha, marked_state, end_time, time_step, True)

    # Plot
    p2_overlaps_plot(times, overlaps, alpha, optimum_gammaN, dimensions, marked_state, save_plots, lattice_dimension)
