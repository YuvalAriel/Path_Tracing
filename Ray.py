class Ray:
    """ 3D line from origin in a specified direction. the direction is a vector describing the ray"""

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
        self.norm_dir = self.direction.vec_normalize()