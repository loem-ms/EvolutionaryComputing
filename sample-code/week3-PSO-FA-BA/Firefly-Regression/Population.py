import numpy as np 
from config import *
from Firely import *
from Dataset import *

class Population(object):
    def __init__(self, filename):
        self.data = Dataset(filename)
        self.firely = [Firely(self) for _ in range(POP_SIZE)]
        bestIdx = np.argmin(np.array([self.firely[i].intensity for i in range(POP_SIZE)]))
        self.bestPosition = self.firely[bestIdx].position.copy()
        self.bestIntensity = self.firely[bestIdx].intensity.copy()

    def move(self):
        for i in range(0, POP_SIZE, +1):
            for j in range(0, POP_SIZE, +1):
                self.firely[i].move(self.firely[j])
                if self.bestIntensity > self.firely[i].intensity:
                    #print("best - firely[i]:",self.bestIntensity, self.firely[i].intensity)
                    self.bestPosition = self.firely[i].position.copy()
                    self.bestIntensity = self.firely[i].intensity.copy()
    
    def printResult(self):
        self.data.setCoef(self.bestPosition)
        self.data.printEquation()