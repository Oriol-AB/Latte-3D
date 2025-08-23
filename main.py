import pygame
import sys
import numpy as np 

import camera
import viewer
import mesh
import utils

if __name__ == "__main__":
    viewer = viewer.Viewer(800, 600)

    viewer.renderNodes = False

    cube_mesh = utils.createCubeMesh("cube")
    viewer.addMesh(cube_mesh)
    
    Clock = pygame.time.Clock()

    while True:
        

        viewer.display.fill(viewer.backgroundColor)

        viewer.renderAll("z")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            cube_mesh.translate((1, 0, 0))

        if keys[pygame.K_LEFT]:
            cube_mesh.translate((-1, 0, 0))
        if keys[pygame.K_DOWN]:
            cube_mesh.translate((0, 1, 0))

        if keys[pygame.K_UP]:
            cube_mesh.translate((0, -1, 0))
        
        if keys[pygame.K_PLUS]:
            cube_mesh.scale((1.1, 1.1, 1.1))

        if keys[pygame.K_MINUS]:
            cube_mesh.scale((0.9, 0.9, 0.9))
        
        if keys[pygame.K_q]:
            cube_mesh.rotate("X", -0.01)

        if keys[pygame.K_w]:
            cube_mesh.rotate("X", 0.01)

        if keys[pygame.K_a]:
            cube_mesh.rotate("Y", -0.01)

        if keys[pygame.K_s]:
            cube_mesh.rotate("Y", 0.01)

        if keys[pygame.K_z]:
            cube_mesh.rotate("Z", -0.01)

        if keys[pygame.K_x]:
            cube_mesh.rotate("Z", 0.01)

        pygame.display.update()
