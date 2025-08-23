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

        self.display = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption(self.caption)
        
        self.meshes = []

    def renderAll(self, axis):
        
        match axis:
            case "X" | "x":
                for mesh in self.meshes:
                    if self.renderNodes:
                        for node in mesh.nodes:
                            pygame.draw.circle(self.display, self.nodeColor, (int(node[2]),int(node[1])), self.nodeRadius)

                    if self.renderEdges:
                        for edge in mesh.edges:
                            pygame.draw.aaline(self.display, self.edgeColor, int(mesh.nodes[edge[0]][1]), int(mesh.nodes[edge[1]][2]))
            
            case "Y" | "y":
                for mesh in self.meshes:
                    if self.renderNodes:
                        for node in mesh.nodes:
                            pygame.draw.circle(self.display, self.nodeColor, (int(node[0]), int(node[2])), self.nodeRadius)

                    if self.renderEdges:
                        for edge in mesh.edges:
                            pygame.draw.aaline(self.dsplay, self.edgeColor, int(mesh.nodes[edge[0]][0]), int(mesh.nodes[edge[1]][2]))

            case "Z" | "z":
                for mesh in self.meshes:
                    if self.renderNodes:
                        for node in mesh.nodes:
                            #print(node)
                            pygame.draw.circle(self.display, self.nodeColor, (int(node[0]), int(node[1])), self.nodeRadius)

                    if self.renderEdges:
                        for edge in mesh.edges:
                            #print((mesh.nodes[edge[0]][0], mesh.nodes[edge[0]][1]))
                            start_pos = (int(mesh.nodes[edge[0]][0]), int(mesh.nodes[edge[0]][1]))
                            end_pos = (int(mesh.nodes[edge[1]][0]), int(mesh.nodes[edge[1]][1]))
                            pygame.draw.aaline(self.display, self.edgeColor, start_pos, end_pos)

            case _:
                raise ValueError(f"L'eix de projecció '{axis}' no és un eix vàlid. Els únics eixos vàlids són: 'X/x', 'Y/y' i  'Z/z'")

    def addMesh(self, mesh):
        self.meshes.append(mesh)
