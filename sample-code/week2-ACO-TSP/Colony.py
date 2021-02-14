import config
from Ant import *
from Field import *

class Colony(object):
    def __init__(self, filename):
        self.field = Field(filename)
        self.ant = [Ant(self) for _ in range(config.ANT_NUM)]
        self.nume = [[0. for _ in range(self.field.nodeNum)] for _ in range(self.field.nodeNum)]

    def selectRoute(self):
        for i in range(self.field.nodeNum):
            for j in range(1, i):
                self.nume[i][j] = pow(self.field.pheromone[i][j], config.alpha)* pow(1/self.field.distance[i][j], config.beta)
            for j in range(i+1, self.field.nodeNum):
                self.nume[i][j] = pow(self.field.pheromone[i][j], config.alpha)* pow(1/self.field.distance[i][j], config.beta)
        
        for i in range(config.ANT_NUM):
            self.ant[i].selectRoute()
    
    def renewPheromone(self):
        for i in range(self.field.nodeNum):
            for j in range(i+1, self.field.nodeNum):
                self.field.pheromone[i][j] *= (1 - config.EVA_R)
        
        for i in range(config.ANT_NUM):
            self.ant[i].putPheromone()
    
    def printPheromone(self):
        print("Pheromone")
        for i in range(self.field.nodeNum):
            for j in range(self.field.nodeNum):
                print("%10.3f"%(self.field.pheromone[i][j]), end=' ')
            print("\n")