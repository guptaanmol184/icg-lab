#!/usr/bin/env python

import sys
import pygame
import math as m

# Set screen props
size = width, height = 600, 340

# define some colors
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0
blue = 0, 0, 255
light_blue = 12, 50, 200
bg_color = 32, 32, 32

# initialize the screen
screen = pygame.display.set_mode(size)
screen.fill(bg_color)
pygame.display.update()

class Stick:

    color = 20, 50, 150
    head_radius = 30
    head_center_to_shoulder = 60
    shoulder_to_legs = 80
    thick = 2
    h_len = 40
    l_len = 40
    h_angle = -30 # in degrees
    l_angle = 30

    def __init__(self, head_x, head_y):
        self.head_x = head_x
        self.head_y = head_y

    def update_pos(self, head_x, head_y):
        self.head_x = head_x
        self.head_y = head_y

    def update_angle(self, h_angle, l_angle):
        self.h_angle = h_angle
        self.l_angle = l_angle

    def calculate(self):
        # shoulder
        self.shoulder_x = self.head_x
        self.shoulder_y = self.head_y + self.head_center_to_shoulder
        #legs start
        self.legs_start_x = self.head_x
        self.legs_start_y = self.shoulder_y + self.shoulder_to_legs
        # right hand
        self.r_hand_end_x = (self.shoulder_x) + self.h_len * (m.cos(m.radians(self.h_angle)))
        self.r_hand_end_y = (self.shoulder_y) + self.h_len * (m.sin(m.radians(self.h_angle)))
        # left hand
        self.l_hand_end_x = (self.shoulder_x) + self.h_len * (m.cos(m.radians(180-self.h_angle)))
        self.l_hand_end_y = (self.shoulder_y) + self.h_len * (m.sin(m.radians(180-self.h_angle)))
        # right leg
        self.r_leg_end_x = (self.legs_start_x) + self.l_len * (m.cos(m.radians(self.l_angle)))
        self.r_leg_end_y = (self.legs_start_y) + self.l_len * (m.sin(m.radians(self.l_angle)))
        # left leg
        self.l_leg_end_x = (self.legs_start_x) + self.l_len * (m.cos(m.radians(180-self.l_angle)))
        self.l_leg_end_y = (self.legs_start_y) + self.l_len * (m.sin(m.radians(180-self.l_angle)))


    def draw(self):
        # clear screen
        screen.fill(bg_color)
        pygame.display.update()
        # calculate new values
        self.calculate()
        # head
        pygame.draw.circle(screen, self.color, (self.head_x, self.head_y), self.head_radius)
        # head to legs
        pygame.draw.line(screen, self.color, (self.head_x, self.head_y),
                                            (self.legs_start_x, self.legs_start_y), self.thick)
        # draw hand right
        pygame.draw.line(screen, self.color, (self.shoulder_x, self.shoulder_y),
                                            (self.r_hand_end_x, self.r_hand_end_y), self.thick)
        # draw hand left
        pygame.draw.line(screen, self.color, (self.shoulder_x, self.shoulder_y),
                                            (self.l_hand_end_x, self.l_hand_end_y), self.thick)
        # draw leg right
        pygame.draw.line(screen, self.color, (self.legs_start_x, self.legs_start_y),
                                            (self.r_leg_end_x, self.r_leg_end_y), self.thick)
        # draw leg left
        pygame.draw.line(screen, self.color, (self.legs_start_x, self.legs_start_y),
                                            (self.l_leg_end_x, self.l_leg_end_y), self.thick)
        pygame.display.update()

if __name__ == '__main__':

    delay = 20 # delay in milliseconds

    stickman = Stick(300, 70)

    for i in range(30, 60):
        pygame.time.wait(delay)
        stickman.update_angle(-i, i)
        stickman.draw()
    for i in range(60, 30, -1):
        pygame.time.wait(delay)
        stickman.update_angle(-i, i)
        stickman.draw()
    for i, j in zip(range(30, 0, -1), range(30, 60)):
        pygame.time.wait(delay)
        stickman.update_angle(-i, j)
        stickman.draw()
    
    # 300, 70
    for j in range(1):
        for i in range(300, 250, -1):
            pygame.time.wait(delay)
            stickman.update_pos(i, 70)
            stickman.draw()
        for i in range(250, 350):
            pygame.time.wait(delay)
            stickman.update_pos(i, 70)
            stickman.draw()
        for i in range(350, 250, -1):
            pygame.time.wait(delay)
            stickman.update_pos(i, 70)
            stickman.draw()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
