from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawFun():
    glClear(GL_COLOR_BUFFER_BIT)
    glutWireTeapot(1)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400,400)
glutCreateWindow("teapot")
glutDisplayFunc(drawFun)
glutMainLoop()