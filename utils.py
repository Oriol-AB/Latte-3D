import numpy as np
import mesh

def collideCircle(radius, circlePos, coords):
    dist = np.sqrt((coords[0]-circlePos[0])**2 + (coords[1]-circlePos[1])**2)

    if dist < radius:
        return True
    
    return False

def unitVector(vector):
    module = np.linalg.norm(vector)
    
    try:
        return vector / module

    except ZeroDivisionError:
        return vector

def translationMatrix(dx, dy, dz):
    return np.array([
            [1, 0, 0, dx],
            [0, 1, 0, dy],
            [0, 0, 1, dz],
            [0, 0, 0, 1]
        ])

def scaleMatrix(dx, dy, dz):
    return np.array([
            [dx, 0, 0, 0],
            [0, dy, 0, 0],
            [0, 0, dz, 0],
            [0, 0, 0, 1]
        ])

def rotationMatrix(axis, angle):
    #if axis.upper() not in ["X", "Y", "Z"]:
    #    raise ValueError(f"Error: L'eix '{axis}' no és un eix de coordenades vàlid.")

    match axis:
        case "X" | "x":
            return np.array([
                    [1, 0, 0],
                    [0, np.cos(angle), -np.sin(angle)],
                    [0, np.sin(angle), np.cos(angle)]
                ])

        case "Y" | "y":
            return np.array([
                    [np.cos(angle), 0, np.sin(angle)],
                    [0, 1, 0],
                    [-np.sin(angle), 0, np.cos(angle)]
                ])

        case "Z" | "z":
            return np.array([
                    [np.cos(angle), -np.sin(angle), 0],
                    [np.sin(angle), np.cos(angle), 0],
                    [0, 0, 1]
                ])

        case _:
            raise ValueError(f"Error: L'eix '{axis}' no és un eix de coordenades vàlid.")

def transformVector(vector, transformationMatrix):
    return np.matmul(transformationMatrix, vector)


def createCubeMesh(tag):

    cube_nodes = np.array([
            [0, 0, 0],
            [0, 0, 1],
            [1, 0, 1],
            [1, 0, 0],
            [0, 1, 0],
            [0, 1, 1],
            [1, 1, 1],
            [1, 1, 0]
        ])

    cube_edges = np.array([
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0],
            [4, 5],
            [5, 6],
            [6, 7],
            [7, 4],
            [0, 4],
            [1, 5],
            [2, 6],
            [3, 7]
        ])

    cube_mesh = mesh.Mesh(tag)

    cube_mesh.addNodes(cube_nodes)
    cube_mesh.addEdges(cube_edges)

    return cube_mesh
