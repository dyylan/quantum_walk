import numpy as np
from main import parameters
from plots import overlaps_plot
from hamiltonian import Hamiltonian


def main(dimensions, gamma, alpha, marked, end_time, time_step):
    H = Hamiltonian(dimensions, gamma, alpha, marked)
    states, times = H.unitary_evolution(end_time, time_step)
    overlaps = [np.vdot(H.m_ket, state) for state in states]
    return times, overlaps


if __name__ == "__main__":
    dimensions = parameters['dimensions']
    marked_state = parameters['marked_state']
    alpha = parameters['alpha']                                            
    optimum_gammaN = parameters['optimum_gammaN']
    gamma = optimum_gammaN/dimensions
    end_time = parameters['end_time'] 
    time_step = parameters['time_step'] 
    save_plots = parameters['save_plots'] 

    times, overlaps = main(dimensions, gamma, alpha, marked_state, end_time, time_step)

    overlaps_plot(times, overlaps, alpha, optimum_gammaN, dimensions, save_plots)
