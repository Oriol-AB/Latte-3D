import numpy as np
import utils

class Mesh:
    def __init__(self, tag):
        self.nodes = []
        self.edges = []
        self.tag = tag

    def addNodes(self, nodes):

        ones = np.ones((len(nodes), 1))
        ones_added = np.hstack((nodes, ones))

        for full_node in ones_added:
            self.nodes.append(full_node)
        
        self.nodes = np.array(self.nodes, dtype=np.float32)

    def addEdges(self, edges):
        for edge in edges:
            self.edges.append(edge)

        self.edges = np.array(self.edges)

    def translate(self, translationVector):
        #  1 0 0 dx |
        #  0 1 0 dy | Matriu de translació
        #  0 0 1 dz |
        #  0 0 0 1  |
        for node in range(len(self.nodes)):
            #self.nodes[node] = np.matmul(utils.translationMatrix(*vector), self.nodes[node])
            self.nodes[node] = utils.transformVector(self.nodes[node], utils.translationMatrix(*translationVector))
           # print(node)

    def scale(self, scaleVector):
        # dx 0 0 0 | 
        # 0 dy 0 0 | Matrix d'escalat
        # 0 0 dz 0 |
        # 0 0  0 0 |
            
        center = self.findCenter()
        self.translate(-center)

        for node in range(len(self.nodes)):
            self.nodes[node] = utils.transformVector(self.nodes[node], utils.scaleMatrix(*scaleVector))
        
        self.translate(center)

    def rotate(self, axis, angle):
        center = self.findCenter()
        self.translate(-center)
        
        for node in range(len(self.nodes)):
            self.nodes[node] = np.append(utils.transformVector(self.nodes[node][:-1], utils.rotationMatrix(axis, angle)), 1)
        
        self.translate(center)

    def findCenter(self):
        
        center = np.array([])

        for i in range(3):
            nums = np.array([])
            
            for node in self.nodes:
                nums = np.append(nums, node[i])
            center = np.append(center, np.mean(nums, dtype=np.float32))
        return center
        
    def printNodes(self):
        for node in self.nodes:
            print(node)

        print("-"*10)
