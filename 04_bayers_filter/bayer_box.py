#!/usr/bin/env python

import numpy as np
from random import randint
from PIL import Image

def print3darray(array):
    for array_row in array:
        print(array_row.tolist())

def convert_to_box(img, box_size):
    height, width, temp = img.shape
    img_box = np.zeros((height*box_size, width*box_size, 3), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
                img_box[i*box_size: i*box_size+(box_size),
                        j*box_size: j*box_size+(box_size)] = img[i, j]
    return img_box

# generate a random image
#73 128
height = 18
width = 32
box_size = 20
print('Height: {}, Width: {}, Box Size: {}'.format(height, width, box_size))
img = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        if i%2 == 0:
            if j%2 == 0:
                img[i, j, 0] = randint(0, 255)
            else:
                img[i, j, 1] = randint(0, 255)
        else:
            if j%2 == 0:
                img[i, j, 1] = randint(0, 255)
            else:
                img[i, j, 2] = randint(0, 255)


# print the updated box
print('bayer filtered image captured:')
print3darray(img)
img_box = convert_to_box(img, box_size)
# print3darray(img_box)
# save the random image
# Image.fromarray(img, 'RGB').save('rgb.png')
Image.fromarray(img_box, 'RGB').save('rgb_box.png')

# DEMOSAIC
img_demosaic = np.zeros(img.shape, dtype=np.uint8)
# we go from 1 to height-2
# since we leave off the edges
# have to use np.uint16 because 8 bit leads to overflow
for i in range(1, height-1):
    for j in range(1, width-1):
        if i%2 == 0:
            if j%2 == 0:
                # ceter is red
                r = img[i, j]
                g = (np.uint16(img[i-1, j]) + np.uint16(img[i+1, j]) + np.uint16(img[i, j-1]) + np.uint16(img[i, j+1]))/4
                b = (np.uint16(img[i-1, j-1]) + np.uint16(img[i-1, j+1]) + np.uint16(img[i+1, j-1]) + np.uint16(img[i+1, j+1]))/4
            else:
                # center is green
                r = (np.uint16(img[i, j-1]) + np.uint16(img[i, j+1]))/2
                g = img[i, j]
                b = (np.uint16(img[i-1, j]) + np.uint16(img[i+1, j]))/2
        else:
            if j%2 == 0:
                # centre is green
                r = (np.uint16(img[i-1, j]) + np.uint16(img[i+1, j]))/2
                g = img[i, j]
                b = (np.uint16(img[i, j-1]) + np.uint16(img[i, j+1]))/2
            else:
                # centre is blue
                r = (np.uint16(img[i-1, j-1]) + np.uint16(img[i-1, j+1]) + np.uint16(img[i+1, j-1]) + np.uint16(img[i+1, j+1]))/4
                g = (np.uint16(img[i-1, j]) + np.uint16(img[i+1, j]) + np.uint16(img[i, j-1]) + np.uint16(img[i, j+1]))/4
                b = img[i, j]
        img_demosaic[i, j] = r + g + b

# save demosaiced image
print3darray(img_demosaic)
img_demosaic_box = convert_to_box(img_demosaic, box_size)
Image.fromarray(img_demosaic_box, 'RGB').save('demosaic_box.png')
