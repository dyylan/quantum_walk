import numpy as np


class Ket:

    def __init__(self, dimensions, type='s', marked=1):
        """Creates different types of kets given by a letter."""
        self.dimensions = dimensions
        self.type = type.lower()
        if self.type == 'm':
            self.ket = Ket.marked_state(dimensions, marked)
            self.marked = marked
        elif self.type == 's':
            self.ket = Ket.superposition_state(dimensions)
        else:
            raise ValueError(f'No ket has type: {self.type}')
        
    @staticmethod
    def marked_state(dimensions, marked):
        return np.array([0 if i != (marked-1) else 1 for i in range(dimensions)])

    @staticmethod
    def superposition_state(dimensions):
        return (1/np.sqrt(dimensions))*np.array([1 for _ in range(dimensions)])