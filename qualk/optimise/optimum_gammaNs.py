import numpy as np
import pandas as pd
from ..quantum.hamiltonian import Hamiltonian


parameters = {
    'chain'               : 'ring',
    'lattice_dimensions'  : 1,
    'start_dimensions'    : 64,
    'end_dimensions'      : 1024,
    'step_dimensions'     : 32,
    'marked_state'        : 5,
    'alpha'               : 1.4,
    'start_gammaN'        : 10,
    'end_gammaN'          : 210,
    'number_of_points'    : 20
}


def optimum_gammaN(lattice_d, chain, dimensions, start_gammaN, end_gammaN, mark, alpha, number_of_points):
    gammaNs = np.linspace(start_gammaN, end_gammaN, number_of_points)
    e1_minus_e0s = []        
    for gammaN in gammaNs:
        gamma = gammaN/dimensions
        H = Hamiltonian(dimensions, gamma, alpha, mark, chain, lattice_d)
        e1_minus_e0s.append(H.energy_1 - H.energy_0)
    opt_gammaN = gammaNs[np.argmin(e1_minus_e0s)]
    return opt_gammaN


def read_optimum_gammaNs(filepath, index):
    dataframe = pd.read_csv(filepath, index_col=index)
    return dataframe[['optimum_gammaNs']]


def check_optimum_gammaNs_parameter_type(optimum_gammaNs):
    if isinstance(optimum_gammaNs, str):
        opt = read_optimum_gammaNs(optimum_gammaNs, 'dimensions')
    else:
        opt = float(optimum_gammaNs)
    return opt


def lookup_gamma(opt_gammaNs, N):
    if isinstance(opt_gammaNs, float):
        gamma = opt_gammaNs/N 
    else:
        gamma = opt_gammaNs.loc[N, 'optimum_gammaNs']/N
    return gamma


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
    start_gammaN = parameters['start_gammaN']
    end_gammaN = parameters['end_gammaN']
    number_of_points = parameters['number_of_points'] 

    if lattice_d == 1:
        dimensions = list(range(start_N, end_N+1, step_N))
    elif lattice_d == 2:
        if is_square(start_N) and is_square(end_N):
            dimensions = [x**2 for x in range(int(np.sqrt(start_N)), int(np.sqrt(end_N))+1, 1)]
        else:
            raise ValueError('Start dimensions and end dimensions must be '
                             'square numbers for lattice dimension of 2.') 

    optimum_gammaNs = []
    start_gammaNs = []
    end_gammaNs = []
    for N in dimensions:
        opt_gammaN = optimum_gammaN(lattice_d, chain, N, start_gammaN, end_gammaN, marked_state, alpha, number_of_points)
        optimum_gammaNs.append(opt_gammaN)
        start_gammaNs.append(start_gammaN)
        end_gammaNs.append(end_gammaN)
        print(f'Computed optimum gammaN for {N} dimensions (up to {end_N}) - lattice dimension {lattice_d}')

    optimum_gammaNs_data = {
        'dimensions'            : dimensions,
        'start_gammaNs'         : start_gammaNs,
        'end_gammaNs'           : end_gammaNs,
        'optimum_gammaNs'       : optimum_gammaNs
    }

    optimum_gammaNs_df = pd.DataFrame(data=optimum_gammaNs_data)

    chain_tag = '_' + chain
    marked_state_tag = f'_m={marked_state}' if not chain else ''

    if lattice_d == 1:
        optimum_gammaNs_df.to_csv(f'optimum_gamma/alpha={alpha}{chain_tag}/optimum_gammaNs{marked_state_tag}.csv', index=False)
    elif lattice_d == 2:
        if chain == 'open':
            optimum_gammaNs_df.to_csv(f'optimum_gamma/alpha={alpha}_lat_dim=2/optimum_gammaNs{marked_state_tag}.csv', index=False)
        else:
            raise ValueError('Ring for lattice dimension 2 is not implemented yet.')
