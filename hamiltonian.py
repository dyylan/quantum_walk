import numpy as np
import scipy.linalg
from ket import Ket


class Hamiltonian:

    def __init__(self, dimensions, gamma, alpha, marked_state):
        """Initialises a hamiltonian with the form of a spatial quantum walk
        with a 1/|i-j|^alpha potential drop-off.
        """
        self.dimensions = dimensions
        self.gamma = gamma
        self.alpha = alpha
        self.marked = marked_state
        self._m_ket = Ket(dimensions, 'm', 2)
        self._s_ket = Ket(dimensions, 's')
        self.H_matrix = self._hamiltonian_matrix()
        self.eigenvectors, self.eigenvalues = Hamiltonian.eigenvectors_eigenvalues(self.H_matrix)
        self.psi_0, self.psi_1 = self.eigenvectors[:,0], self.eigenvectors[:,1]
        self.energy_0, self.energy_1 = self.eigenvalues[0], self.eigenvalues[1]

    @property
    def m_ket(self):
        return self._m_ket.ket

    @m_ket.setter
    def m_ket(self, marked_state):
        self._m_ket = Ket(dimensions, 'm', marked_state)

    @property
    def s_ket(self):
        return self._s_ket.ket
    
    def unitary_evolution(self, initial_state, end_time, dt=None):
        if not dt:
            times = [dt*interval for interval in range(int(np.ceil(end_time/dt)))]
            states = [np.matmul(self._unitary_matrix(time), initial_state)
                                                                for time in times]
            return states, times 
        else: 
            state = np.matmul(self._unitary_matrix(end_time), initial_state)
            return state, end_time

    def _hamiltonian_matrix(self):
        if self.alpha:
            H = -self.gamma*np.array([[(1/(np.abs(col-row)))**(self.alpha) if col != row else 1 
                                                for col in range(self.dimensions)] 
                                                    for row in range(self.dimensions)]) 
            H[(self.marked-1, self.marked-1)] = H[(self.marked-1, self.marked-1)] - 1
        else:
            H = -self.gamma*self.dimensions*np.outer(self.s_ket, self.s_ket) - \
                    np.outer(self.m_ket, self.m_ket) 
        return H

    def _unitary_matrix(self, time):
        print(f'Computing hamiltonian at time: {time}')
        return scipy.linalg.expm(-1j*self.H_matrix*time)

    @staticmethod
    def eigenvectors_eigenvalues(hamiltonian):
        """Returns sorted eigenvalues and eigenvectors."""
        eigenvalues, eigenvectors = scipy.linalg.eig(hamiltonian)
        index = np.argsort(eigenvalues)
        eigenvalues = eigenvalues[index]
        eigenvectors = eigenvectors[:,index]
        return eigenvectors, eigenvalues