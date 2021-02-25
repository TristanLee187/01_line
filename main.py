from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

#octants 1 and 5
draw_line(0, 0, XRES-1, YRES-1, s, c)
draw_line(0, 0, XRES-1, YRES // 2, s, c)
draw_line(XRES-1, YRES-1, 0, YRES // 2, s, c)

#octants 8 and 4
c[BLUE] = 255
draw_line(0, YRES-1, XRES-1, 0, s, c)
draw_line(0, YRES-1, XRES-1, YRES//2, s, c)
draw_line(XRES-1, 0, 0, YRES//2, s, c)

#octants 2 and 6
c[RED] = 255
c[GREEN] = 0
c[BLUE] = 0
draw_line(0, 0, XRES//2, YRES-1, s, c)
draw_line(XRES-1, YRES-1, XRES//2, 0, s, c)

#octants 7 and 3
c[BLUE] = 255
draw_line(0, YRES-1, XRES//2, 0, s, c)
draw_line(XRES-1, 0, XRES//2, YRES-1, s, c)

#horizontal and vertical
c[BLUE] = 0
c[GREEN] = 255
draw_line(0, YRES//2, XRES-1, YRES//2, s, c)
draw_line(XRES//2, 0, XRES//2, YRES-1, s, c)


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')

def my_own():
    from math import cos,sin
    DEFAULT_COLOR[0]=255
    DEFAULT_COLOR[1]=255
    DEFAULT_COLOR[2]=255
    s=new_screen()
    c=[0,0,0]

    # x-axis
    draw_line(0,YRES//2,XRES,YRES//2,s,c)
    # y-axis
    draw_line(XRES//2,0,XRES//2,YRES,s,c)

    c=[220,0,0]
    density=4.5

    # derivative of xsin(x)
    f_prime = lambda x: x*cos(x/density)/density+sin(x/density)

    lasty=YRES//2
    for x in range(XRES//2,XRES-1):
        lin=f_prime(x-XRES//2)
        draw_line(x,lasty,x+1,lasty+int(lin),s,c)
        lasty+=int(lin)
    lasty = YRES // 2
    for x in range(XRES // 2, 0,-1):
        lin = f_prime(x - XRES // 2)
        draw_line(x, lasty, x - 1, lasty - int(lin), s, c)
        lasty -= int(lin)

    # squeeze
    c=[0,100,255]
    draw_line(0,0,XRES,YRES,s,c)
    draw_line(0,YRES,XRES,0,s,c)

    display(s)
    save_ppm(s, 'binary.ppm')
    save_ppm_ascii(s, 'ascii.ppm')
    save_extension(s, 'img.png')

my_own()