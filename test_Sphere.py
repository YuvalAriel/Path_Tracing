from Sphere import Sphere
from Ray import Ray


def test_intersect():
    sphere = Sphere(radius=1, center=(0, 0, 0))
    hitting_ray = Ray(source=(1, 1, 1), direction=(-1, -1, -0.99999))
    missing_ray = Ray(source=(1, 1, 1), direction=(1, 0, 0))
    assert sphere.intersect(ray=hitting_ray)
    assert sphere.intersect(ray=missing_ray) is False
