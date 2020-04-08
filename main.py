import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


alpha = 2
dimensions = 1024 # this is the dimensions of the Hamiltonian
lattice_dimension = 2 # this is the physical lattice dimensions
marked_state = 5
optimum_gammaN = {
    0   : 1.0,
    1   : 79.77889447236181,  # for 1024 dimensions
    2   : None
}


p1_parameters = {
    'dimensions'          : dimensions,
    'marked_state'        : marked_state,                     
    'alpha'               : alpha,
    'start_gammaN'        : 1, 
    'end_gammaN'          : 150,
    'number_of_points'    : 150,
    'save_plots'          : True
}


p2_parameters = {
    'dimensions'          : dimensions,
    'marked_state'        : marked_state,
    'alpha'               : alpha,
    'end_time'            : 200,
    'time_step'           : 1,
    'optimum_gammaN'      : optimum_gammaN[alpha],
    'save_plots'          : True
}


p3_parameters = {
    'marked_state'        : marked_state,
    'alpha'               : alpha,
    'start_dimensions'    : 64,
    'end_dimensions'      : 1760,
    'step_dimensions'     : 32,
    # For optimum_gammaNs can put a single number (eg. 1.0) or a file path to optimum_gammaNs CSV.
    'optimum_gammaNs'     : f'optimum_gamma/alpha={alpha}/optimum_gammaNs.csv',
    'save_plots'          : True
}


p4_parameters = {
    'marked_state'        : marked_state,
    'alpha'               : alpha,
    'start_dimensions'    : 64,
    'end_dimensions'      : 1760,
    'step_dimensions'     : 32,
    'end_time'            : 250,
    'time_step'           : 1,
    # For optimum_gammaNs can put a single number (eg. 1.0) or a file path to optimum_gammaNs CSV.
    'optimum_gammaNs'     : f'optimum_gamma/alpha={alpha}/optimum_gammaNs.csv',
    'save_plots'          : True
}


p5_parameters = {
    'marked_state'        : marked_state,
    'alpha'               : alpha,
    'start_dimensions'    : 64,
    'end_dimensions'      : 1760,
    'step_dimensions'     : 32,
    'end_time'            : 250,
    'time_step'           : 1,
    # For optimum_gammaNs can put a single number (eg. 1.0) or a file path to optimum_gammaNs CSV.
    'optimum_gammaNs'     : f'optimum_gamma/alpha={alpha}/optimum_gammaNs.csv',
    'save_plots'          : True
}