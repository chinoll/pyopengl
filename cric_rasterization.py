
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import colorsys
import numpy as np
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

def cric_bres(r,x0,y0):
    x = 0
    y = r
    p = 5/4 - r
    while x <= y:
        x += 1
        if p < 0:
            p += 2*x + 1
        else:
            p += 2 * (x - (y + 0.1)) + 1
            y -= 1
        cricPoints(x0,y0,x,y)
def cricPoints(x0,y0,x,y):
    glBegin(GL_POINTS)
    antialiasing(x0 + x,y0 + y)
    antialiasing(x0 - x,y0 + y)
    antialiasing(x0 + x,y0 - y)
    antialiasing(x0 - x,y0 - y)
    antialiasing(x0 + y,y0 + x)
    antialiasing(x0 - y,y0 + x)
    antialiasing(x0 + y,y0 - x)
    antialiasing(x0 - y,y0 - x)
    glEnd()
    glFlush()
def init():
    global x
    x = [int(x) for x in input().split(",")]
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0,400.0,0.0,400.0)


def start():
    cric_bres(x[0],x[1],x[2])
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400,400)
glutCreateWindow("圆光栅化算法")
init()
glutDisplayFunc(start)
glutMainLoop()