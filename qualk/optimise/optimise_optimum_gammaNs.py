import numpy as np
import pandas as pd
from .optimum_gammaNs import check_optimum_gammaNs_parameter_type, lookup_gamma, optimum_gammaN
from ..quantum.hamiltonian import Hamiltonian


parameters = {
    'chain'               : 'ring',
    'lattice_dimensions'  : 1,
    'start_dimensions'    : 64,
    'end_dimensions'      : 1760,
    'step_dimensions'     : 32,
    'marked_state'        : 50,                     
    'alpha'               : 1,
    'gammaN_range'        : 1,
    'number_of_points'    : 100,
}


def optimise():
    chain = parameters['chain']
    lattice_d = parameters['lattice_dimensions']
    start_N = parameters['start_dimensions']
    end_N = parameters['end_dimensions']
    step_N = parameters['step_dimensions']
    marked_state = parameters['marked_state']
    alpha = parameters['alpha']                             
    gammaN_range = parameters['gammaN_range']
    number_of_points = parameters['number_of_points']

    chain_tag = '_' + chain
    lat_dim_tag = '_lat_dim' if lattice_d == 2 else ''
    centre_gammaNs_csv = f'optimum_gamma/alpha={alpha}{chain_tag}{lat_dim_tag}/optimum_gammaNs.csv'
    centre_gammaNs = check_optimum_gammaNs_parameter_type(centre_gammaNs_csv)
    
    dimensions = list(range(start_N, end_N+1, step_N))

    optimum_gammaNs = []
    start_gammaNs = []
    end_gammaNs = []
    for N in dimensions:
        centre_gammaN = lookup_gamma(centre_gammaNs, N) * N
        start_gammaN = centre_gammaN - (gammaN_range/2)
        end_gammaN = centre_gammaN + (gammaN_range/2)
        opt_gammaN = optimum_gammaN(lattice_d, chain, N, start_gammaN, end_gammaN, marked_state, alpha, number_of_points)
        optimum_gammaNs.append(opt_gammaN)
        start_gammaNs.append(start_gammaN)
        end_gammaNs.append(end_gammaN)
        print(f'--> Computed optimum gammaN of {opt_gammaN} for {N} dimensions (up to {end_N})'
              f'\n\t\twith start_gammaN = {start_gammaN} and end_gammaN = {end_gammaN}')

    optimum_gammaNs_data = {
        'dimensions'            : dimensions,
        'start_gammaNs'         : start_gammaNs,
        'end_gammaNs'           : end_gammaNs,
        'optimum_gammaNs'       : optimum_gammaNs
    }

    optimum_gammaNs_df = pd.DataFrame(data=optimum_gammaNs_data)

    if lattice_d == 1:
        optimum_gammaNs_df.to_csv(f'optimum_gamma/alpha={alpha}{chain_tag}/optimised_optimum_gammaNs.csv', index=False)
    elif lattice_d == 2:
        if chain == 'open':
            optimum_gammaNs_df.to_csv(f'optimum_gamma/alpha={alpha}_lat_dim=2/optimised_optimum_gammaNs.csv', index=False)
        else:
            raise ValueError('Ring for lattice dimension 2 is not implemented yet.')