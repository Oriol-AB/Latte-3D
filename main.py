import pygame
import sys
import numpy as np 

import camera
import viewer
import mesh
import utils

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()

    screenWidth, screenHeight = 1000, 800
    font = pygame.font.SysFont("Arial", 30)
    

    window = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
    viewer = viewer.Viewer(screenWidth, screenHeight)


    cube_mesh = utils.createCubeMesh("cube")
    viewer.addMesh(cube_mesh)
   
    camera = camera.Camera("camera", np.array([1, 1, 1], dtype=np.float32), np.array([500, 400]))
    viewer.bindCamera(camera)

    clock = pygame.time.Clock()




    while True:
        #window.fill((255, 255, 255))

        FL_surface = font.render(f"Focal Length: {camera.focalLength}", False, (255, 255, 255))
        FPSText = font.render(f"FPS: {int(clock.get_fps())}", False, (255, 255, 255))

        viewer.display_surface.fill(viewer.backgroundColor)

    
        viewer.renderScene(window, position=(0, 0))

        window.blit(FL_surface, (25, 25))
        window.blit(FPSText, (25, 65))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.VIDEORESIZE:
                viewer.updateDisplaySurface(window.get_width(), window.get_height())


        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            camera.moveSideways(-0.5)

        if keys[pygame.K_LEFT]:
            camera.moveSideways(0.5)
        if keys[pygame.K_DOWN]:
            camera.moveForward(0.5)

        if keys[pygame.K_UP]:
            camera.moveForward(-0.5)
        
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
            camera.moveVertical(-0.5)
        if keys[pygame.K_x]:
            camera.moveVertical(0.5)

        if keys[pygame.K_0]:
            camera.focalLength += 1
            if camera.focalLength > 200:
                camera.focalLength -= 1
            camera.updateIntrinsicMatrix()
            
        if keys[pygame.K_9]:
            
            camera.focalLength -= 1
            if camera.focalLength < 10:
                camera.focalLength += 1
            
            camera.updateIntrinsicMatrix()

            focalLengthToggler = not focalLengthToggler

        pygame.display.update()
        clock.tick(60)
