import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from antialiasing import *
from math import pi
from transfor import *
x = []
def bresenhamLine(x0,y0,xend,yend,width=1):
    dx = abs(xend - x0)
    dy = abs(yend - y0)
    p = 2 * dy - dx
    points = []
    try:
        k = abs((yend-y0)/(xend - x0))
    except:
        k = -1  #垂直直线
    if k < 1:
        twody = 2 * dy
        twodymiusdx = 2 * (dy - dx)
        if x0 > xend:
            x = xend
            y = yend
            xend = x0
        else:
            x = x0
            y = y0
    elif k > 1:
        twody = 2 * dx
        twodymiusdx = 2 * (dx - dy)
        if y0 > yend:
            y = xend
            x = yend
            xend = y0
        else:
            x,y = x0,y0
            xend,yend=yend,xend
    elif k == 1.0:
        x,y = x0,y0
        while x <= xend:
            antialiasing(x,y)
            points.append((x,y))

            x += 1
            y += 1
        return points
    elif k == 0:
        x,y = x0,y0
        while x0 < xend:
            antialiasing(x,y)
            points.append((x,y))
            x += 1
        return points
    elif k == -1:
        y,x = x0,y0
        while x0 < xend:
            antialiasing(x,y)
            points.append((x,y))
            x += 1
        glEnd()
        glFlush()
        return points
    antialiasing(x,y)
    points.append((x,y))
    while x < xend:
        x += 1
        if p < 0:
            p += twody
        else:
            y += 1
            p += twodymiusdx
        antialiasing(x,y)
        points.append((x,y))
        if x0 >y0:
            for i in range(1,width+1):
                antialiasing(x,y+i)
        else:
            for i in range(1,width+1):
                antialiasing(x+i,y)
    return points
def init():
    global x
    x = [int(x) for x in input().split(",")]
    glClearColor(1,1,1,0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0,400.0,0.0,400.0)


def start():
    glBegin(GL_POINTS)
    points = []
    if len(x) == 4:
        points = bresenhamLine(x[0],x[1],x[2],x[3])
    else:
        points = bresenhamLine(x[0],x[1],x[2],x[3],x[4])
    print(points)
    i = [i[0] for i in points]
    j = [i[1] for i in points]
    scalePolygan(i,j,0.5,0.3,i[0],j[0])
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400,400)
glutCreateWindow("直线光栅化算法")
init()
glutDisplayFunc(start)
glutMainLoop()