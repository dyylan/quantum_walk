import numpy as np
import pandas as pd
from hamiltonian import Hamiltonian
from optimum_gammaNs import lookup_gamma, optimum_gammaN, read_optimum_gammaNs


parameters = {
    'start_dimensions'    : 64,
    'end_dimensions'      : 1760,
    'step_dimensions'     : 32,
    'marked_state'        : 5,                     
    'alpha'               : 1,
    'gammaN_range'        : 1, 
    'number_of_points'    : 100,
}


if __name__ == "__main__":
    start_N = parameters['start_dimensions']
    end_N = parameters['end_dimensions']
    step_N = parameters['step_dimensions']
    marked_state = parameters['marked_state']
    alpha = parameters['alpha']                             
    gammaN_range = parameters['gammaN_range']
    number_of_points = parameters['number_of_points'] 

    dimensions = list(range(start_N, end_N+1, step_N))

    optimum_gammaNs = []
    start_gammaNs = []
    end_gammaNs = []
    for N in dimensions:
        gammaN = lookup_gamma(opt_gammaNs, N) * N
        start_gammaN = gammaN - (gammaN_range/2)
        end_gammaN = gammaN + (gammaN_range/2)
        opt_gammaN = optimum_gammaN(N, start_gammaN, end_gammaN, marked_state, alpha, number_of_points)
        optimum_gammaNs.append(opt_gammaN)
        start_gammaNs.append(start_gammaN)
        end_gammaNs.append(end_gammaN)
        print(f'Computed optimum gammaN of {opt_gammaN} for {N} dimensions (up to {end_N}) '
              f'with start_gammaN = {start_gammaN} and end_gammaN = {end_gammaN}')

    optimum_gammaNs_data = {
        'dimensions'            : dimensions,
        'start_gammaNs'         : start_gammaNs,
        'end_gammaNs'           : end_gammaNs,
        'optimum_gammaNs'       : optimum_gammaNs
    }

    optimum_gammaNs_df = pd.DataFrame(data=optimum_gammaNs_data)

    optimum_gammaNs_df.to_csv(f'optimum_gamma/alpha={alpha}/optimised_optimum_gammaNs.csv', index=False)
