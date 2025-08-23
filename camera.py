import pygame
import utils
import numpy as np

class Camera:
    def __init__(self, tag, active, position, orientation=np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])):
        self.position = position
        self.orientation = orientation
        self.tag = tag

        if np.all(self.orientation == 0):
            raise ValueError(f"Error: El vector d'orientació per la càmera '{self.tag}' està buit. ")


    def debugPrint(self):
        print(f"------------  Càmera '{self.tag}' --------------")

        print(f"Posició: {self.position}")
        print(f"Orientació: {self.orientation}")
        print(f"Activa: {'Si' if self.active else 'No'}")
