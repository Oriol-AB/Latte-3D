import pygame
import numpy as np

class Viewer:
    def __init__(self, width, height, caption="Latte 3D Window"):
        self.width = width
        self.height = height
        self.caption = caption

        self.renderEdges = True
        self.renderNodes = True
        self.nodeRadius = 4
        self.nodeColor = (200, 200, 200)
        self.edgeColor = (255, 255, 255)
        self.backgroundColor = (10, 10, 10)

        self.display_surface = pygame.Surface((self.width, self.height))
        pygame.display.set_caption(self.caption)

        self.meshes = []
        self.activeCamera = None

        self.nearClip = 0.1
        self.farClip = 100

    def updateDisplaySurface(self, width, height):
        self.display_surface = pygame.Surface((width, height))

    def bindCamera(self, camera):
        self.activeCamera = camera

    def renderScene(self, window, position=(0, 0)):
        if self.activeCamera is None:
            raise RuntimeError("No active camera in the scene!")
        for mesh in self.meshes:
            if self.renderNodes:
                for node in mesh.nodes:
                    screenCoordinate = np.matmul(self.activeCamera.projectionMatrix, np.expand_dims(node, axis=1))
                    zDepth = screenCoordinate[2][0]
                    
                    if zDepth > self.nearClip and zDepth < self.farClip:
                        screenCoordinate = screenCoordinate / screenCoordinate[2][0]
                        #print(screenCoordinate)
                        pygame.draw.circle(self.display_surface, self.nodeColor, (int(screenCoordinate[0][0]), int(screenCoordinate[1][0])), self.nodeRadius)

            if self.renderEdges:
                for edge in mesh.edges:
                    startPos = np.matmul(self.activeCamera.projectionMatrix, np.expand_dims(mesh.nodes[edge[0]], axis=1))
                    endPos = np.matmul(self.activeCamera.projectionMatrix, np.expand_dims(mesh.nodes[edge[1]], axis=1))
                    #Normalize z-depth
                    startPos = startPos / startPos[2][0]
                    endPos = endPos / endPos[2][0]
                    
                    pygame.draw.aaline(self.display_surface, self.nodeColor, startPos[:-1], endPos[:-1])


        window.blit(self.display_surface, position)

    def renderAll(self, axis):
        
        match axis:
            case "X" | "x":
                for mesh in self.meshes:
                    if self.renderNodes:
                        for node in mesh.nodes:
                            pygame.draw.circle(self.display_surface, self.nodeColor, (int(node[2]),int(node[1])), self.nodeRadius)

                    if self.renderEdges:
                        for edge in mesh.edges:
                            pygame.draw.aaline(self.display_surface, self.edgeColor, int(mesh.nodes[edge[0]][1]), int(mesh.nodes[edge[1]][2]))
            
            case "Y" | "y":
                for mesh in self.meshes:
                    if self.renderNodes:
                        for node in mesh.nodes:
                            pygame.draw.circle(self.display_surface, self.nodeColor, (int(node[0]), int(node[2])), self.nodeRadius)

                    if self.renderEdges:
                        for edge in mesh.edges:
                            pygame.draw.aaline(self.dsplay_surface, self.edgeColor, int(mesh.nodes[edge[0]][0]), int(mesh.nodes[edge[1]][2]))

            case "Z" | "z":
                for mesh in self.meshes:
                    if self.renderNodes:
                        for node in mesh.nodes:
                            #print(node)
                            pygame.draw.circle(self.display_surface, self.nodeColor, (int(node[0]), int(node[1])), self.nodeRadius)

                    if self.renderEdges:
                        for edge in mesh.edges:
                            #print((mesh.nodes[edge[0]][0], mesh.nodes[edge[0]][1]))
                            start_pos = (int(mesh.nodes[edge[0]][0]), int(mesh.nodes[edge[0]][1]))
                            end_pos = (int(mesh.nodes[edge[1]][0]), int(mesh.nodes[edge[1]][1]))
                            pygame.draw.aaline(self.display_surface, self.edgeColor, start_pos, end_pos)

            case _:
                raise ValueError(f"L'eix de projecció '{axis}' no és un eix vàlid. Els únics eixos vàlids són: 'X/x', 'Y/y' i  'Z/z'")

    def addMesh(self, mesh):
        self.meshes.append(mesh)
