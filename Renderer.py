import math
import numpy as np
import matplotlib.pyplot as plt
import random

from Vec3D import Vec3D
from Ray import Ray


class Renderer:
    def __init__(self, scene, camera, max_depth=4, pixel_samples=4, num_d0_samples=30):
        self.scene = scene
        self.camera = camera
        self.max_depth = max_depth
        self.pixel_samples = pixel_samples  # for anti-aliasing. number of rays per pixel.
        self.num_d0_samples = num_d0_samples  # number of samples for the first bounce where depth=0.

    def render(self):
        img = np.zeros((self.camera.img_height, self.camera.img_width, 3))  # init img to hightXwidth of (0,0,0) rgb.
        for w in range(0, self.camera.img_width):
            if w % (self.camera.img_width / 100) == 0:  # print out execution progress
                print(w * 100 / self.camera.img_width, "% completed")
            for h in range(0, self.camera.img_height):
                color = np.zeros(3)
                # sum and average color of rays passing through pixel [h,w] and record to img.
                for _ in range(0, self.pixel_samples):
                    ray = self.camera.gen_rand_ray(x_pixel=w, y_pixel=h)  #
                    color = color + self._compute_sample(ray, depth=0, ref_depth=0)
                img[h, w, :] = np.clip(color / self.pixel_samples, 0, 1)
        plt.imsave('pics\\picture.png', img)

    def _compute_sample(self, ray, depth, ref_depth):
        if (depth + ref_depth) == self.max_depth:
            return np.zeros(3)
        # ask scene to find the closest intersection point and record material, hit position, hit_norm for reflected ray
        obj_material, hit_position, hit_norm = self.scene.find_closest_intersection(ray)
        if hit_position is None:  # if ray didn't hit anything, return black.
            return [0.274, 0.576, 0.945]

        # collect color from following the path of the ray. send new rays depending on material properties.
        color_from_ray = self._send_new_ray(ray, obj_material, hit_position, hit_norm, depth, ref_depth)

        # total color at hit_position is color from path of ray and emission of the hit_object itself.
        total_ray_emission = obj_material.emission + color_from_ray

        return total_ray_emission

    def _send_new_ray(self, ray, obj_material, hit_position, hit_norm, depth, ref_depth):
        # depending on material properties: will send new ray either as reflected sample or as hemisphere sample.
        # split into 3 cases: reflection, refraction and diffuse.
        # use the law of large numbers to simplify. If an object has multiple properties, send just one ray

        # generate a random p value between 0-1
        p = random.uniform(0, 1)

        # 1st case: reflective material.
        if obj_material.reflection > p:  # send reflective ray.
            # TODO add coneAngle variable to adjust for size of the cone.
            # calculation of direction of reflected ray.
            temp = hit_norm.vec_mul(2 * ray.norm_dir.vec_dot(hit_norm))
            reflect_dir = ray.norm_dir.vec_sub(temp)
            reflect_dir = reflect_dir.vec_normalize()
            # on first hit: add/reduce x,y,z by 0.05 of normalized reflected ray to create randomness.
            # if depth == 0:
            #     rnd = random.uniform(-0.02, 0.02)
            #     reflect_dir.x += rnd
            #     reflect_dir.y += rnd
            #     reflect_dir.z += rnd
            return self._compute_sample(ray=Ray(hit_position, reflect_dir), depth=depth, ref_depth=ref_depth + 1)

        # 2nd case: transparent material.
        elif obj_material.transparency > 0:
            #  TODO add refraction code.
            # if ray.norm_dir.vec_dot(hit_norm) > 0:
            # ray direction should be opposite of hit objects normal unless refraction.
            #     hit_norm = -hit_norm
            print("does not compute")
            pass

        # 3rd case: diffuse material.
        else:
            # on first hit of a non reflective material, send d0 number of rays. otherwise send 1 ray.
            num_d0_samples = self.num_d0_samples if depth == 0 else 1

            # average color contribution of all hemisphere samples.
            color = np.zeros(3)
            for _ in range(num_d0_samples):
                diffuse_dir = _hemisphere_sample(hit_norm)
                color += obj_material.color * self._compute_sample(Ray(hit_position, diffuse_dir), depth + 1, ref_depth)
            return color / num_d0_samples


def _hemisphere_sample(hit_norm):
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
    y = math.sqrt(1 - radius_squared)
    z = radius * math.sin(theta)
    rnd_vec = Vec3D(x, y, z)

    # transform rnd_vec to local coordinate system of hit_norm.
    ray_dir = Vec3D(rnd_vec.x * vec_nb.x + rnd_vec.y * hit_norm.x + rnd_vec.z * vec_nt.x,
                    rnd_vec.x * vec_nb.y + rnd_vec.y * hit_norm.y + rnd_vec.z * vec_nt.y,
                    rnd_vec.x * vec_nb.z + rnd_vec.y * hit_norm.z + rnd_vec.z * vec_nt.z)
    return ray_dir
