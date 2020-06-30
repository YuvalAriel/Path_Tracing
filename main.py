import numpy as np
import time

from Scene import Scene
from Sphere import Sphere
from Material import Material
from Camera import Camera
from Renderer import Renderer
from Plane_Disk import Disk
from Plane_Disk import Plane

red = [1, 0, 0]
green = [0, 1, 0]
blue = [0, 0, 1]
black = [0, 0, 0]
white = [1, 1, 1]

bright_light = Material(white, emission=np.ones(3) * 10)

sphere1 = Sphere(center=(-3, -0.5, -5), radius=1.5, material=Material(red, reflection=0))
sphere2 = Sphere(center=(2, -1, -4), radius=1, material=Material(blue, reflection=0))
sphere3 = Sphere(center=(1, 1, -8), radius=3, material=Material(green, reflection=0))

light1 = Sphere(center=(0, 14, -3), radius=4, material=bright_light)

plane1 = Plane((0, 1, 0), (0, -2, 0), material=Material([0.2, 0.2, 0.2], reflection=0))

disk1 = Disk((0, 0, -1), (5, 5, -8))

scene = Scene(light1, plane1, sphere1, sphere2, sphere3)

cam = Camera(120, 90)
# cam = Camera(400, 300)
# cam = Camera(600, 450)
# cam = Camera(800, 600)
# cam = Camera(1000, 750)

renderer = Renderer(scene, cam, max_depth=2, pixel_samples=3, num_d0_samples=5)  # low-quality rendering
# renderer = Renderer(scene, cam, max_depth=4, pixel_samples=4, num_d0_samples=30)  # high-quality rendering

tic = time.perf_counter()
renderer.render()
tc = time.perf_counter()

# import winsound
# duration = 1000  # milliseconds
# freq = 1440  # Hz
# winsound.Beep(freq, duration)

print(f" Runtime {tc - tic:0.4f} seconds")
print(f" Runtime {(tc - tic) / 60:0.1f} mins")
