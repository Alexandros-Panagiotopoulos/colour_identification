import cv2
import webcolors
from collections import Counter
from matplotlib import colors

reduced_x_pixels = 100
reduced_y_pixels = 100


def get_closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS21_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def calculate_dominant_colour_of_all_pixels(image):
    colours = []
    for i in range(reduced_x_pixels-1):
        for j in range(reduced_y_pixels-1):
            colours.append(get_closest_colour(image[j,i]))
    counter = Counter(colours)
    return max(counter, key=counter.get)


image = cv2.imread('images/colourful2.png')
image = cv2.resize(image, (reduced_x_pixels, reduced_y_pixels))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
dominant_colour = calculate_dominant_colour_of_all_pixels(image)
print(webcolors.name_to_rgb(dominant_colour), dominant_colour)

# requested_colour = image[2, 5]
# print(get_closest_colour(requested_colour))
# print("The type of this input is {}".format(type(image)))
# print("Shape: {}".format(image.shape))
# print(image[50, 50])