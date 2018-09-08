import pygame, sys
import math

# Set screen props
size = width, height = 640, 360

# define origin
origin = 225, 130

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

# Koch Snoflake Edge
# Draws a koch snowflake edge recursively 
# Parameters:
# (x0, y0) -> starting point
# (x1, y1) -> ending point
# n -> number iterations
# (m, n) is the point of the tip of the equilateral triangle
#           a               b                c
#   |---------------|-----------------|----------------|
# (x0,y0)       (p0,q0)           (p1, q1)         (x1, y1)
def koch_snowflake_edge(x0, y0, length, alpha, itr):

    x1 = x0 + length * math.cos(math.radians(alpha))
    y1 = y0 + length * math.sin(math.radians(alpha))

    if itr > 0:
        # calculate some values
        # length is the distance between (x0, y0) and (x1, y1)
        p0 = x0 + (length/3) * math.cos(math.radians(alpha))
        q0 = y0 + (length/3) * math.sin(math.radians(alpha))
        p1 = x0 + 2 * (length/3) * math.cos(math.radians(alpha))
        q1 = y0 + 2 * (length/3) * math.sin(math.radians(alpha))
        m = p0 + (length/3)*(math.cos(math.radians(alpha + 60)))
        n = q0 + (length/3)*(math.sin(math.radians(alpha + 60)))
        # draw a
        koch_snowflake_edge(x0, y0, length/3, alpha, itr-1)
        # draw c
        koch_snowflake_edge(p1, q1, length/3, alpha, itr-1)
        # draw b
        koch_snowflake_edge(p0, q0, length/3, alpha+60, itr-1)
        koch_snowflake_edge(m, n, length/3, alpha-60, itr-1)
    else:
        pygame.draw.line(screen, light_blue, [x0, y0], [x1, y1], 1)
        pygame.display.update()

def draw_koch_snowflake(itr_count):
    # define origin
    x, y = origin
    length = 150
    # draw first edge from origin 
    koch_snowflake_edge(x, y, length, 60, itr_count)
    # update strting point for second edge
    x = x + length * math.cos(math.radians(60))
    y = y + length * math.sin(math.radians(60))
    koch_snowflake_edge(x, y, length, -60, itr_count)
    # update starting point for third edge
    x = x + length * math.cos(math.radians(-60))
    y = y + length * math.sin(math.radians(-60))
    koch_snowflake_edge(x, y, length, 180, itr_count)

if __name__ == '__main__':
    # get input
    itr_count = int(input('Enter the number of iterations to undergo: ').strip())

    # draw origin
    pygame.draw.line(screen, red, origin, origin, 1)
    pygame.display.update()
    pygame.time.delay(1000)

    # draw koch snowflake
    draw_koch_snowflake(itr_count)

    pygame.display.update()

    # hang indefinately untill user quits
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

