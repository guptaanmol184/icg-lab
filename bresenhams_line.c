#include<stdio.h>
#include<graphics.h>

#define COLOR 2
 
void line_bresenham(int x0, int y0, int x1, int y1)
{
    int delta_x, delta_y, decesion_param, x, y;
 
	// calculate the deltas
    delta_x = x1-x0;
    delta_y = y1-y0;
 
	// initialize the starting point
    x = x0;
    y = y0;
 
	// calculate intial decesion parameter
    decesion_param=2*delta_y-delta_x;
 
	// draw line
    while(x<x1)
    {
        putpixel(x,y,COLOR);
        if(decesion_param>=0)
		{
            y = y+1;
            decesion_param += 2*delta_y-2*delta_x;
        }
        else
            decesion_param += 2*delta_y;

        x = x+1;
    }
}
 
int main()
{
    int gdriver=DETECT, gmode, error, x0, y0, x1, y1;
 
	printf("Assumptions\n"
	       "1. We draw line from left to right.\n"
	       "2. x1 < x2 and y1< y2\n"  
	       "3. Slope of the line is between 0 and 1. "
		   "We draw a line from lower left to upper right.\n");

    printf("Enter co-ordinates of first point: ");
    scanf("%d %d", &x0, &y0);
    printf("Enter co-ordinates of second point: ");
    scanf("%d %d", &x1, &y1);

    initgraph(&gdriver, &gmode, NULL);

	line_bresenham(x0, y0, x1, y1);
 
	getch();
	closegraph();

    return 0;
}
