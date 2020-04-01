import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


parameters = {
    'dimensions'          : 1024,
    'marked_state'        : 5,
    'start_gammaN'        : 1,
    'end_gammaN'          : 2,
    'alpha'               : 0,
    'number_of_points'    : 20,
    'save_plots'          : False
}


def hamiltonian_matrix(n, gamma=1, alpha=0, marked=1):
    H_matrix = -gamma*np.array([[(1/(np.abs(col-row)))**(alpha) if col != row else 1 
                                    for col in range(n)] 
                                        for row in range(n)])
    H_matrix[(marked-1, marked-1)] = H_matrix[(marked-1, marked-1)] - 1
    return H_matrix


def unitary_matrix(H_matrix, time=1):
    print(f'Computing hamiltonian at time: {time}')
    return scipy.linalg.expm(-1j*H_matrix*time)


def marked_state(n, marked=1):
    return np.array([0 if i != (marked-1) else 1 for i in range(n)])


def superposition_state(n):
    return (1/np.sqrt(n))*np.array([1 for _ in range(n)])


def sorted_eigenvectors_and_eigenvalues(hamiltonian):
    eigenvalues, eigenvectors = scipy.linalg.eig(hamiltonian)
    index = np.argsort(eigenvalues)
    eigenvalues = eigenvalues[index]
    eigenvectors = eigenvectors[:,index]
    return eigenvalues, eigenvectors


def psi_0_and_psi_1(eigenvectors):
    return eigenvectors[:,0], eigenvectors[:,1]


def energy_0_and_energy_1(eigenvalues):
    return eigenvalues[0], eigenvalues[1]


def unitary_evolution(hamiltonian, initial_state, target_state, end_time, dt):
    times = [dt*interval for interval in range(int(np.ceil(end_time/dt)))]
    overlaps = [np.vdot(target_state, 
                                np.matmul(unitary_matrix(hamiltonian, time), 
                                            initial_state))
                        for time in times]
    return times, overlaps


def eigenstate_m_and_s_overlap(s_ket, m_ket, dimensions, mark, gamma, alpha, number_of_points, start_gamma=0):
    gammas = [gamma*(i/number_of_points) for i in range(1,(number_of_points+1))]
    m_psi_0s = []
    s_psi_0s = []
    m_psi_1s = []
    s_psi_1s = []
    e1_minus_e0s = []        
    for point, gamma in enumerate(gammas):
        H = -gamma*dimensions*np.outer(s_ket, s_ket) - np.outer(m_ket, m_ket) 
        if alpha: 
            H = hamiltonian_matrix(n=dimensions, gamma=gamma, alpha=alpha, marked=mark)
        eigenvalues, eigenvectors = sorted_eigenvectors_and_eigenvalues(H)
        psi_0, psi_1 = psi_0_and_psi_1(eigenvectors)
        e0, e1 = energy_0_and_energy_1(eigenvalues)
        e1_minus_e0s.append(e1 - e0)
        m_psi_0s.append(np.square(np.abs(np.vdot(m_ket, psi_0))))
        s_psi_0s.append(np.square(np.abs(np.vdot(m_ket, psi_1))))
        m_psi_1s.append(np.square(np.abs(np.vdot(s_ket, psi_0))))
        s_psi_1s.append(np.square(np.abs(np.vdot(s_ket, psi_1))))
        print(f'Finished point: {point+1}/{number_of_points} \n\t with gamma: {gamma}')
    gammasN = [gamma * dimensions for gamma in gammas]
    return gammasN, [m_psi_0s, m_psi_1s, s_psi_0s, s_psi_1s], e1_minus_e0s


def amplitudes_plot(alpha, dimensions, gammasN, amps, e1_minus_e0, save=False):
    fig, ax = plt.subplots()
    linestyles = ['solid', 'solid', 'dashed', 'dashed']
    for i, amp in enumerate(amps):
        ax.plot(gammasN, amp, linestyle=linestyles[i])
    ax.plot(gammasN, e1_minus_e0)
    ax.legend(['$|\langle m|\psi_0 \\rangle |^2$', 
                '$|\langle m|\psi_1 \\rangle |^2$', 
                '$|\langle s|\psi_0 \\rangle |^2$', 
                '$|\langle s|\psi_1 \\rangle|^2$',
                '$E_1 - E_0$'])
    ax.set(xlabel='$\gamma  N$')
    ax.grid()
    if save: 
        plt.savefig(f'plots/amplitudes/alpha={alpha}_dim={dimensions}.png')
    plt.show()


def overlaps_plot(times, overlaps, alpha, gammaN, dimensions, save=False):
    norm_overlaps = np.multiply(np.conj(overlaps), overlaps)
    real_overlaps = np.real(overlaps)
    imag_overlaps = np.imag(overlaps)
    ys = [real_overlaps, imag_overlaps, norm_overlaps]
    fig, ax = plt.subplots()
    linestyles = ['dashed', 'dashed', 'solid']
    for i, y in enumerate(ys):
        ax.plot(times, y, linestyle=linestyles[i])
    ax.legend(['$Re(\langle m| U |s\\rangle)$',
                '$Im(\langle m| U |s\\rangle)$',
                '$|\langle m| U |s\\rangle|^2$'])
    ax.set(xlabel='$time~(\hbar s)$')
    ax.grid() 
    if save:
        plt.savefig(f'plots/overlaps/overlaps_alpha={alpha}_gammaN={gammaN}_N={dimensions}.png')
    plt.show()


if __name__ == "__main__":
    dimensions = 1024
    mark = 5
    gamma = 180/dimensions
    alpha = 1
    number_of_points = 1000
    m_ket = marked_state(n=dimensions, marked=mark)
    s_ket = superposition_state(n=dimensions) 

    # GammaN eigenstates with m and s state amplitudes 
    gammasN, amps, e1_minus_e0s = eigenstate_m_and_s_overlap(s_ket, m_ket, 
                                                            dimensions, mark, 
                                                            gamma, alpha, 
                                                            number_of_points) 


    #~~~ Optimum gamma N
    opt_gammaN = gammasN[np.argmin(e1_minus_e0s)]
    print(f'optimum gammaN value is {opt_gammaN}')


    #~~~ Unitary evolution
    #opt_gammaN = 80.0
    H_alpha_0 = hamiltonian_matrix(n=dimensions, gamma=(opt_gammaN/dimensions), alpha=1, marked=mark)
    times, overlaps = unitary_evolution(H_alpha_0, s_ket, m_ket, 200, 0.5)
    

    #~~~ Plots
    amplitudes_plot(alpha, dimensions, gammasN, amps, e1_minus_e0s, save=True)
    overlaps_plot(times, overlaps, alpha=alpha, gammaN=opt_gammaN, dimensions=dimensions, save=True)

