#! /usr/bin/env python

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

LineList = (
            (0.0, 0.0, 1.0, 1.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
            (0.0, 0.0, 1.0, -1.0),
            (1.0, 1.0, 0.0, 1.0),
           )

MaxPersistance = 2
OldLines = []
Phosphor = (1.00, 1.00, 0.70)
Decay = 1.5
BrightLevels = []

def show(lines):
    # store display for persistance
    global OldLines
    OldLines.append(lines)
    if len(OldLines) > MaxPersistance:
        del OldLines[0]

    # display the lines
    for (bl, display_lines) in enumerate(OldLines):
        glColor3f(*BrightLevels[bl])
        glLineWidth(1.0)
        glBegin(GL_LINES)
        for (bx, by, ex, ey) in display_lines:
            glVertex3f(bx, by, 0.0)
            glVertex3f(ex, ey, 0.0)
        glEnd()

def main():
    # establish brightness levels
    bl = Phosphor
    for i in range(MaxPersistance):
        BrightLevels.append(bl)
        new_bl = []
        for l in bl:
            new_bl.append(l/Decay)
        bl = new_bl
    BrightLevels.reverse()

    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)

    dx = 0.0
    delta = -0.01
    while True:
        # generate new display list
        d_list = []
        for (bx, by, ex, ey) in LineList:
            d_list.append((bx+dx, by, ex+dx, ey))
        dx += delta
        if dx > 0.5 or dx < -0.5:
            delta = -delta

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        show(d_list)
        pygame.display.flip()
        pygame.time.wait(10)

main()

