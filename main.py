import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


alpha = 1
dimensions = 1024
marked_state = 5
optimum_gammaN = {
    0   : 1,
    1   : 79.77889447236181
}


p1_parameters = {
    'dimensions'          : dimensions,
    'marked_state'        : marked_state,                     
    'start_gammaN'        : 0.1, 
    'end_gammaN'          : 180,
    'alpha'               : alpha,
    'number_of_points'    : 200,
    'save_plots'          : True
}


p2_parameters = {
    'dimensions'          : dimensions,
    'marked_state'        : marked_state,
    'alpha'               : alpha,
    'end_time'            : 200,
    'time_step'           : 10,
    'optimum_gammaN'      : optimum_gammaN[alpha],
    'save_plots'          : False
}