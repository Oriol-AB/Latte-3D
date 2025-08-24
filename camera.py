import pygame
import utils
import numpy as np

class Camera:
    def __init__(self, tag, position, principalPoint,orientation=np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=np.float32), focalLength=50, skew=0):
        self.position = position                                                #  forward       top       right
        self.orientation = orientation
        self.tag = tag
        self.focalLength = focalLength
        self.skew = skew
        self.principalPoint = principalPoint


        self.intrinsicMatrix = np.array([
                [self.focalLength, self.skew, self.principalPoint[0]],
                [0, self.focalLength, self.principalPoint[1]],
                [0, 0, 1]
            ], dtype=np.float32)

        self.extrinsicMatrix = np.hstack((self.orientation, np.expand_dims(self.position, axis=1)))
        
        self.projectionMatrix = np.matmul(self.intrinsicMatrix, self.extrinsicMatrix)

        if np.all(self.orientation == 0):
            raise ValueError(f"Error: La matriu d'orientació per la càmera '{self.tag}' està buida. ")

    def updateProjectionMatrix(self):
        self.projectionMatrix = np.matmul(self.intrinsicMatrix, self.extrinsicMatrix)

    def updateIntrinsicMatrix(self):

        self.intrinsicMatrix = np.array([
                [self.focalLength, self.skew, self.principalPoint[0]],
                [0, self.focalLength, self.principalPoint[1]],
                [0, 0, 1]
            ], dtype=np.float32)
        self.updateProjectionMatrix()

    def translate(self, translationVector):
        self.position = utils.transformVector(self.position, utils.translationMatrix(*translationVector))
        self.updateExtrinsicMatrix()
        self.updateProjectionMatrix()
    
    def moveForward(self, amount):
        self.position += amount * utils.unitVector(self.orientation[0])
        self.updateExtrinsicMatrix()

    def moveSideways(self, amount):
        self.position += amount * utils.unitVector(self.orientation[2])
        self.updateExtrinsicMatrix()

    def moveVertical(self, amount):
        self.position += amount * utils.unitVector(self.orientation[1])
        self.updateExtrinsicMatrix()

    def rotate(self, axis, angle):
        for axis in range(3):
            original_pos = self.position
            self.translate(-self.position)
            self.orientation[axis] = utils.transformVector(self.orientation[axis], utils.rotationMatrix(axis, angle))
            self.translate(original_pos)
        
        self.updateExtrinsicMatrix()
        self.updateProjectionMatrix()

    def updateExtrinsicMatrix(self):
        self.extrinsicMatrix = np.hstack((self.orientation, np.expand_dims(self.position, axis=1)))

        self.updateProjectionMatrix()

    def debugPrint(self):
        print(f"------------  Càmera '{self.tag}' --------------")

        print(f"Posició: {self.position}")
        print(f"Orientació: {self.orientation}")
        print(f"Activa: {'Si' if self.active else 'No'}")

if __name__ == "__main__":
    camera = Camera("camera", True, np.array([4, 4, 4], dtype=np.float32), np.array([200, 200]))
