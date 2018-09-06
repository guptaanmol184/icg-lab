// DDA Line drawing algorithm
// DDA - Digital Differential Algorithm

#include <graphics.h>

#define COLOR 2
void dda_line(int, int, int , int);

int main()
{
	// input points
	int x1, y1, x2, y2;
	printf("DDA Line Drawing Algorithm\n");
	printf("(x, y) denotes (column, row)\n");
	printf("The origin is in the top left corner of the screen.\n");
	printf("Default window size is 640 x 480 pixels.\n");
	printf("The horizontal axis is the x axis.\n");
	printf("The vertical axis is the y axid.\n");
	printf("Enter x1, y1, x2, y2: ");
	scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

	// initialize graphics window
	// default window size in pixels 640 x 480
	int gd = DETECT, gm;
	initgraph(&gd, &gm, NULL);

	// draw line
	dda_line(x1, y1, x2, y2);

	getch();
	closegraph();
	return 0;
}

void dda_line(int x1, int y1, int x2, int y2)
{
	// DDA ALGORITHM
	int delta_x_abs = abs(x2 - x1);
	int delta_y_abs = abs(y2 - y1);
	float x, y;
	float m = (float)(y2-y1) / (x2-x1);

	// CASE 1
	// delta_x_abs >= delta_y_abs
	if( delta_x_abs >= delta_y_abs )
	{
		// we will increment along x axis	
		if(x1 <= x2)
		{
			x = x1;
			y = y1;
			// start at x1
			while(x<=x2)
			{
				putpixel((int) x, (int) y, COLOR);
				x = x + 1;
				y = y + m;
			}
		}	
		else
		{
			x = x2;
			y = y2;
			// start at x2
			while(x<=x1)
			{
				putpixel((int) x, (int) y, COLOR);
				x = x + 1;
				y = y + m;
			}
		}	
	}
	// CASE 2
	// delta_x_abs < delta_y_abs
	else
	{
		// we will increment along y axis	
		if(y1 <= y2)
		{
			y = y1;
			x = x1;
			// start at y1
			while(y<=y2)
			{
				putpixel((int) x, (int) y, COLOR);
				x = x + (1/m);
				y = y + 1;
			}
		}	
		else
		{
			y = y2;
			x = x2;
			// start at y2
			while(y<=y1)
			{
				putpixel((int) x, (int) y, COLOR);
				x = x + (1/m);
				y = y + 1;
			}
		}	
	}
}
