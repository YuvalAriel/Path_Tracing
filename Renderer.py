import math
import numpy as np
import matplotlib.pyplot as plt
import random

from Vec3D import Vec3D
from Scene import Scene
from Material import Material
from Ray import Ray
from Camera import Camera


# (noam) read about fakes and mocks in tests
# (noam) read about dependancy injection
class Renderer:
    def __init__(self, scene, camera, max_depth=3, pixel_samples=5, num_U_samples=20):
        self.scene = scene
        self.camera = camera
        self.max_depth = max_depth
        self.pixel_samples = pixel_samples  # for antialiasing. number of rays per pixel.
        self.num_U_samples = num_U_samples  # number of samples for the first bounce.

    def render(self):
        # w columns X h rows. each has a list of 3 zeroes. each pixel initialized to 0,0,0.
        img = np.zeros((self.camera.img_height, self.camera.img_width, 3))
        for w in range(0, self.camera.img_width):
            for h in range(0, self.camera.img_height):
                color = np.zeros(3)  # r,g,b = 0
                for _ in range(0, self.pixel_samples):
                    # create a ray from camera origin that goes through pixel w,h.
                    ray = self.camera.gen_rand_ray(pixelx=w, pixely=h)
                    # needs to return color value as np.array rgb [0,1].
                    color = color + self.compute_sample(ray, depth=0)
                img[h, w, :] = np.clip(color / self.pixel_samples, 0, 1)
        plt.imsave('pics\\UV.png', img)

    # (noam) consider making these helper functions private
    def compute_sample(self, ray, depth):
        if depth == self.max_depth:
            return np.zeros(3)
        # ask scene to find the closest intersection point.
        obj_material, hit_position, hit_norm = self.scene.find_closest_intersection(ray)
        # after finding the hit_obj. need to produce the resulting ray which depends on: material, hit position, hit_norm.
        if hit_position is None:  # if ray didn't hit anything, return environment color.
            return self.scene.environment_color

        if depth == 0:  # on first hit, send u number of rays.
            num_U_samples = self.num_U_samples
        else:
            num_U_samples = 1

        color_result = np.zeros(3)
        for u in range(num_U_samples):
            # send new rays depending on material properties.
            color_result = color_result + self.send_new_ray(ray, obj_material, hit_position, hit_norm, u, depth)

        total_ray_emission = obj_material.emission + color_result / num_U_samples

        return total_ray_emission

    def send_new_ray(self, ray, obj_material, hit_position, hit_norm, u, depth):
        # depending on material properties: will send new ray either as cone sample or as hemisphere sample.
        # split into 3 cases: reflection, diffuse, refraction. use probability to navigate the rays based on properties.
        # use the law of large numbers to simplify and instead of calculating all the above, just send one ray.

        # if ray.norm_dir.vec_dot(
        #         hit_norm) > 0:  # ray direction should be opposite of hit objects normal unless refraction.
        #     hit_norm = -hit_norm
        #     inside = True

        # generate a random p value between 0-1
        p = random.uniform(0, 1)

        # 1st case: reflective material.
        if obj_material.reflection > p:  # send reflective ray. might send u*v ray so need to randomize the dir.
            # TODO add coneAngle variable to adjust for size of the cone.
            # calculation of direction of reflected ray.
            temp = hit_norm.vec_mul(2 * ray.norm_dir.vec_dot(hit_norm))
            reflect_dir = ray.norm_dir.vec_sub(temp)
            reflect_dir = reflect_dir.vec_normalize()
            # on first hit: add/reduce x,y,z by 0.05 of normalized reflected ray to create randomness.
            if depth == 0:
                rnd = random.uniform(-0.05, 0.05)
                reflect_dir.x += rnd
                reflect_dir.y += rnd
                reflect_dir.z += rnd
            return self.compute_sample(ray=Ray(hit_position, reflect_dir), depth=depth + 1)

        # 2nd case: transparent material.
        elif obj_material.transparency > 0:
            # obj_material.refraction_ind  # TODO add refraction code.
            print("does not compute")
            pass

        # 3rd case: diffuse material.
        else:
            diffuse_dir = hemisphere_sample2(hit_norm)
            return obj_material.color * self.compute_sample(ray=Ray(hit_position, diffuse_dir), depth=depth + 1)


def hemisphere_sample(hit_norm):
    # create coordinate system with hit_norm - vec1 and vec2 are complimentary orthogonal bases.
    # https://www.scratchapixel.com/lessons/3d-basic-rendering/global-illumination-path-tracing/global-illumination-path-tracing-practical-implementation
    if abs(hit_norm.x) > abs(hit_norm.y):
        vec_nt = Vec3D(hit_norm.z, 0, -hit_norm.x).vec_normalize()
    else:
        vec_nt = Vec3D(0, -hit_norm.z, hit_norm.y).vec_normalize()
    vec_nb = hit_norm.vec_cross(vec_nt)

    # sample randomly in a sphere.
    rnd1, rnd2 = random.uniform(0, 1), random.uniform(0, 1)
    sinTheta = math.sqrt(1 - (rnd1 * rnd1))
    phi = 2 * math.pi * rnd2
    x = sinTheta * math.cos(phi)
    y = 1 - rnd1
    z = sinTheta * math.sin(phi)
    rnd_vec = Vec3D(x, y, z)

    # transform rnd_vec to local coordinate system of hit_norm.
    ray_dir = Vec3D(rnd_vec.x * vec_nb.x + rnd_vec.y * hit_norm.x + rnd_vec.z * vec_nt.x,
                    rnd_vec.x * vec_nb.y + rnd_vec.y * hit_norm.y + rnd_vec.z * vec_nt.y,
                    rnd_vec.x * vec_nb.z + rnd_vec.y * hit_norm.z + rnd_vec.z * vec_nt.z)
    return ray_dir


def hemisphere_sample2(hit_norm):
    if abs(hit_norm.x) > abs(hit_norm.y):
        vec_nt = Vec3D(hit_norm.z, 0, -hit_norm.x).vec_normalize()
    else:
        vec_nt = Vec3D(0, -hit_norm.z, hit_norm.y).vec_normalize()
    vec_nb = hit_norm.vec_cross(vec_nt)

    # sample randomly in a sphere.
    rnd1, rnd2 = random.uniform(0, 1), random.uniform(0, 1)
    theta = 2 * math.pi * rnd2
    radius_squared = rnd1
    radius = math.sqrt(radius_squared)
    x = radius * math.cos(theta)
    y = math.sqrt(1-radius_squared)
    z = radius * math.sin(theta)
    rnd_vec = Vec3D(x, y, z)

    # transform rnd_vec to local coordinate system of hit_norm.
    ray_dir = Vec3D(rnd_vec.x * vec_nb.x + rnd_vec.y * hit_norm.x + rnd_vec.z * vec_nt.x,
                    rnd_vec.x * vec_nb.y + rnd_vec.y * hit_norm.y + rnd_vec.z * vec_nt.y,
                    rnd_vec.x * vec_nb.z + rnd_vec.y * hit_norm.z + rnd_vec.z * vec_nt.z)
    return ray_dir
