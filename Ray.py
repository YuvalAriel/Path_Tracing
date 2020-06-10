from math import sqrt
from Vec3D import Vec3D


class Ray:
    """ 3D line from origin in a specified direction. the direction is a vector describing the ray"""

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction  # Vec3D(direction[0], direction[1], direction[2])
        self.norm_dir = self.direction.vec_normalize()
        # self.hit_pos = None
        # self.hit_norm = None

    # def magnitude(self):
    #     return sqrt(self.direction.vec_dot(self.direction))
    #
    # def normalize(self):
    #     return self.direction.vec_normalize()

# ray1 = Ray(origin=(1,3,5), direction=(0,4,0))
