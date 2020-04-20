import numpy as np
import scipy.linalg
from .ket import Ket


class Rho:

    def __init__(self, n, hamiltonain):
        """
        """
        self.n = n
        self.dimensions = 2**n
        self.hamiltonain = hamiltonain
        self.rho_0 = initial_rho()
        self.rho_t = self.rho_0
        self.projectors_0 = get_projectors_0()
        self.projectors_1 = get_projectors_1()

    def initial_rho():
        s_ket = Ket(self.dimensions, 's', full=True)
        return np.inner(s_ket.ket, s_ket.ket)

    def get_projectors_0():
        projectors = []
        ket_0 = np.array([1, 0])
        identity = np.matrix('1 0; 0 1')
        for i in range(self.n):
            if i == 0:
                proj = np.outer(ket_0,ket_0)
            else:
                proj = identity
            for j in range(1,n):
                if j == i:
                    proj = np.kron(proj,np.outer(ket_0,ket_0))
                else:
                    proj = np.kron(proj,identity)
            projectors.append(proj)
        return projectors

    def get_projectors_0():
        projectors = []
        ket_1 = np.array([0, 1])
        identity = np.matrix('1 0; 0 1')
        for i in range(self.n):
            if i == 0:
                proj = np.outer(ket_1,ket_1)
            else:
                proj = identity
            for j in range(1,n):
                if j == i:
                    proj = np.kron(proj,np.outer(ket_1,ket_1))
                else:
                    proj = np.kron(proj,identity)
            projectors.append(proj)
        return projectors

    def update_rho(kappa, grain, time_step=1):
        current_rho = self.rho_t
        steps = grain*time_step
        for t in range(steps):
            h_rho = np.matmul(self.hamiltonain,current_rho)
            rho_h = np.matmul(current_rho,self.hamiltonain)
            new_rho = current_rho- ( 1j/grain )*( h_rho - rho_h )
            if kappa != 0:
                p_term = self.projectors_0[0].dot(current_rho.dot(self.projectors_0[0])) + self.projectors_1[0].dot(current_rho.dot(self.projectors_1[0]))
                for i in range(1,n):
                    p_term = p_term + self.projectors_0[i].dot(current_rho.dot(self.projectors_0[i])) + self.projectors_1[i].dot(current_rho.dot(self.projectors_1[i]))
                new_rho = new_rho - (kappa/grain)*( current_rho - (1/self.n)*p_term )
            current_rho = new_rho
        self.rho_t = current_rho

