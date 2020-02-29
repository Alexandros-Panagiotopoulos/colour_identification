import numpy as np
import cv2
import urllib.request
import webcolors
from collections import Counter
import requests
import ast

with open('predefined_colours.txt', 'r') as file_object:
    predefined_colours = ast.literal_eval(file_object.read())  # read predefined colours as a list of dicts
reduced_x_pixels = 100          #controls the size of the pixels sample that handled and speed of code
reduced_y_pixels = 100
max_dist_squared = 255**2*3     #maximum squared distance between two corners of rgb space
match_factor = 0.02             #the lower the factor the closer match is demanded


def get_closest_colour_from_CSS3_colours(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    min_dist = min(min_colours.keys())
    if min_dist > (max_dist_squared * match_factor):
        return None
    return min_colours[min_dist]


def get_closest_colour_from_predefined_colours(requested_colour):
    min_colours = {}
    for predefined_colour in predefined_colours:
        r_c, g_c, b_c = predefined_colour["red"], predefined_colour["green"], predefined_colour["blue"],
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = predefined_colour["key"]
    min_dist = min(min_colours.keys())
    if min_dist > (max_dist_squared * match_factor):    #if there is no close matched colour it returns None
        return None
    return min_colours[min_dist]


def calculate_dominant_colour_of_all_pixels(image):
    colours = []
    for i in range(reduced_x_pixels-1):
        for j in range(reduced_y_pixels-1):
            colours.append(get_closest_colour_from_predefined_colours(image[j,i]))
    counter = Counter(colours)
    return max(counter, key=counter.get)        #returns the colour with most pixels or None if most pixels has no close matched colour

url = "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-teal.png"
response = urllib.request.urlopen(url)
image = np.asarray(bytearray(response.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
image = cv2.resize(image, (reduced_x_pixels, reduced_y_pixels))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
dominant_colour = calculate_dominant_colour_of_all_pixels(image)
print(dominant_colour)