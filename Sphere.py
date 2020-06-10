from math import sqrt
from Vec3D import Vec3D
from Material import Material


class Sphere:
    """material parameter should receive a Material Class as an argument"""

    def __init__(self, center, radius=2, material=Material([0, 0, 1])):
        self.center = Vec3D(center[0], center[1], center[2])
        self.radius = float(radius)
        self.material = material

    def sphere_intersect(self, ray):
        """ returns d if intersected. if not returns false. hit_point = origin +d*l"""
        # check 3 cases: 1. ray missed sphere. 2. ray hit sphere at one point. 3. ray hit sphere at two points.
        # record Hit details: location, normal, ..
        # need to solve for d: d^2(ldotl) + 2d(ldot(o-c)) + (o-c)dot(o-c) - r^2 = 0. where:
        # d = distance along ray from starting point. l = direction of ray(a unit vector). o = origin of ray.
        # c = center of sphere. r = radius of sphere.
        l = ray.norm_dir
        o = ray.origin
        c = self.center
        r = self.radius
        co = o.vec_sub(c)  # the vector from center of sphere to origin of ray.
        discriminant = (l.vec_dot(co)) ** 2 - (co.vec_dot(co) - (r * r))  # simplified because |l|^2 = 1 always(if norm)
        if discriminant <= 0:  # ray missed the sphere, also if =0 cause then ray hits the exact edge.
            # if -l.dot(co)=0 then direction of ray in 90deg to co. orthogonal. no hit unless o is inside sphere.
            return False
        if co.vec_dot(co) < r * r:
            print("oops, ray origin is inside sphere")
            return False
        if l.vec_dot(co) > 0:
            # could be that camera or objects are misaligned and d is negative.
            # print("oops, object behind ray direction. reorient camera or objects.")
            return False
        else:  # has two intersection points. need to pick closest one to ray origin.
            # d1 = -l.vec_dot(co) + sqrt(discriminant) dot prod of l and co is negative when l is directed at sphere.
            d = -l.vec_dot(co) - sqrt(discriminant)  # always the smaller option, closer to ray origin.
            return d
            #  create record of hit position. include: position3d, normal, inside/outside? norm=-norm?
            #  ray.hit_pos = o + l*d
            #  ray.hit_norm = (ray.hit_pos - c)/(sqrt((ray.hit_pos - c).dot((ray.hit_pos - c))))

    def get_hit_norm(self, hit_point):
        return hit_point.vec_sub(self.center).vec_normalize()

