from qualk.optimise import optimise_optimum_gammaNs, optimum_gammaNs, optimum_times
from qualk.plotting import (p1_eigenstate_amplitudes_against_gammaN, 
                            p2_marked_state_probability_against_time,
                            p3_min_gap_against_N,
                            p4_time_against_N,
                            p5_probability_against_N,
                            p6_fidelity_against_marked_state)

if __name__ == "__main__":
    p2_marked_state_probability_against_time.run()