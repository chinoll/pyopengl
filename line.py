from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(1,1,1,0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0,200.0,0.0,150.0)

def line():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.4,0.2)
    glBegin(GL_LINES)
    glVertex2i(180,25)
    glVertex2i(10,145)
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400,400)
glutCreateWindow("Hello world")
init()
glutDisplayFunc(line)
glutMainLoop()
