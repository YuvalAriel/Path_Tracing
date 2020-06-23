import math
import sys
import numpy as np
import matplotlib.pyplot as plt
import time

from Vec3D import Vec3D
from Scene import Scene
from Sphere import Sphere
from Material import Material
from Ray import Ray
from Camera import Camera
from Renderer import Renderer
from Plane_Disk import Disk
from Plane_Disk import Plane

epsilon = 0.000001

red = [1, 0, 0]
green = [0, 1, 0]
blue = [0, 0, 1]
black = [0, 0, 0]
white = [1, 1, 1]

bright_light = Material(white, emission=np.ones(3) * 5)

sphere1 = Sphere(center=(-6, 0, -7), material=Material(red))
sphere2 = Sphere(center=(0, -2, -10), radius=3, material=Material(green, reflection=0.9))
sphere3 = Sphere(center=(6, 0, -7), material=Material(blue))

light1 = Sphere(center=(0, 14, -5), radius=4, material=bright_light)
# light2 = Sphere(center=(0, -10, -5), radius=5, material=bright_light)

plane1 = Plane((1, -1, 0), (0, 0, 0))

disk1 = Disk((0, 0, -1), (5, 5, -8))

# scene = Scene(disk1, sphere1)
# scene = Scene(sphere1, sphere3, sphere2, light1)
# scene = Scene(sphere1)
scene = Scene(plane1, light1)

cam = Camera(200, 150)  # cam_center=(0.5,0.5,0)
# cam = Camera(400, 300)
# cam = Camera(600, 450)
# cam = Camera(800, 600)
# cam = Camera(1000, 750)

renderer = Renderer(scene, cam, max_depth=2, pixel_samples=5, num_U_samples=10)
tic = time.perf_counter()
renderer.render()
tc = time.perf_counter()

# import winsound
# duration = 1000  # milliseconds
# freq = 1440  # Hz
# winsound.Beep(freq, duration)

print(f" Runtime {tc - tic:0.4f} seconds")
print(f" Runtime {(tc - tic)/60:0.4f} mins")
