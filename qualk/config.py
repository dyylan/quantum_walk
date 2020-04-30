import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


optimum_gammaN = {
    1 : {
        0   : 1.0,
        1   : 69.40946158836066,  # for 1024 dimensions with ring
        1.1 : 94.94949494949493,  # for 1024 dimensions with ring
        1.2 : 125.42929292929294, # for 1024 dimensions with ring
        1.3 : 161.3036616161616,  # for 1024 dimensions with ring
        1.4 : 203.66560340244558, # for 1024 dimensions with ring
        1.5 : 254.87956487956495, # for 1024 dimensions with ring
        1.6 : 319.26262626262627, # for 1024 dimensions with ring
        1.7 : None,
        1.8 : 515.0, # for 1024 dimensions with ring
        1.9 : None, 
        2   : 876.7876438806672, # for 1024 dimensions with ring
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
    'show_plots'                : False,
    'chain'                     : chain_form[2],
    'alpha'                     : alpha,
    'kappa'                     : 0.5,
    'dimensions'                : 1024, # this is the dimensions of the Hamiltonian
    'lattice_dimension'         : lat_d, # this is the physical lattice dimensions
    'marked_state'              : 5,
    'save_tag'                  : '',#'anti_s_init', # Adds an additional message to the saved plot filename
    'init_state'                : 'anti_s', # States: 'm', 'a', 's', 'sq', 'b'
    'use_init_state'            : False,        
    'noise'                     : 0,  # Simple decoherence procedure
    'samples'                   : 1,  # Number of samples for the noise calculation
    'p1'                        : {
        'start_gammaN'              : 1, 
        'end_gammaN'                : 400,
        'number_of_points'          : 50,
        'save_plots'                : True,
    },

    'p2'                        : {
        'end_time'                  : 150,
        'time_step'                 : 1,
        'optimum_gammaN'            : optimum_gammaN[lat_d][alpha],
        'save_plots'                : True,

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
        'end_dimensions'            : 1024,
        'step_dimensions'           : 32,
        'end_time'                  : 160, # For ring the timestep can be less
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
        'time'                      : 25.0,
        'save_plots'                : True         
    }
}


def update_parameter(parameter_tuple, px=''):
    key = parameter_tuple[0]
    value = parameter_tuple[1]
    if px:
        parameters[px][key] = value
        print(f'Updated {key} to {value} in {px}')
    else:
        parameters[key] = value
        print(f'Updated {key} to {value}')
    

def update_alpha(new_alpha):
    alpha = new_alpha