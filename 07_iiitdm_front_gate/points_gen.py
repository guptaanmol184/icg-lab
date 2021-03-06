#!/usr/bin/env python

# flag = 0 -> behave as strip
# flag = 1 -> behave as loop
def common(flag):

    f = open('points.txt', 'r')
    lines = f.readlines()

    # check boundary case
    # don't do anything if we do not have enough points
    # the user probably click it by mistake
    if len(lines) <= 1:
        return

    # find first line without draw or block
    index = 0
    for i in range(len(lines)):
        if 'block' not in lines[i] and 'draw' not in lines[i]:
            index = i
            break

    old_lines = lines[:index]
    new_lines = []
    # add a comment for the new block
    new_lines.append('#block\n')
    # generate the block using points
    for i in range(index, len(lines)-1):
        x0, y0 = map(int, lines[i].strip().split())
        x1, y1 = map(int, lines[i+1].strip().split())
        new_lines.append('draw_line(({:4d}, {:4d}), ({:4d}, {:4d}))\n'.format(x0, y0, x1, y1))
    
    # close the loop if flag is 1
    if flag == 1:
        start_x, start_y = map(int, lines[index].strip().split())
        end_x, end_y = map(int, lines[len(lines)-1].strip().split())
        new_lines.append('draw_line(({:4d}, {:4d}), ({:4d}, {:4d}))\n'.format(end_x, end_y, start_x, start_y))

    lines = old_lines + new_lines
    f = open('points.txt','w')
    f.writelines(lines)
    f.close()

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # save the clicked points to a file
        f = open('points.txt', 'a')
        print('Writing ({:4d}, {:4d}) to file.'.format(x, y))
        f.write('{:4d} {:4d}\n'.format(x, y))
        f.close()
    if event == cv2.EVENT_RBUTTONDOWN:
        # # delete operation for points
        # # undo last selected point
        # f = open('points.txt')
        # lines = f.readlines()
        # f.close()
        # if len(lines) > 0:
        #     f = open('points.txt','w')
        #     f.writelines([item for item in lines[:-1]])
        #     x, y = lines[-1].strip().split()
        #     print('Deleting point ({:4d}, {:4d})'.format(int(x), int(y)))
        #     f.close()
        # change this to line drawing
        # use this to create a strip for pygame to draw with t
        common(0)
    if event == cv2.EVENT_MBUTTONDOWN:
        common(1)

import cv2
img = cv2.imread('front_2.jpg')
cv2.imshow('FRONT GATE', img)
cv2.setMouseCallback('FRONT GATE', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# from matplotlib import pyplot as plt

# img = cv2.imread('front_2.jpg')
# plt.imshow(img)
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()
