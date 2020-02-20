import cv2
import webcolors
from collections import Counter

predefined_colours = [
    {"key": "black", "red": 0, "green": 0, "blue": 0},
    {"key": "white", "red": 255, "green": 255, "blue": 255},
    {"key": "grey", "red": 85, "green": 85, "blue": 85},
    {"key": "Navy", "red": 0, "green": 0, "blue": 128},
    {"key": "teal", "red": 0, "green": 128, "blue": 128},
    {"key": "silver", "red": 192, "green": 192, "blue": 192},
]
reduced_x_pixels = 100
reduced_y_pixels = 100
max_dist_squared = 160000
match_factor = 0.1


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
    if min_dist > (max_dist_squared * match_factor):
        return None
    return min_colours[min_dist]


def calculate_dominant_colour_of_all_pixels(image):
    colours = []
    for i in range(reduced_x_pixels-1):
        for j in range(reduced_y_pixels-1):
            colours.append(get_closest_colour_from_predefined_colours(image[j,i]))
    counter = Counter(colours)
    return max(counter, key=counter.get)



image = cv2.imread('images/test-sample-teal.png')
image = cv2.resize(image, (reduced_x_pixels, reduced_y_pixels))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
dominant_colour = calculate_dominant_colour_of_all_pixels(image)
print(dominant_colour)
# print(image[50, 50:55])