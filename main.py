import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

def hamiltonian_matrix(n, gamma=1, alpha=0, marked=1):
    H_matrix = -gamma*np.array([[(1/(np.abs(col-row)))**(alpha) if col != row else 1 
                                    for col in range(n)] 
                                        for row in range(n)])
    H_matrix[(marked-1, marked-1)] = 0
    return H_matrix


def unitary_matrix(H_matrix, time=1):
    return scipy.linalg.expm(-1j*H_matrix*time)


def marked_state(n, marked=1):
    return np.array([0 if i != (marked-1) else 1 for i in range(n)])


def superposition_state(n):
    return (1/np.sqrt(n))*np.array([1 for _ in range(n)])


def eigenvectors_and_eigenvalues(hamiltonian):
    eigenvalues, eigenvectors = scipy.linalg.eig(hamiltonian)
    return eigenvalues, eigenvectors

def psi_0_and_psi_1(eigenvalues, eigenvectors):
    sorted_eigenvectors = eigenvectors[np.argsort(eigenvalues)]
    return sorted_eigenvectors[0], sorted_eigenvectors[1]


def E_0_and_E_1(eigenvalues, eigenvectors):
    sorted_eigenvalues = np.sort(eigenvalues)
    return sorted_eigenvalues[0], sorted_eigenvalues[1]


def amplitudes_plot(gammas, amps):
    fig, ax = plt.subplots()
    for amp in amps:
        ax.plot(gammas, amp)
    #ax.legend([])
    ax.set(xlabel='$\gamma$', ylabel='Amplitude')
    ax.grid()    
    plt.savefig('fig_1.png')
    plt.show()


if __name__ == "__main__":
    dimensions = 1024
    mark = 2
    gamma = 0.1
    alpha = 0
    number_of_points = 10
    gammas = [gamma*(i/number_of_points) for i in range(number_of_points+1)]
    m_psi_0s = []
    s_psi_0s = []
    m_psi_1s = []
    s_psi_1s = []
    for point, gamma in enumerate(gammas):
        m_ket = marked_state(n=dimensions, marked=mark)
        s_ket = superposition_state(n=dimensions)
        H = hamiltonian_matrix(n=dimensions, gamma=gamma, alpha=alpha, marked=mark)
        eigenvalues, eigenvectors = eigenvectors_and_eigenvalues(H)
        psi_0, psi_1 = psi_0_and_psi_1(eigenvalues, eigenvectors)
        e_0, e_1 = E_0_and_E_1(eigenvalues, eigenvectors)
        m_psi_0s.append(np.square(np.abs(np.dot(m_ket, psi_0))))
        s_psi_0s.append(np.square(np.abs(np.dot(s_ket, psi_0))))
        m_psi_1s.append(np.square(np.abs(np.dot(m_ket, psi_1))))
        s_psi_1s.append(np.square(np.abs(np.dot(s_ket, psi_1))))
        print(f'Finished point: {point} --  gamma: {gamma}')
    amplitudes_plot(gammas, [m_psi_0s, s_psi_0s, m_psi_1s, s_psi_1s])
    '''
    print(times)
    m_ket = marked_state(n=dimensions, marked=mark)
    s_ket = superposition_state(n=dimensions)
    print(m_ket)
    print(s_ket)
    H = hamiltonian_matrix(n=dimensions, gamma=gamma, alpha=alpha, marked=mark)
    U = unitary_matrix(H, time=time)
    U_s_ket = np.matmul(U, s_ket)
    amplitude = np.dot(m_ket, U_s_ket)
    print(H)
    print(U)
    print(amplitude)
    '''
    