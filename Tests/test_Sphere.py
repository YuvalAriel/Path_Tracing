from Sphere import Sphere
from Ray import Ray


def test_sphere_intersect():
    sphere = Sphere(radius=5, center=(15, 0, 0))
    hitting_ray = Ray(origin=(0, 0, 0), direction=(1, 0, 0))
    missing_ray = Ray(origin=(0, 0, 0), direction=(0, 1, 0))
    assert sphere.sphere_intersect(ray=hitting_ray)
    assert sphere.sphere_intersect(ray=missing_ray) is False
