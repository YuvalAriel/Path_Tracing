import numpy as np


class Ray:

    def __init__(self, source, direction):
        self.source = np.array(source)
        self.direction = np.array(direction)
