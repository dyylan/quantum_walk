import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


optimum_gammaN = {
    1 : {
        0   : 1.0,
        1   : 69.40946158836066,  # for 1024 dimensions with Ring
        2   : None,
        3   : 1374.966 # for 256 dimensions with Ring 
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
    'chain'                     : chain_form[3],
    'alpha'                     : alpha,
    'dimensions'                : 512, # this is the dimensions of the Hamiltonian
    'lattice_dimension'         : lat_d, # this is the physical lattice dimensions
    'marked_state'              : 5,
    'save_tag'                  : '', # Adds an additional message to the saved plot filename
    'init_state'                : 'm', # States: 'm', 'a', 's', 'sq', 'b'
    'use_init_state'            : False,

    'p1'                        : {
        'start_gammaN'              : 1, 
        'end_gammaN'                : 100,
        'number_of_points'          : 50,
        'save_plots'                : True
    },

    'p2'                        : {
        'end_time'                  : 400,
        'time_step'                 : 1,
        'optimum_gammaN'            : optimum_gammaN[lat_d][alpha],
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
        'end_time'                  : 95, # For ring the timestep can be less
        'time_step'                 : 1,
        'save_plots'                : True
    },

    'p5'                        : {
        'start_dimensions'          : 64,
        'end_dimensions'            : 1760,
        'step_dimensions'           : 32,
        'end_time'                  : 95, # For ring the timestep can be less
        'time_step'                 : 1,
        'save_plots'                : True
    },

    'p6'                        : {
        'time'                      : 43.0,
        'save_plots'                : True         
    }
}