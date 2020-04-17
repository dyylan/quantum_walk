import numpy as np
from .plots import p1_amplitudes_plot
from ..config import parameters
from ..quantum.hamiltonian import Hamiltonian


def p1(dimensions, mark, start_gamma, end_gamma, alpha, ring, number_of_points):
    gammas = np.linspace(start_gamma, end_gamma, number_of_points)
    m_psi_0s = []
    s_psi_0s = []
    m_psi_1s = []
    s_psi_1s = []
    e1_minus_e0s = []        
    for point, gamma in enumerate(gammas):
        H = Hamiltonian(dimensions, gamma, alpha, mark, ring, parameters['lattice_dimension'])
        e1_minus_e0s.append(H.energy_1 - H.energy_0)
        m_psi_0s.append(np.square(np.abs(np.vdot(H.m_ket, H.psi_0))))
        s_psi_0s.append(np.square(np.abs(np.vdot(H.m_ket, H.psi_1))))
        m_psi_1s.append(np.square(np.abs(np.vdot(H.s_ket, H.psi_0))))
        s_psi_1s.append(np.square(np.abs(np.vdot(H.s_ket, H.psi_1))))
        print(f'Finished point: {point+1}/{number_of_points} \n\t with gamma: {gamma}')
    gammasN = [gamma * dimensions for gamma in gammas]
    return gammasN, [m_psi_0s, m_psi_1s, s_psi_0s, s_psi_1s], e1_minus_e0s


def run():
    p1_parameters = parameters['p1']

    # Parameters
    ring = parameters['ring']
    alpha = parameters['alpha'] 
    dimensions = parameters['dimensions']
    marked_state = parameters['marked_state']
    
    start_gamma = p1_parameters['start_gammaN']/dimensions
    end_gamma = p1_parameters['end_gammaN']/dimensions                              
    number_of_points = p1_parameters['number_of_points'] 
    save_plots = p1_parameters['save_plots'] 

    # Eigenstate amplitudes
    gammasN, amps, e1_minus_e0s = p1(dimensions, marked_state, start_gamma, 
                                        end_gamma, alpha, ring, number_of_points)

    opt_gammaN = gammasN[np.argmin(e1_minus_e0s)]
    print(f'optimum gammaN value is {opt_gammaN}')

    # Plot
    p1_amplitudes_plot(alpha, dimensions, gammasN, amps, e1_minus_e0s, save_plots, ring, parameters['lattice_dimension'])
