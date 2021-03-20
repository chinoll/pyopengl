import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
x = []

def bres(x0,y0,xend,yend):
    dx = abs(xend - x0)
    dy = abs(yend - y0)
    p = 2 * dy - dx
    twody = 2 *dy
    twodymiusdx = 2 * (dy - dx)
    #glPointSize(5)
    glBegin(GL_POINTS)
    if x0 > xend:
        x = xend
        y = yend
        xend = x0
    elif yend > xend:
        xend,yend = yend,xend
        x,y = y0,x0
    else:
        x = x0
        y = y0
    glVertex2f(x,y)

    while x < xend:
        x += 1
        if p < 0:
            p += twody
        else:
            y += 1
            p += twodymiusdx
        glVertex2i(x,y)
    glEnd()
    glFlush()
def init():
    global x
    x = [int(x) for x in input().split(",")]
    glClearColor(1,1,1,0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0,400.0,0.0,400.0)


def start():
    bres(x[0],x[1],x[2],x[3])
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400,400)
glutCreateWindow("直线光栅化算法")
init()
glutDisplayFunc(start)
glutMainLoop()