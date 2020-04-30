from qualk.optimise import optimise_optimum_gammaNs, optimum_gammaNs, optimum_times
from qualk.plotting import (p1_eigenstate_amplitudes_against_gammaN, 
                            p2_marked_state_probability_against_time,
                            p2_d_marked_state_probability_against_time,
                            p3_min_gap_against_N,
                            p4_time_against_N,
                            p5_probability_against_N,
                            p6_fidelity_against_marked_state)


if __name__ == "__main__":
    # optimum_gammaNs.optimise()
    # goptimise_optimum_gammaNs.optimise()

    # p1_eigenstate_amplitudes_against_gammaN.run() 
     p2_marked_state_probability_against_time.run()
    # p2_d_marked_state_probability_against_time.run()
    # p3_min_gap_against_N.run()
    # p4_time_against_N.run()
    # p5_probability_against_N.run()
    # p6_fidelity_against_marked_state.run()

    # from qualk.config import update_parameter

    # update_parameter(('end_time', 200), 'p2')

    from qualk.config import update_alpha

    update_alpha(1.1)
    p2_marked_state_probability_against_time.run()
    # p4_time_against_N.run()

    update_alpha(1.2)
    p2_marked_state_probability_against_time.run()
    # p4_time_against_N.run()

    update_alpha(1.3)
    p2_marked_state_probability_against_time.run()
    # p4_time_against_N.run()

    update_alpha(1.4)
    p2_marked_state_probability_against_time.run()

    update_alpha(1.5)
    p2_marked_state_probability_against_time.run()

    update_alpha(1.6)
    p2_marked_state_probability_against_time.run()