import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread('images/test-sample-teal.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print("The type of this input is {}".format(type(image)))
print("Shape: {}".format(image.shape))
print(image[1000,1000:1010])