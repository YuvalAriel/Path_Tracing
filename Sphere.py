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
        """ returns d if intersected. if not returns False. hit_point = origin +t*l"""
        # need to solve for t: t^2(ldotl) + 2t(ldot(o-c)) + (o-c)dot(o-c) - r^2 = 0. where:
        # t = distance along ray from starting point. l = direction of ray(a unit vector). o = origin of ray.
        # c = center of sphere. r = radius of sphere.
        L = ray.origin.vec_sub(self.center)
        a = ray.norm_dir.vec_dot(ray.norm_dir)
        b = ray.norm_dir.vec_dot(L) * 2
        c = L.vec_dot(L) - self.radius_squared
        t = sol_quad(a, b, c)
        if t:
            return t
        else:
            return False

        # l = ray.norm_dir
        # co = ray.origin.vec_sub(self.center)  # the vector from center of sphere to origin of ray.
        # discriminant = (l.vec_dot(co)) ** 2 - (co.vec_dot(co) - self.radius_squared)
        # if discriminant <= 0:  # ray missed the sphere, also if =0 cause then ray hits the exact edge.
        #     # if -l.dot(co)=0 then direction of ray in 90deg to co. orthogonal. no hit unless o is inside sphere.
        #     return False
        # if co.vec_dot(co) < self.radius_squared:
        #     print("oops, ray origin is inside sphere")
        #     return False
        # if l.vec_dot(co) > 0:
        #     # meaning the ray direction and the direction from the sphere center to the ray origin are the same.
        #     # could only happen if sphere is behind ray direction.
        #     return False
        # # has two intersection points. need to pick closest one to ray origin.
        # elif -l.vec_dot(co) - sqrt(discriminant) > 0:
        #     t = -l.vec_dot(co) - sqrt(discriminant)
        #     return t
        # else:
        #     t = -l.vec_dot(co) + sqrt(discriminant)  # dot prod of l and co is negative when l is directed at sphere.
        #     return t

    def get_hit_norm(self, hit_point):
        return hit_point.vec_sub(self.center).vec_normalize()


def sol_quad(a, b, c):
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return False
    elif discriminant == 0:
        x0 = x1 = 0.5 * b / a
    else:
        if b > 0:
            q = -0.5 * (b + sqrt(discriminant))
        else:
            q = -0.5 * (b - sqrt(discriminant))
        x0 = q / a
        x1 = c / q
    if x0 > x1:
        x0, x1 = x1, x0
    if x0 < 0:
        x0 = x1 # if t0 is negative, let's use t1 instead
        if x0 < 0:  # both t0 and t1 are negative
            return False
    return x0
