import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


optimum_gammaN = {
    1 : {
        0   : 1.0,
        1   : 111.11894171068481,  # for 1760 dimensions with Ring
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
    'ring'                      : False,
    'alpha'                     : alpha,
    'kappa'                     : 0,
    'dimensions'                : 3, # this is the dimensions of the Hamiltonian
    'lattice_dimension'         : lat_d, # this is the physical lattice dimensions
    'marked_state'              : 1,
    'save_tag'                  : '', # Adds an additional message to the saved plot filename
    'init_state'                : '', # TODO: implement for all states: 'm', 'a', 's', 'sq', 'b'
    'use_init_state'            : False,

    'p1'                        : {
        'start_gammaN'              : 1, 
        'end_gammaN'                : 150,
        'number_of_points'          : 150,
        'save_plots'                : True
    },

    'p2'                        : {
        'end_time'                  : 200,
        'time_step'                 : 1,
        'optimum_gammaN'            : optimum_gammaN[lat_d][alpha],
        'save_plots'                : True
    },

    'p2_d'                      : {
        'end_time'                  : 50,
        'time_step'                 : 0.5,
        'grain'                     : 100,
        'optimum_gammaN'            : 1,
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