import numpy as np


class Material:
    """send color as list of 3 floats in range of 0-1"""

    def __init__(self, color, reflection=0, transparency=0, emission=np.array((0, 0, 0)), refraction_ind=1):
        self.color = np.array(color)
        self.emission = emission  # only for light sources
        self.reflection = reflection
        self.transparency = transparency
        self.refraction_ind = refraction_ind
