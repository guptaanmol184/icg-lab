import pygame, sys
import math as m

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
print('Enter the length of the line')
length = int(input())
print('Enter the angle with the x axis')
angle = int(input())

# Levy's C Curve
#
# Parameters:
# x, y -> starting points
# length -> length of the line
# n -> number of iterations
def levy_c_curve(x, y, l, alpha, n):
    if n > 0:
        l_new = l/(2**(1/2))
        levy_c_curve(x, y, l_new, alpha+45, n-1)
        levy_c_curve((x + l_new * m.cos(m.radians(45 + alpha))),
                     (y + l_new * m.sin(m.radians(45 + alpha))), l_new, alpha-45, n-1)
    else:
        x_end = int(x + (l * m.cos(m.radians(alpha))))
        y_end = int(y + (l * m.sin(m.radians(alpha))))
        print('End:({},{})'.format(x_end, y_end))
        pygame.draw.line(screen, green, [x, y], [x_end, y_end], 1)
        pygame.display.flip()

# draw origin
pygame.draw.line(screen, red, [300, 150], [300, 150], 1)
pygame.display.flip()
pygame.time.delay(1500)

levy_c_curve(300, 150, length, angle, itr_count)

pygame.display.flip()
pygame.time.delay(2500)

# hang indefinately
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
