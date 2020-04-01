import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


optimum_gammaN = {
    0   : 1,
    1   : 79.74
}


parameters = {
    'dimensions'          : 1024, 
    'marked_state'        : 5,
    'start_gammaN'        : 79,
    'end_gammaN'          : 80,
    'alpha'               : 1,
    'number_of_points'    : 200,
    'end_time'            : 200,
    'time_step'           : 0.5,
    'optimum_gammaN'      : optimum_gammaN[0],
    'save_plots'          : False
}
