import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


optimum_gammaN = {
    1 : {
        0   : 1.0,
        1   : 118.07575757575758,  # for 1024 dimensions with ring
        2   : 118.07575757575758, # for 1760 dimensions with chord
        3   : 1374.966 # for 256 dimensions with ring 
    },
    2 : {
        0   : 1.0,
        1   : 7.0, # for 400 dimensions
        2   : None
    }
}

chain_form = {
    1   :   'open',
    2   :   'ring',
    3   :   'chord'
}

lat_d = 1
alpha = 1

parameters = {
    'chain'                     : chain_form[1],
    'alpha'                     : alpha,
    'kappa'                     : 0.5,
    'dimensions'                : 8, # this is the dimensions of the Hamiltonian
    'lattice_dimension'         : lat_d, # this is the physical lattice dimensions
    'marked_state'              : 1,
    'save_tag'                  : '', # Adds an additional message to the saved plot filename
    'init_state'                : 'm', # States: 'm', 'a', 's', 'sq', 'b'
    'use_init_state'            : False,

    'p1'                        : {
        'start_gammaN'              : 1, 
        'end_gammaN'                : 400,
        'number_of_points'          : 50,
        'save_plots'                : True,
    },

    'p2'                        : {
        'end_time'                  : 100,
        'time_step'                 : 1,
        'optimum_gammaN'            : optimum_gammaN[lat_d][alpha],
        'save_plots'                : True
    },

    'p2_d'                      : {
        'end_time'                  : 20,
        'time_step'                 : 0.5,
        'grain'                     : 50,
        'optimum_gammaN'            : 2.1057575757575800,
        'save_plots'                : True
    },

    'p3'                        : {
        'start_dimensions'          : 64,
        'end_dimensions'            : 1760,
        'step_dimensions'           : 32,
        'save_plots'                : True
    },

    'p4'                        : {
        'start_dimensions'          : 64,
        'end_dimensions'            : 1760,
        'step_dimensions'           : 32,
        'end_time'                  : 80, # For ring the timestep can be less
        'time_step'                 : 1,
        'save_plots'                : True
    },

    'p5'                        : {
        'start_dimensions'          : 64,
        'end_dimensions'            : 1760,
        'step_dimensions'           : 32,
        'end_time'                  : 80, # For ring the timestep can be less
        'time_step'                 : 1,
        'save_plots'                : True
    },

    'p6'                        : {
        'time'                      : 43.0,
        'save_plots'                : True         
    }
}