#!/usr/bin/env python

import numpy as np
from PIL import Image

# generate a random image
#73 128
height = 10
width = 10
box_size = 50
img = np.random.randint(0, 256, (height, width), np.uint8)
img_box = np.zeros((height * box_size, width * box_size, 3), dtype=np.uint8)
# generate img_box from img
for i in range(height):
    for j in range(width):
        if i%2 == 0 and j%2 == 0:
            # Oth row and 0th column == R
            img_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    0] = img[i, j]
        elif i%2 == 0 and j%2 == 1:
            # 0th row and 1st column == G
            img_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    1] = img[i, j]
        elif i%2 == 1 and j%2 == 0:
            # 1st row and 0th column == G
            img_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    1] = img[i, j]
        elif i%2 == 1 and j%2 == 1:
            # 1st row and 1st column == B
            img_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    2] = img[i, j]

# remove edge rows for display
img_box_noedge = img_box[box_size:-box_size, box_size:-box_size, :]
# save the random image
Image.fromarray(img_box, 'RGB').save('rgb_edge.png')
Image.fromarray(img_box_noedge, 'RGB').save('rgb.png')

# remove the edges
img_demosaic = img[1:-1, 1:-1]
new_height , new_width = img_demosaic.shape
img_demosaic_box = np.zeros((new_height * box_size, new_width * box_size, 3), dtype=np.uint8)

# do demosaicing
for i in range(new_height):
    for j in range(new_width):
        if i%2 == 0 and j%2 == 0:
            # 1st row and 1st column of original = B
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    0] = np.uint8((img[i-1, j-1] + img[i-1, j+1] + img[i+1, j-1] + img[i+1, j+1])/4)
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    1] = np.uint8((img[i-1, j] + img[i, j-1] + img[i, j+1] + img[i+1, j])/4)
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    2] = img[i, j]
        elif i%2 == 0 and j%2 == 1:
            # 1st row and 2nd column of original = G
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    0] = np.uint8((img[i-1, j] + img[i+1, j])/2)
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    1] = img[i, j]
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    2] = np.uint8((img[i, j-1] + img[i, j+1])/2)
        elif i%2 == 1 and j%2 == 0:
            # 2nd row and 1st column of original = G
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    0] = np.uint8((img[i, j-1] + img[i, j+1])/2)
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    1] = img[i, j]
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    2] = np.uint8((img[i-1, j] + img[i+1, j])/2)
        elif i%2 == 1 and j%2 == 1:
            # 2nd row and 2nd column of original = R
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    0] = img[i, j]
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    1] = np.uint8((img[i-1, j] + img[i+1, j] + img[i, j-1] + img[i, j+1])/4)
            img_demosaic_box[i*box_size: i*box_size+(box_size-1),
                    j*box_size: j*box_size+(box_size-1),
                    2] = np.uint8((img[i-1, j-1] + img[i-1, j+1] + img[i+1, j-1] + img[i+1, j+1])/4)

# save demosaiced image
Image.fromarray(img_demosaic_box, 'RGB').save('demosaic.png')
