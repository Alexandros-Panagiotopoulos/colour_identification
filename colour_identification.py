import matplotlib.pyplot as plt
import numpy as np
import cv2
import webcolors


def get_closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS21_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


image = cv2.imread('images/test-sample-teal.png')
image = cv2.resize(image, (1200, 600))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

requested_colour = image[500, 1000]
print(get_closest_colour(requested_colour))

# print("The type of this input is {}".format(type(image)))
# print("Shape: {}".format(image.shape))
# print(image[1000, 1000:1010])