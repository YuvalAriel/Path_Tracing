from math import sqrt
from Vec3D import Vec3D
from Material import Material


class Sphere:
    def __init__(self, center, radius=2, material=Material([0, 0, 1])):
        self.center = Vec3D(center[0], center[1], center[2])
        self.radius = float(radius)
        self.radius_squared = self.radius * self.radius
        self.material = material

    def sphere_intersect(self, ray):
        """ returns t if intersected. if not returns False. hit_point = origin +t*l"""
        # need to solve for t: t^2(ldotl) + 2t(ldot(o-c)) + (o-c)dot(o-c) - r^2 = 0. where:
        # t = distance along ray from starting point. l = direction of ray(a unit vector). o = origin of ray.
        # c = center of sphere. r = radius of sphere.
        oc = ray.origin.vec_sub(self.center)
        a = ray.norm_dir.vec_dot(ray.norm_dir)
        b = ray.norm_dir.vec_dot(oc) * 2
        c = oc.vec_dot(oc) - self.radius_squared
        t = sol_quad(a, b, c)
        return t

    def get_hit_norm(self, hit_point):
        return hit_point.vec_sub(self.center).vec_normalize()


def sol_quad(a, b, c):
    discriminant = b * b - 4 * a * c
    if discriminant <= 0:
        return False
    # elif discriminant == 0:  # ray hits the sphere only on the edge. negligible so removed.
    #     x0 = x1 = 0.5 * b / a
    else:  # need to return the smallest absolute value. closer to ray origin.
        if b > 0:
            q = -0.5 * (b + sqrt(discriminant))
        else:
            q = -0.5 * (b - sqrt(discriminant))
        x0 = q / a
        x1 = c / q
    if x0 > x1:
        x0, x1 = x1, x0
    if x0 < 0:
        x0 = x1  # if t0 is negative, let's use t1 instead
        if x0 < 0:  # both t0 and t1 are negative
            return False
    return x0
