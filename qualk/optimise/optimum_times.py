import numpy as np
import pandas as pd
from scipy.signal import find_peaks 
from .optimum_gammaNs import check_optimum_gammaNs_parameter_type, lookup_gamma
from ..quantum.hamiltonian import Hamiltonian


parameters = {
    'chain'               : 'ring',
    'lattice_dimensions'  : 1,
    'start_dimensions'    : 3,
    'end_dimensions'      : 10,
    'step_dimensions'     : 1,
    'marked_state'        : 1,                     
    'alpha'               : 1,
    'start_time'          : 1, 
    'end_time'            : 200,
    'number_of_points'    : 200,
}


def optimum_time(lattice_d, chain, dimensions, gamma, start_time, end_time, mark, alpha, number_of_points):
    H = Hamiltonian(dimensions, gamma, alpha, mark, chain, lattice_d)
    times = np.linspace(start_time, end_time, number_of_points)
    fidelities = []        
    for time in times:
        state, _ = H.unitary_evolution(time)
        marked_amplitude = np.vdot(H.m_ket, state)
        fidelity = np.abs(np.multiply(np.conj(marked_amplitude), marked_amplitude))
        fidelities.append(fidelity)
    peaks, _ = find_peaks(fidelities, height=(0.5, 1.05))
    optimum_time = times[peaks[0]]
    max_fidelity = fidelities[peaks[0]]
    return optimum_time, max_fidelity


def read_optimum_times(filepath, index):
    dataframe = pd.read_csv(filepath, index_col=index)
    return dataframe[['optimum_times']]


def check_optimum_times_parameter_type(optimum_times):
    if isinstance(optimum_times, str):
        opt = read_optimum_times(optimum_times, 'dimensions')
    else:
        opt = float(optimum_times)
    return opt


def lookup_time(optimum_times, N):
    if isinstance(optimum_times, float):
        time = optimum_times/N 
    else:
        time = optimum_times.loc[N, 'optimum_times']/N
    return time


def is_square(integer):
    root = np.sqrt(integer)
    return integer == int(root + 0.5) ** 2


def optimise():
    chain = parameters['chain']
    lattice_d = parameters['lattice_dimensions']
    start_N = parameters['start_dimensions']
    end_N = parameters['end_dimensions']
    step_N = parameters['step_dimensions']
    marked_state = parameters['marked_state']
    alpha = parameters['alpha']                             
    start_time = parameters['start_time']
    end_time = parameters['end_time']
    number_of_points = parameters['number_of_points'] 

    chain_tag = '_' + chain
    optimum_gammaNs_file = f'optimum_gamma/alpha={alpha}{chain_tag}/optimum_gammaNs.csv'
    
    optimum_gammaNs = check_optimum_gammaNs_parameter_type(optimum_gammaNs_file)
    
    if lattice_d == 1:
        dimensions = list(range(start_N, end_N+1, step_N))
    elif lattice_d == 2:
        if is_square(start_N) and is_square(end_N):
            dimensions = [x**2 for x in range(int(np.sqrt(start_N)), int(np.sqrt(end_N))+1, 1)]
        else:
            raise ValueError('Start dimensions and end dimensions must be '
                             'square numbers for lattice dimension of 2.') 

    optimum_times = []
    start_times = []
    end_times = []
    max_fidelities = []
    for N in dimensions:
        gamma = lookup_gamma(optimum_gammaNs, N)
        opt_time, max_fidelity = optimum_time(lattice_d, chain, N, gamma, start_time, end_time, marked_state, alpha, number_of_points)
        optimum_times.append(opt_time)
        max_fidelities.append(max_fidelity)
        start_times.append(start_time)
        end_times.append(end_time)
        print(f'Computed optimum time of {opt_time} for {N} dimensions (up to {end_N}) - lattice dimension {lattice_d}')

    optimum_times_data = {
        'dimensions'            : dimensions,
        'start_time'            : start_times,
        'end_time'              : end_times,
        'max_fidelity'          : max_fidelities,
        'optimum_times'         : optimum_times
    }

    optimum_times_df = pd.DataFrame(data=optimum_times_data)

    if lattice_d == 1:
        optimum_times_df.to_csv(f'optimum_time/alpha={alpha}{chain_tag}/optimum_times_m={marked_state}.csv', index=False)
    elif lattice_d == 2:
        if chain == 'open':
            optimum_times_df.to_csv(f'optimum_time/alpha={alpha}_lat_dim=2/optimum_times_m={marked_state}.csv', index=False)
        else:
            raise ValueError('Ring for lattice dimension 2 is not implemented yet.')