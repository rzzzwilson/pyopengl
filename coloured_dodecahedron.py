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
#            (1, 16, 17, 2, 12),
            (2, 10, 3, 13, 12),
#            (0, 19, 4, 8, 9),
#            (1, 9, 8, 5, 16),
#            (2, 17, 6, 11, 10),
#            (3, 18, 7, 11, 10),
#            (7, 14, 4, 19, 18),
#            (5, 15, 6, 17, 16),
#            (5, 15, 14, 4, 8),
#            (7, 14, 15, 6, 11),
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

def Dodecahedron():
    glBegin(GL_TRIANGLE_FAN)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            if x >= len(colors):
                x = 0
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((1.0, 1.0, 1.0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
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
        #pygame.time.wait(10)
        pygame.time.wait(100)

main()
