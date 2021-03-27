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

def scalePolygan(x,y,sx,sy,xf,yf):
    '''
        将图元进行缩放
        x:坐标x的集合
        y:坐标y的集合
        sx:坐标x的缩放比例
        sy:坐标y的缩放比例
        xf:缩放基准点x
        yf:缩放基准点y
    '''
    points = []
    for i in range(len(x)):
        nx = x[i] * sx + xf*(1-sx)
        ny = y[i] * sy + yf*(1-sy)
        points.append((nx,ny))
    for point in points:
        antialiasing(point[0],point[1])
    return points