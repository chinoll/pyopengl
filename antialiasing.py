from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import colorsys
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
            glVertex2f(x + j,y-i)