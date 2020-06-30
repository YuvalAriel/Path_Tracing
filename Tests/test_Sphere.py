from Sphere import Sphere
from Ray import Ray
from Vec3D import Vec3D


def test_sphere_intersect():
    sphere = Sphere(radius=5, center=(15, 0, 0))
    hitting_ray = Ray(origin=Vec3D(0, 0, 0), direction=Vec3D(1, 0, 0))
    missing_ray = Ray(origin=Vec3D(0, 0, 0), direction=Vec3D(0, 1, 0))
    assert sphere.sphere_intersect(ray=hitting_ray)==10
    assert sphere.sphere_intersect(ray=missing_ray) is False
