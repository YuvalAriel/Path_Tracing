import math
import random


class Vec3D:
    def __init__(self, x, y=None, z=None):
        if y is None and z is None:
            self.x = float(x.x)
            self.y = float(x.y)
            self.z = float(x.z)
        else:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)

    def vec_dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def vec_sub(self, other):
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def vec_add(self, other):
        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def vec_multiplication(self, factor):
        return Vec3D(self.x * factor, self.y * factor, self.z * factor)

    def vec_normalize(self):
        return Vec3D(self.vec_multiplication(1/(math.sqrt(self.vec_dot(self)))))


