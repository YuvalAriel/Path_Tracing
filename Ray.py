from math import sqrt
from Vec3D import Vec3D


class Ray:
    """ 3D line from origin in a specified direction. the direction is a vector describing the ray"""

    def __init__(self, origin=(0, 0, 0), direction=(1, 0, 0)):
        self.origin = Vec3D(origin)
        self.direction = Vec3D(direction)
        self.ray_norm = self.direction.vec_normalize()
        self.hit_pos = None
        self.hit_norm = None

    def magnitude(self):
        return sqrt(self.direction.vec_dot(self.direction))

    def normalize(self):
        return self.direction.vec_normalize()

    def distance_to_point(self, d): # not used yet.
        # magnitude of the ray between origin and the point.
        # receives parameter d from intersect.
        end_point = self.origin.vec_add(self.normalize() * d)
        print(end_point)
        return sqrt((end_point - self.origin).vec_dot(end_point - self.origin))


# ray1 = Ray(origin=(1,3,5), direction=(0,4,0))
