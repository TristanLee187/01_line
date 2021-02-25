from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    [(i,j),(k,l)]=sorted([(x0,y0),(x1,y1)])
    a=l-j
    b=i-k
    x = i
    y = j
    if b==0:
        while y<max(j,l):
            plot(screen,color,x,y)
            y+=1
        return
    m=-a/b
    # Quadrant 1 and 5
    if 0<=m<=1:
        d=2*a+b
        while x<=k:
            plot(screen,color,x,y)
            if d>0:
                y+=1
                d+=2*b
            x+=1
            d+=2*a
    # Quadrant 2 and 6
    elif 1<m:
        d=a+2*b
        while y<l:
            plot(screen,color,x,y)
            if d<0:
                x+=1
                d+=2*a
            y+=1
            d+=2*b
    # Quadrant 3 and 7
    elif m<-1:
        d=a+2*b
        while y>l:
            plot(screen,color,x,y)
            if d>0:
                x+=1
                d+=2*a
            y-=1
            d-=2*b
    # Quadrant 4 and 8
    else:
        d = 2 * a + b
        while x <= k:
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= 2 * b
            x += 1
            d += 2 * a