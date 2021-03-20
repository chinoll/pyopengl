import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import colorsys
x = []
def antialiasing(x,y):
    hsv = colorsys.rgb_to_hsv(255,255,255)[2] / 4
    mask = (np.array([[1,2,1],[2,4,2],[1,2,1]]) * hsv).astype(np.int16)
    x -= 1
    y += 1
    for i in range(3):
        for j in range(3):
            rgb = np.array(colorsys.hsv_to_rgb(0,0,mask[i][j]))/255
            rgb = list(rgb)
            glColor3f(rgb[0],rgb[1],rgb[2])
            glVertex2i(x + j,y-i)

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
        antialiasing(x,y)
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