import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


alpha = 0
dimensions = 64
marked_state = 5
optimum_gammaN = {
    0   : 1.0,
    1   : 79.77889447236181  # for 1024 dimensions
}


p1_parameters = {
    'dimensions'          : dimensions,
    'marked_state'        : marked_state,                     
    'alpha'               : alpha,
    'start_gammaN'        : 0.01, 
    'end_gammaN'          : 2,
    'number_of_points'    : 200,
    'save_plots'          : False
}


p2_parameters = {
    'dimensions'          : dimensions,
    'marked_state'        : marked_state,
    'alpha'               : alpha,
    'end_time'            : 200,
    'time_step'           : 1,
    'optimum_gammaN'      : optimum_gammaN[alpha],
    'save_plots'          : False
}


p3_parameters = {
    'marked_state'        : marked_state,
    'alpha'               : alpha,
    'start_dimensions'    : 64,
    'end_dimensions'      : 1760,
    'step_dimensions'     : 32,
    # For optimum_gammaNs can put a single number (eg. 1.0) or a file path to optimum_gammaNs CSV.
    'optimum_gammaNs'     : 1.0, #f'optimum_gamma/alpha={alpha}/optimum_gammaNs.csv',
    'save_plots'          : True
}


p4_parameters = {
    'marked_state'        : marked_state,
    'alpha'               : alpha,
    'start_dimensions'    : 64,
    'end_dimensions'      : 1760,
    'step_dimensions'     : 32,
    'end_time'            : 200,
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
    'end_time'            : 200,
    'time_step'           : 1,
    # For optimum_gammaNs can put a single number (eg. 1.0) or a file path to optimum_gammaNs CSV.
    'optimum_gammaNs'     : 1.0, #f'optimum_gamma/alpha={alpha}/optimum_gammaNs.csv',
    'save_plots'          : True
}