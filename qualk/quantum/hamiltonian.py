import numpy as np
import scipy.linalg
from .ket import Ket


class Hamiltonian:

    def __init__(self, dimensions, gamma, alpha, marked_state, chain='open', lattice_d=1):
        """Initialises a hamiltonian with the form of a spatial quantum walk
        with a 1/|i-j|^alpha potential drop-off.
        """
        if chain in [1, 'open', 'o']:
            self._chain = 1
        elif chain in [2, 'ring', 'r']:
            self._chain = 2
        elif chain in [3, 'chord', 'c']:
            self._chain = 3
        else:
            raise ValueError(f'{chain} is not a valid chain specification!')
        self.lattice_d = lattice_d
        self.dimensions = dimensions
        self.gamma = gamma
        self.alpha = alpha
        self.marked = marked_state
        self._m_ket = Ket(dimensions, 'm', marked_state)
        self._s_ket = Ket(dimensions, 's')
        if lattice_d == 1:
            self.H_matrix = self._hamiltonian_matrix()
        elif lattice_d == 2:
            if self.chain == 1:
                self.H_matrix = self._2d_hamiltonian_matrix()
            else:
                raise ValueError('Cannot have a 2d Hamiltonian with a ring or chord yet.')
        self.eigenvectors, self.eigenvalues = Hamiltonian.eigenvectors_eigenvalues(self.H_matrix)
        self.psi_0, self.psi_1 = self._psi_0_and_psi_1()
        self.energy_0, self.energy_1 = self._energy_0_and_energy_1()

    @property
    def m_ket(self):
        return self._m_ket.ket

    @m_ket.setter
    def m_ket(self, marked_state):
        self._m_ket = Ket(dimensions, 'm', marked_state)

    @property
    def s_ket(self):
        return self._s_ket.ket
    
    def unitary_evolution(self, end_time, dt=None, print_status=False, initial_state='s'):
        initial_state = self.s_ket if initial_state=='s' else Ket(self.dimensions, initial_state).ket
        if dt:
            times = [dt*interval for interval in range(int(np.ceil(end_time/dt)))]
            states = [np.matmul(self._unitary_matrix(time, print_status), initial_state)
                                                                for time in times]
            return states, times 
        else: 
            state = np.matmul(self._unitary_matrix(end_time), initial_state)
            return state, end_time

    def full_hamiltonian(self):
        N = 2**self.dimensions
        full_H = np.zeros([N,N])
        non_zeros = [(2**i) for i in range(self.dimensions)]
        for i,k in enumerate(non_zeros):
            for j,l in enumerate(non_zeros):
                full_H[k][l] = self.H_matrix[self.dimensions-(i+1)][self.dimensions-(j+1)]
        self.H_matrix = full_H
        full_marked = non_zeros[self.dimensions-self.marked]+1
        self._m_ket =  Ket(N, 'm',full_marked)
        full_s = (1/np.sqrt(self.dimensions))*np.array([1 if i in non_zeros else 0 for i in range(N)])
        self._s_ket.ket = full_s

    def _hamiltonian_matrix(self):
        if self._chain == 1:
            def coef(row, col):
                return 1/((np.abs(col-row))**(self.alpha))
        elif self._chain == 2:
            def coef(row, col):
                return 1/((np.abs(col-row))**(self.alpha)) + 1/((np.abs(self.dimensions-np.abs(col-row)))**(self.alpha))
        elif self._chain == 3:
            def coef(row, col):
                return np.pi**self.alpha/((self.dimensions*np.abs(np.sin(np.pi*(row-col)/self.dimensions)))**self.alpha)
        if self.alpha: 
            H = -self.gamma*np.array([[coef(row, col) if col != row else 1
                                                for col in range(self.dimensions)] 
                                                    for row in range(self.dimensions)]) 
            H[(self.marked-1, self.marked-1)] = H[(self.marked-1, self.marked-1)] - 1
        else:
            H = -self.gamma*self.dimensions*np.outer(self.s_ket, self.s_ket) - \
                    np.outer(self.m_ket, self.m_ket) 
        return H

    def _2d_hamiltonian_matrix(self):
        def coef(i, j, k, l):
            return 1/(((i-k)**2 + (j-l)**2)**(self.alpha/2))
        n = range(int(self.dimensions**(1/self.lattice_d)))
        H = [[coef(i,j,k,l) if not (i==k and j==l) else 1 for k in n for l in n] for i in n for j in n]
        H = -self.gamma*np.array(H)
        H[(self.marked-1, self.marked-1)] = H[(self.marked-1, self.marked-1)] - 1
        return H

    def _unitary_matrix(self, time, print_status=False):
        if print_status:
            print(f'Computing unitary evolution at time: {time}')
        return scipy.linalg.expm(-1j*self.H_matrix*time)

    def _psi_0_and_psi_1(self):
        return self.eigenvectors[:,0], self.eigenvectors[:,1]

    def _energy_0_and_energy_1(self):
        return self.eigenvalues[0], self.eigenvalues[1]

    @staticmethod
    def eigenvectors_eigenvalues(hamiltonian):
        """Returns sorted eigenvalues and eigenvectors."""
        eigenvalues, eigenvectors = scipy.linalg.eig(hamiltonian)
        index = np.argsort(eigenvalues)
        eigenvalues = eigenvalues[index]
        eigenvectors = eigenvectors[:,index]
        return eigenvectors, eigenvalues