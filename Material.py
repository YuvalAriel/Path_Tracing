import numpy as np


class Material:
    def __init__(self, color3D):
        self.color = np.array(color3D)
        self.reflection = 1
        self.diffuse = 1
        self.specular = 0



