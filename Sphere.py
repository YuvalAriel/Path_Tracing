import numpy as np


class Sphere:

    def __init__(self, center, radius):
        self.center = np.array(center)
        self.radius = np.array(radius)

    def intersect(self, ray):
        if (self.center == ray.source + ray.direction).all():
            return True
        return False
