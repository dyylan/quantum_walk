import numpy as np
from main import p2_parameters
from plots import overlaps_plot
from hamiltonian import Hamiltonian


def p2(dimensions, gamma, alpha, marked, end_time, time_step, print_status=False):
    H = Hamiltonian(dimensions, gamma, alpha, marked)
    states, times = H.unitary_evolution(end_time, dt=time_step, print_status=print_status)
    overlaps = [np.vdot(H.m_ket, state) for state in states]
    return times, overlaps


if __name__ == "__main__":
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
    overlaps_plot(times, overlaps, alpha, optimum_gammaN, dimensions, save_plots)
