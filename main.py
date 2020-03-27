import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt


def hamiltonian_matrix(n, gamma=1, alpha=0, marked=1):
    H_matrix = -gamma*np.array([[(1/(np.abs(col-row)))**(alpha) if col != row else 1 
                                    for col in range(n)] 
                                        for row in range(n)])
    H_matrix[(marked-1, marked-1)] = H_matrix[(marked-1, marked-1)] - 1
    return H_matrix


def unitary_matrix(H_matrix, time=1):
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


def amplitudes_plot(alpha, dimensions, gammasN, amps, e1_minus_e0):
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
    plt.savefig(f'plots/alpha={alpha}_dim={dimensions}.png')
    plt.show()


if __name__ == "__main__":
    dimensions = 1024
    mark = 5
    gamma = 4000/dimensions
    alpha = 3
    number_of_points = 100
    gammas = [gamma*(i/number_of_points) for i in range(1,(number_of_points+1))]
    m_psi_0s = []
    s_psi_0s = []
    m_psi_1s = []
    s_psi_1s = []
    e1_minus_e0s = []        
    m_ket = marked_state(n=dimensions, marked=mark)
    s_ket = superposition_state(n=dimensions)    
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
    amplitudes_plot(alpha, dimensions, gammasN, 
                    [m_psi_0s, m_psi_1s, s_psi_0s, s_psi_1s], e1_minus_e0s)
    