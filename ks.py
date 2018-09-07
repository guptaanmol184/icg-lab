import pygame, sys
import math

# Set screen props
size = width, height = 640, 360

# define some colors
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0

# initialize the screen
screen = pygame.display.set_mode(size)

print('Enter the number of iterations to undergo: ')
itr_count = int(input())
# print('Enter the length of the side')
# length = int(input())


# Koch Snoflake
# Parameters:
# (x0, y0) -> starting point
# (x1, y1) -> ending point
# n -> number iterations
#   |---------------|-----------------|----------------|
# (x0,y0)       (p0,q0)           (p1, q1)         (x1, y1)
def koch_snowflake(x0, y0, length, alpha, itr):
    x1 = x0 + length * math.cos(math.radians(alpha))
    y1 = y0 + length * math.sin(math.radians(alpha))

    if itr > 0:
        #print('call koch snowflake' + str(n))
        # length is the distance between (x0, y0) and (x1, y1)
        p0 = x0 + (length/3) * math.cos(math.radians(alpha))
        q0 = y0 + (length/3) * math.sin(math.radians(alpha))
        p1 = x0 + 2 * (length/3) * math.cos(math.radians(alpha))
        q1 = y0 + 2 * (length/3) * math.sin(math.radians(alpha))
        # (m, n) is the tip of the equilateral triangle in the center
        m = p0 + (length/3)*(math.cos(math.radians(alpha + 60)))
        n = q0 + (length/3)*(math.sin(math.radians(alpha + 60)))
        pygame.draw.line(screen, green, [x0, y0], [p0, q0], 1)
        pygame.display.flip()
        #pygame.time.delay(1000)
        pygame.draw.line(screen, green, [p1, q1], [x1, y1], 1)
        pygame.display.flip()
        #pygae.time.delay(1000)
        koch_snowflake(p0, q0, length/3, alpha+60, itr-1)
        koch_snowflake(m, n, length/3, alpha-60, itr-1)
    else:
        pygame.draw.line(screen, green, [x0, y0], [x1, y1], 1)
        pygame.display.flip()
        #pygame.time.delay(1000)

# draw origin
pygame.draw.line(screen, red, [300, 150], [300, 150], 1)
pygame.display.flip()
pygame.time.delay(1500)

koch_snowflake(300, 150, 100, 60, itr_count)
x = 300 + 100 * math.cos(math.radians(60))
y = 150 + 100 * math.sin(math.radians(60))
koch_snowflake(x, y, 100, -60, itr_count)
x = x + 100 * math.cos(math.radians(-60))
y = y + 100 * math.sin(math.radians(-60))
koch_snowflake(x, y, 100, 180, itr_count)

pygame.display.flip()
pygame.time.delay(2500)

#hang indefinately
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
