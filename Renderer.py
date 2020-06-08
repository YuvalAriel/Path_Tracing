import math
import sys

from Vec3D import Vec3D
from Scene import Scene
from Sphere import Sphere
from Material import Color
from Ray import Ray
from Camera import Camera


class Renderer:
    def __init__(self, scene, camera):
        self.scene = scene
        self.camera = camera
        self.max_depth = 3
        self.num_samples = 2  # for antialiasing. number of rays per pixel.

    def render(self):

        for w in range(0, self.camera.img_width):
            for h in range(0, self.camera.img_height):
                color = Vec3D(0, 0, 0)
                for _ in range(0, self.num_samples):
                    # create a ray from camera origin that goes through pixel w,h. ray
                    ray = self.camera.gen_rand_ray(pixelx=w, pixely=h)
                    color += self.computeSample(ray, depth=0)
                # plot pixel w,h. as average. sum_color/num_samples.

    def computeSample(self, x, y, depth):


        ray = Ray(self.camera, direction)

        return self.trace(ray, 1)

    def trace(self, ray, currentDepth):
        hitDistance = 5000.0
        hitObject = None

        for sphere in self.scene.list:
            intersect = sphere.intersect(ray)
            if hitDistance > intersect > -1.0:
                hitDistance = intersect
                hitObject = sphere
        if hitDistance == 5000.0:
            return Color(0, 0, 0)
        elif hitObject.isEmitter:
            return hitObject.color
        elif currentDepth == self.max_depth:
            return Color(0, 0, 0)

        hitPoint = ray.origin.add(
            ray.direction.mul(hitDistance * 0.998))  # by.988 to prevent casting a ray into sphere
        # normal = hitObject.sphere_norm(hitPoint)

        randomPoint = Vec3D.sample_hemi()  # sample_hemi not def yet
        # if (randomPoint.vec_dot(normal) < 0.0):  # to check if sampled from right hemisphere.
        #   randomPoint = randomPoint.negate()  # negate not def yet
        reflectionRay = Ray(hitPoint, randomPoint.vec_normalize())

        returnColor = self.trace(reflectionRay, currentDepth + 1)

        r = hitObject.color.r * returnColor.r
        g = hitObject.color.g * returnColor.g
        b = hitObject.color.b * returnColor.b

        r /= 255.0
        g /= 255.0
        b /= 255.0

        return Color(r, g, b)
