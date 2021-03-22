import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import colorsys
x = []
def antialiasing(x,y):
    hsv = colorsys.rgb_to_hsv(255,255,255)[2] / 128
    mask = (np.array([[96,112,96],[112,128,112],[96,112,96]]) * hsv).astype(np.int16)
    x -= 1
    y += 1
    for i in range(3):
        for j in range(3):
            rgb = np.array(colorsys.hsv_to_rgb(0,0,mask[i][j]))/255
            rgb = list(rgb)
            glColor3f(rgb[0],rgb[1],rgb[2])
            glVertex2i(x + j,y-i)
def bresenhamLine(x0,y0,xend,yend,width=1):
    dx = abs(xend - x0)
    dy = abs(yend - y0)
    p = 2 * dy - dx
    glBegin(GL_POINTS)
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
            x += 1
            y += 1
        glEnd()
        glFlush()
        return
    elif k == 0:
        x,y = x0,y0
        while x0 < xend:
            antialiasing(x,y)
            x += 1
        glEnd()
        glFlush()
        return
    elif k == -1:
        y,x = x0,y0
        while x0 < xend:
            antialiasing(x,y)
            x += 1
        glEnd()
        glFlush()
        return
    antialiasing(x,y)

    while x < xend:
        x += 1
        if p < 0:
            p += twody
        else:
            y += 1
            p += twodymiusdx
        antialiasing(x,y)
        if x0 >y0:
            for i in range(1,width+1):
                antialiasing(x,y+i)
        else:
            for i in range(1,width+1):
                antialiasing(x+i,y)
    glEnd()
    glFlush()
def init():
    global x
    x = [int(x) for x in input().split(",")]
    glClearColor(1,1,1,0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0,400.0,0.0,400.0)


def start():
    if len(x) == 4:
        bresenhamLine(x[0],x[1],x[2],x[3])
    else:
        bresenhamLine(x[0],x[1],x[2],x[3],x[4])

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400,400)
glutCreateWindow("直线光栅化算法")
init()
glutDisplayFunc(start)
glutMainLoop()