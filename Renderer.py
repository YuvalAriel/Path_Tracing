import math
import sys
import numpy as np
import matplotlib.pyplot as plt

from Vec3D import Vec3D
from Scene import Scene
from Sphere import Sphere
from Material import Material
from Ray import Ray
from Camera import Camera


# (noam) read about fakes and mocks in tests
# (noam) read about dependancy injection
class Renderer:
    def __init__(self, scene, camera, max_depth=2, num_samples=3, num_UV_samples=3):
        self.scene = scene
        self.camera = camera
        self.max_depth = max_depth
        self.num_samples = num_samples  # for antialiasing. number of rays per pixel.
        self.num_UV_samples = num_UV_samples

    def render(self):
        # w columns X h rows. each has a list of 3 zeroes. each pixel initialized to 0,0,0.
        img = np.zeros((self.camera.img_height, self.camera.img_width, 3))
        for w in range(0, self.camera.img_width):
            for h in range(0, self.camera.img_height):
                color = np.zeros(3)  # r,g,b = 0
                for _ in range(0, self.num_samples):
                    # create a ray from camera origin that goes through pixel w,h.
                    ray = self.camera.gen_rand_ray(pixelx=w, pixely=h)
                    # needs to return color value as np.array rgb [0,1].
                    color = color + self.compute_sample(ray, depth=0)
                img[h, w, :] = np.clip(color / self.num_samples, 0, 1)
        plt.imsave('pics\\UV.png', img)

    # (noam) consider making these helper functions private
    def compute_sample(self, ray, depth):
        if depth > self.max_depth:
            return np.zeros(3)
        # ask scene to find the closest intersection point.
        obj_material, hit_position, norm = self.scene.find_closest_intersection(ray=ray)
        # after finding the hit_obj. need to produce the resulting ray which depends on: material, hit position, norm.
        if hit_position is None:  # if ray didnt hit anything, return environment color.
            return self.scene.environment_color

        if depth == 0:  # on first hit, send u*v number of rays. u and v will be used to determine direction of rays.
            num_U_samples = num_V_samples = self.num_UV_samples
        else:
            num_U_samples = num_V_samples = 1

        color_result = np.zeros(3)
        for u in range(num_U_samples):
            for v in range(num_V_samples):
                # send new rays depending on material properties.
                color_result = color_result + self.send_new_ray(obj_material, hit_position, norm, u, v, depth)

        total_ray_emission = obj_material.color + color_result / (num_V_samples * num_U_samples)

        return total_ray_emission

    def send_new_ray(self, obj_material, hit_position, norm, u, v, depth):
        # (noam) Consider adding TODO with what you wish to implement here.
        # depending on material properties: will send new ray either as cone sample or as hemisphere sample.
        # at the moment, send new ray in direction of norm to the hit_position.
        reflected_ray = Ray(hit_position, norm)

        # recursive call
        return self.compute_sample(ray=reflected_ray, depth=depth + 1)
