import numpy as np
import matplotlib.pyplot as plt


w = 400
h = 300

img = np.zeros((h, w, 3))  # h rows X w columns. each has a list of 3 zeroes. each pixel initialized to 0,0,0.

color = np.zeros(3)

img[2,3, :] = [0.5,0.6,0.7]
img[7,10, :] = [0.2,0.2,0.3]
img[200,300, :] = [1,0,0]
img[50,100, :] = [0,1,0]
# img[h, w, :] = np.clip(color, 0, 1)  # https://numpy.org/doc/1.18/reference/generated/numpy.clip.html

plt.imsave('path.png', img)
