from Vec3D import Vec3D
from Material import Material

epsilon = 0.000001


class Plane:
    """
    https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-plane-and-ray-disk-intersection
    n= plane normal
    (p-p0)dot(n)=0  # p-p0 is any vector on the plane given p0. dot product of two perpendicular vectors equals zero.
    ray: ray_origin + ray_direction*t = p
    combining the two: # l∗t⋅n+(l0−po)⋅n=0 , arrange -> t=(p0−l0)⋅n/l⋅n
    """
    def __init__(self, normal, point, material=Material([0.2, 0.2, 0.2])):
        self.plane_norm = Vec3D(normal[0], normal[1], normal[2])
        self.plane_norm = self.plane_norm.vec_normalize()
        self.p0 = Vec3D(point[0], point[1], point[2])
        self.material = material

    def plane_intersect(self, ray):
        """ returns t if intersected. if not returns False."""
        n = self.plane_norm
        v1 = self.p0.vec_sub(ray.origin)  # vector from a point on the plane to the ray origin
        ln = ray.norm_dir.vec_dot(n)  # when close to zero then ray and plane are parallel.
        #  equation of a plane:  norm.x*x + norm.y*y+norm.z*z = norm.x*p0.x + norm.y*p0.y + norm.z*p0.z

        if ln == 0:
            return False
        t = v1.vec_dot(n) / ln
        if abs(ln) > epsilon and t > 0:
            return t
        return False

    def get_hit_norm(self, hit_point):
        # unused parameter because find_closest_intersection method is applied to varying objects
        return self.plane_norm


class Disk:
    def __init__(self, normal, point, radius=2, material=Material([0, 0.5, 0])):
        self.disk_norm = Vec3D(normal[0], normal[1], normal[2])
        self.disk_norm = self.disk_norm.vec_normalize()
        self.disk_center = Vec3D(point[0], point[1], point[2])
        self.radius = radius
        self.radius_squared = self.radius * self.radius
        self.material = material

    def disk_intersect(self, ray):
        """ returns t if intersected. if not returns False."""
        n = self.disk_norm
        v1 = self.disk_center.vec_sub(ray.origin)  # vector from a point on the plane to the ray origin
        ln = ray.norm_dir.vec_dot(n)  # when close to zero then ray and plane are parallel.
        t = v1.vec_dot(n) / ln
        if ln > epsilon and t > 0:
            p = ray.origin.vec_add(ray.norm_dir.vec_mul(t))  # p - point on the plane where the ray intersected.
            d = p.vec_sub(self.disk_center)  # vector from p to center of disk.
            distance = d.vec_dot(d)
            if distance <= self.radius_squared:
                return t
        return False

    def get_hit_norm(self, hit_point):
        return self.disk_norm
