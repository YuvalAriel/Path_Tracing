from Plane_Disk import Plane, Disk
from Vec3D import Vec3D
from Ray import Ray

# equation of a plane:  norm.x*x + norm.y*y+norm.z*z = norm.x*p0.x + norm.y*p0.y + norm.z*p0.z


def test_plane_intersect():
    plane = Plane(normal=(0, 1, 1), point=(0, 0, -1))
    hitting_ray = Ray(origin=Vec3D(0, 0, 0), direction=Vec3D(0, 0, -1))
    missing_ray = Ray(origin=Vec3D(0, 0, 0), direction=Vec3D(0, 1, 0))
    assert plane.plane_intersect(ray=hitting_ray)
    assert plane.plane_intersect(ray=missing_ray) is False

