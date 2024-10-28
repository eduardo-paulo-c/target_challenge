import cv2
import numpy as np

# load image
image = cv2.imread('meteor_challenge_01.png')

# Blue
low_pure_blue = np.array([255, 0, 0]) 
high_pure_blue = np.array([255, 0, 0])

# Red
low_oure_red = np.array([0, 0, 255])
high_pure_red = np.array([0, 0, 255])

# Creating masks
blue = cv2.inRange(image, low_pure_blue, high_pure_blue)
red = cv2.inRange(image, low_oure_red, high_pure_red)

# Geting the coordinates of the blue pixels
blue_coordinates = np.where(blue == 255)

# Creating a final mask for only the red pixels in the columns with blue pixels
vertical_red_mask = np.zeros_like(red)

# Iterate over the columns where there are blue pixels
coluns_whit_blue = blue_coordinates[1]  # Get only the column indexes

for comlumns in np.unique(coluns_whit_blue):  # Get single columns with blue pixels
    # Add the red pixels in this column to the final mask
    vertical_red_mask[:, comlumns] = red[:, comlumns]

# Count vertical red pixels
count_red_pixels = cv2.countNonZero(vertical_red_mask)

print(f"Meteors falling on the Water: {count_red_pixels}")