import numpy as np


class Material:
    """send color as list of 3 floats in range of 0-1"""
    def __init__(self, color):
        self.color = np.array(color)
        self.reflection = 0.5
        # self.diffuse = 1
        # self.specular = 0



