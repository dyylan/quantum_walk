# Spatial search by quantum walk
## File naming convention
The Hamiltonian and Kets classes are located in `hamiltonian.py` and `ket.py`
respectively. It is not necessarily to change these. They have not been 
documented yet, however, they are reasonably self-explanatory.

The files beginning with the prefix `p + *number*` are the plot-generating 
scripts. These also do not need to be altered. 

The file `main.py` contains the parameters used in the scripts. 

`plots.py` contains the plotting functions used by the scripts. The plots are 
saved to the `/plots` subdirectory named for the prefix of the plot-generating 
script that produced it.

## Make a new plot
Change the parameters for a specific plot in `main.py`. The global variables 
`alpha`, `dimensions`, and `marked_state` are defined at the top of the script. 
Additional parameters for the specific plotting scripts can be changed in the 
parameters dictionaries that are prefixed by the corresponding plot number. 

Then just run the plotting script, for example:
```
python p2_marked_state_probability_against_time.py
```
