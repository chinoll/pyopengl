from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from antialiasing import *
from math import *
def transforPolygan(x,y,tx,ty):
    '''
        将图元平移
        x:坐标x的集合
        y:坐标y的集合
        tx:移动x的增量
        ty:移动y的增量
    '''
    points = []
    for i in range(len(x)):
        points.append((x[i] + tx,y[i] + ty))
    for point in points:
        antialiasing(point[0],point[1])
    return points

def rotatePolygan(x,y,tx,ty,theta):
    '''
        将图元绕轴旋转
        x:坐标x的集合
        y:坐标y的集合
        tx:轴的x坐标
        ty:轴的y坐标
        theta:旋转角度
    '''
    points = []
    for i in range(len(x)):
        nx = tx + (x[i] - tx)*cos(theta) - (y[i] - ty)*sin(theta)
        ny = ty + (x[i] - tx)*sin(theta) + (y[i] - ty)*cos(theta)
        points.append((nx,ny))
    for point in points:
        antialiasing(point[0],point[1])
    return points