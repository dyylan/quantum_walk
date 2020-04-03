import numpy as np
import pandas as pd
from hamiltonian import Hamiltonian


def optimum_gammaN(dimensions, start_gammaN, end_gammaN, mark, alpha, number_of_points):
    gammaNs = np.linspace(start_gammaN, end_gammaN, number_of_points)
    e1_minus_e0s = []        
    for gammaN in gammaNs:
        gamma = gammaN/dimensions
        H = Hamiltonian(dimensions, gamma, alpha, mark)
        e1_minus_e0s.append(H.energy_1 - H.energy_0)
    opt_gammaN = gammaNs[np.argmin(e1_minus_e0s)]
    return opt_gammaN


def read_optimum_gammaNs(filepath, index):
    dataframe = pd.read_csv(filepath, index_col=index)
    return dataframe[['optimum_gammaNs']]


def lookup_gamma(opt_gammaNs, N):
    if isinstance(opt_gammaNs, int):
        gamma = opt_gammaNs/N 
    else:
        gamma = opt_gammaNs.loc[N, 'optimum_gammaNs']/N
    return gamma


parameters = {
    'start_dimensions'    : 64,
    'end_dimensions'      : 1760,
    'step_dimensions'     : 32,
    'marked_state'        : 5,                     
    'alpha'               : 1,
    'start_gammaN'        : 4, 
    'end_gammaN'          : 400,
    'number_of_points'    : 100,
}


if __name__ == "__main__":
    start_N = parameters['start_dimensions']
    end_N = parameters['end_dimensions']
    step_N = parameters['step_dimensions']
    marked_state = parameters['marked_state']
    alpha = parameters['alpha']                             
    start_gammaN = parameters['start_gammaN']
    end_gammaN = parameters['end_gammaN']
    number_of_points = parameters['number_of_points'] 

    dimensions = list(range(start_N, end_N+1, step_N))

    optimum_gammaNs = []
    start_gammaNs = []
    end_gammaNs = []
    for N in dimensions:
        opt_gammaN = optimum_gammaN(N, start_gammaN, end_gammaN, marked_state, alpha, number_of_points)
        optimum_gammaNs.append(opt_gammaN)
        start_gammaNs.append(start_gammaN)
        end_gammaNs.append(end_gammaN)
        print(f'Computed optimum gammaN for {N} dimensions (up to {end_N})')

    optimum_gammaNs_data = {
        'dimensions'            : dimensions,
        'start_gammaNs'         : start_gammaNs,
        'end_gammaNs'           : end_gammaNs,
        'optimum_gammaNs'       : optimum_gammaNs
    }

    optimum_gammaNs_df = pd.DataFrame(data=optimum_gammaNs_data)

    optimum_gammaNs_df.to_csv(f'optimum_gamma/alpha={alpha}/optimum_gammaNs.csv', index=False)
