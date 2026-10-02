import numpy as np

# IsingSystem2D class that holds a paricular spin configuration at any given time in a square lattice of equal side lengths
class IsingSystem2D:
    def __init__(self, num_electrons_side):
        '''
        num_electrons_side: the number of electrons per side of the square lattice of electrons
        '''
        # initialise variable to store the side_length
        self.side_length = num_electrons_side

        # initialise the configuration of the Ising system with random orientations of the elctron spins
        self.configuration = 2 * np.random.randint(0, 2, (num_electrons_side, num_electrons_side)) - 1 

    # method to flip the spin of a particular electron
    def flip(self, electron_pos_x, electron_pos_y):
        '''
        electron_pos_x: the x coordinate of the electron desired for flipping, ranging from 0 to num_electrons_side - 1
        electron_pos_y: the y coordinate of the electron desired for flipping, ranging from 0 to num_electrons_side - 1
        '''

        self.configuration[electron_pos_x, electron_pos_y] *= -1;

    # method to compute the difference in Hamiotonian over a spin flip
