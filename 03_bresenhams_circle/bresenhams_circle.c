#include <graphics.h>
#include <stdio.h>

void bresenham_circle(int x, int y, int radius);

int main(void)
{
	int gd = DETECT, gm;
	initgraph(&gd, &gm, NULL);

	bresenham_circle(200, 200, 100);

	getch();
	closegraph();
	
	return 0;
}

// Bresenham's Circle Drawing Algorithm
void bresenham_circle(int center_x, int center_y, int radius)
{
	// draw (0,r), (0,-r), (r,0), (-r,0)
	putpixel(center_x, center_y+radius, WHITE);
	putpixel(center_x, center_y-radius, WHITE);
	putpixel(center_x+radius, center_y, WHITE);
	putpixel(center_x-radius, center_y, WHITE);

	int decesion_param;
	decesion_param = 1-radius;

	int x, y;
	for(x=1, y=radius; x <=y; ++x)
	{
		if(decesion_param >=0 )
		{
			y = y-1;
			decesion_param += 2*(x-y) + 5;
		}
		else
			decesion_param += 2*x + 3;

		// draw pixels using symmetry
		putpixel(center_x+x, center_y+y, WHITE);
		putpixel(center_x-x, center_y+y, WHITE);
		putpixel(center_x+x, center_y-y, WHITE);
		putpixel(center_x-x, center_y-y, WHITE);

		putpixel(center_x+y, center_y+x, WHITE);
		putpixel(center_x-y, center_y+x, WHITE);
		putpixel(center_x+y, center_y-x, WHITE);
		putpixel(center_x-y, center_y-x, WHITE);

	}
}
