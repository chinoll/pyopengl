from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from antialiasing import *

def transforPolygan(x,y,tx,ty):
    '''
        x:坐标x的集合
        y:坐标y的集合
        tx:移动x的增量
        ty:移动y的增量
    '''
    points = []
    for i in range(len(x)):
        points.append((x[i] + tx,y[i] + ty))
    #print("move",points)
    glBegin(GL_POINTS)
    for point in points:
        antialiasing(point[0],point[1])
    return points