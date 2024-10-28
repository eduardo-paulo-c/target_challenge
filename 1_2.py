import cv2
import numpy as np

# Load image
image = cv2.imread('meteor_challenge_01.png')

# Pure red
low_pure_red = np.array([0, 0, 255])   
high_pure_rede = np.array([0, 0, 255]) 

# Pure white
low_pure_white = np.array([255, 255, 255])   
high_pure_white = np.array([255, 255, 255])

# Creating a mask that contains the pixels within the color range
red = cv2.inRange(image, low_pure_red, high_pure_rede)
white = cv2.inRange(image, low_pure_white, high_pure_white)

# Count the pixels whit the defined color
count_red_pixels = cv2.countNonZero(red)
count_white_pixels = cv2.countNonZero(white)

print(f"Number of star: {count_white_pixels}")
print(f"Number of Meteors: {count_red_pixels}")

