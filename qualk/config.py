import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt
from .quantum.ket import Ket


optimum_gammaN = {
    1 : {
        0   : 1.0,
        1   : 25.66607253438912,  # for 256 dimensions
        2   : None
    },
    2 : {
        0   : 1.0,
        1   : 7.0, # for 400 dimensions
        2   : None
    }
}

lat_d = 1
alpha = 1

parameters = {
    'ring'                      : True,
    'alpha'                     : alpha,
    'dimensions'                : 256, # this is the dimensions of the Hamiltonian
    'lattice_dimension'         : lat_d, # this is the physical lattice dimensions
    'marked_state'              : 50,
    'save_tag'                  : 'm_state', # Adds an additional message to the saved plot filename
    'init_state'                : '',#Ket(dimensions=dimensions, type='m', marked=marked_state, alpha=alpha),
    'use_init_state'            : False,

    'p1'                        : {
        'start_gammaN'              : 1, 
        'end_gammaN'                : 150,
        'number_of_points'          : 150,
        'save_plots'                : True
    },

    'p2'                        : {
        'end_time'                  : 150,
        'time_step'                 : 1,
        'optimum_gammaN'            : optimum_gammaN[lat_d][alpha],
        'save_plots'                : True
    },

    'p3'                        : {
        'start_dimensions'          : 64,
        'end_dimensions'            : 1760,
        'step_dimensions'           : 32,
        'optimum_gammaNs'           : f'optimum_gamma/alpha={alpha}/optimum_gammaNs.csv',
        'save_plots'                : True
    },

    'p4'                        : {
        'start_dimensions'          : 64,
        'end_dimensions'            : 1760,
        'step_dimensions'           : 32,
        'end_time'                  : 250,
        'time_step'                 : 1,
        'optimum_gammaNs'           : f'optimum_gamma/alpha={alpha}/optimum_gammaNs.csv',
        'save_plots'                : True
    },

    'p5'                        : {
        'start_dimensions'          : 64,
        'end_dimensions'            : 1760,
        'step_dimensions'           : 32,
        'end_time'                  : 218,
        'time_step'                 : 1,
        'optimum_gammaNs'           : f'optimum_gamma/alpha={alpha}/optimum_gammaNs.csv',
        'save_plots'                : True
    },

    'p6'                        : {
        'time'                      : 43.0,
        'optimum_gammaNs'           : f'optimum_gamma/alpha={alpha}/optimum_gammaNs.csv',
        'save_plots'                : True         
    }
}