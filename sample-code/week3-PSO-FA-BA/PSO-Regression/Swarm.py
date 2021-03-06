import numpy as np
from config import *
from Particle import *
from Dataset import *

class Swarm(object):
    def __init__(self, filename):
        self.data = Dataset(filename)
        self.particles = [Particle(self) for _ in range(SWARM_SIZE)]
        bestIdx = np.argmin(np.array([self.particles[i].value for i in range(SWARM_SIZE)]))
        self.gBestPosition = self.particles[bestIdx].position.copy()
        self.gBestValue = self.particles[bestIdx].value.copy()
    
    def move(self):
        bestIdx = -1
        for i in range(SWARM_SIZE):
            self.particles[i].move()
            if self.gBestValue > self.particles[i].value:
                bestIdx = i
        
        if bestIdx != -1:
            self.gBestPosition = self.particles[bestIdx].position.copy()
            self.gBestValue = self.particles[bestIdx].value
    
    def printResult(self):
        self.data.setCoef(self.gBestPosition)
        self.data.printEquation()