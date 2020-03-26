import numpy as np


def hamiltonian_matrix(n, alpha=0):
    H_matrix = np.array([[(1/(np.abs(col-row)))**(alpha) if col != row else 1 
                                    for col in range(n)] 
                                        for row in range(n)])
    return H_matrix


if __name__ == "__main__":
    print(hamiltonian_matrix(n=5, alpha=2))