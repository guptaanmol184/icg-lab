#!/usr/bin/env python

import numpy as np
from PIL import Image

# generate a random image
height = 73
width = 128
box_size = 10
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

# save the random image
Image.fromarray(img_box, 'RGB').save('rgb.png')

# do demosaicing
