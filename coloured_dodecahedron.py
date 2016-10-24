#! /usr/bin/env python

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

colors = (
          (0.0, 0.0, 0.0),
          (0.0, 0.0, 0.5),
          (0.0, 0.0, 1.0),
          (0.0, 0.5, 1.0),
          (0.0, 1.0, 0.0),
          (0.0, 1.0, 0.5),
          (0.0, 1.0, 1.0),
          (0.5, 1.0, 1.0),
          (1.0, 0.0, 0.0),
          (1.0, 0.0, 0.5),
          (1.0, 0.0, 1.0),
          (1.0, 0.5, 1.0),
          (1.0, 1.0, 0.0),
          (1.0, 1.0, 0.5),
          (1.0, 1.0, 1.0),
         )

#colors = (
#          (1.0, 0.0, 0.0),
#          (1.0, 0.5, 0.0),
#          (1.0, 0.5, 0.5),
#          (1.0, 0.0, 0.5),
#          (1.0, 0.0, 0.0),
#          (1.0, 0.5, 0.0),
#          (1.0, 0.5, 0.5),
#          (1.0, 0.0, 0.5),
#          (1.0, 0.0, 0.0),
#          (1.0, 0.5, 0.0),
#          (1.0, 0.5, 0.5),
#          (1.0, 0.0, 0.5),
#          (1.0, 0.0, 0.0),
#          (1.0, 0.5, 0.0),
#          (1.0, 0.5, 0.5),
#          (1.0, 0.0, 0.5),
#         )

Phi = (1.0 + math.sqrt(5.0))/2.0

# vertices of dodecahedron centred at (0, 0, 0)
vertices = (
            ( 1.0,  1.0, -1.0),             # 0 orange
            (-1.0,  1.0, -1.0),             # 1
            (-1.0,  1.0,  1.0),             # 2
            ( 1.0,  1.0,  1.0),             # 3
            ( 1.0, -1.0, -1.0),             # 4
            (-1.0, -1.0, -1.0),             # 5
            (-1.0, -1.0,  1.0),             # 6
            ( 1.0, -1.0,  1.0),             # 7
            ( 0.0, -1.0/Phi, -Phi),         # 8 green
            ( 0.0,  1.0/Phi, -Phi),         # 9
            ( 0.0,  1.0/Phi,  Phi),         # 10
            ( 0.0, -1.0/Phi,  Phi),         # 11
            (-1.0/Phi,  Phi, 0.0),          # 12 blue
            ( 1.0/Phi,  Phi, 0.0),          # 13
            ( 1.0/Phi, -Phi, 0.0),          # 14
            (-1.0/Phi, -Phi, 0.0),          # 15
            (-Phi, 0.0, -1.0/Phi),          # 16 red
            (-Phi, 0.0,  1.0/Phi),          # 17
            ( Phi, 0.0,  1.0/Phi),          # 18
            ( Phi, 0.0, -1.0/Phi),          # 19
           )

surfaces = (
            (0, 13, 3, 18, 19),
            (0, 9, 1, 12, 13),
            (1, 16, 17, 2, 12),
            (2, 10, 3, 13, 12),
            (0, 19, 4, 8, 9),
            (1, 9, 8, 5, 16),
            (2, 17, 6, 11, 10),
            (3, 18, 7, 11, 10),
            (7, 14, 4, 19, 18),
            (5, 15, 6, 17, 16),
            (5, 15, 14, 4, 8),
            (7, 14, 15, 6, 11),
           )
edges = (
         (0, 9),
         (0, 13),
         (0, 19),
         (1, 9),
         (1, 12),
         (1, 16),
         (2, 10),
         (2, 12),
         (2, 17),
         (3, 10),
         (3, 13),
         (3, 18),
         (4, 8),
         (4, 14),
         (4, 19),
         (5, 8),
         (5, 16),
         (5, 15),
         (6, 11),
         (6, 15),
         (6, 17),
         (7, 11),
         (7, 14),
         (7, 18),
         (8, 9),
         (10, 11),
         (12, 13),
         (14, 15),
         (16, 17),
         (18, 19),
        )

fly = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
       0x03, 0x80, 0x01, 0xC0, 0x06, 0xC0, 0x03, 0x60,
       0x04, 0x60, 0x06, 0x20, 0x04, 0x30, 0x0C, 0x20,
       0x04, 0x18, 0x18, 0x20, 0x04, 0x0C, 0x30, 0x20,
       0x04, 0x06, 0x60, 0x20, 0x44, 0x03, 0xC0, 0x22,
       0x44, 0x01, 0x80, 0x22, 0x44, 0x01, 0x80, 0x22,
       0x44, 0x01, 0x80, 0x22, 0x44, 0x01, 0x80, 0x22,
       0x44, 0x01, 0x80, 0x22, 0x44, 0x01, 0x80, 0x22,
       0x66, 0x01, 0x80, 0x66, 0x33, 0x01, 0x80, 0xCC,
       0x19, 0x81, 0x81, 0x98, 0x0C, 0xC1, 0x83, 0x30,
       0x07, 0xe1, 0x87, 0xe0, 0x03, 0x3f, 0xfc, 0xc0,
       0x03, 0x31, 0x8c, 0xc0, 0x03, 0x33, 0xcc, 0xc0,
       0x06, 0x64, 0x26, 0x60, 0x0c, 0xcc, 0x33, 0x30,
       0x18, 0xcc, 0x33, 0x18, 0x10, 0xc4, 0x23, 0x08,
       0x10, 0x63, 0xC6, 0x08, 0x10, 0x30, 0x0c, 0x08,
       0x10, 0x18, 0x18, 0x08, 0x10, 0x00, 0x00, 0x08]

def Dodecahedron():
#    glCullFace(GL_BACK)
#    glPolygonMode(GL_FRONT, GL_FILL)
#    glPolygonMode(GL_BACK, GL_FILL)
#    glPolygonMode(GL_FRONT, GL_FILL)
#    glEnable(GL_CULL_FACE)

#    glFrontFace(GL_CW)
#    glEnable (GL_POLYGON_STIPPLE)
#    glPolygonStipple(fly)
    x = 0
    for surface in surfaces:
        x += 1
        if x >= len(colors):
            x = 0
        glColor3fv(colors[x])
        glBegin(GL_POLYGON)
        for vertex in surface:
            glVertex3fv(vertices[vertex])
        glEnd()

    glPushAttrib(GL_ENABLE_BIT)
    glLineStipple(2, 0xAAAA)
    glEnable(GL_LINE_STIPPLE)
    glColor3fv((1.0, 1.0, 1.0))
    for edge in edges:
        glBegin(GL_LINES)
        for vertex in edge:
            glVertex3fv(vertices[vertex])
        glEnd()
    glPopAttrib()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (float(display[0])/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Dodecahedron()
        pygame.display.flip()
        pygame.time.wait(10)
        #pygame.time.wait(100)

main()
