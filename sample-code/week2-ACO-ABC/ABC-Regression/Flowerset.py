import numpy as np
from config import *
from Flower import *
from Dataset import *

class Flowerset(object):
    def __init__(self, filename):
        self.data = Dataset(filename)
        self.flower = [Flower(self) for _ in range(EBEE_NUM)]
        bestIndex = np.argmax(np.array([self.flower[i].value for i in range(EBEE_NUM)]))
        self.bestPos = self.flower[bestIndex].position.copy()
        self.bestValue = self.flower[bestIndex].value
        self._newFlower = Flower(self)
        self._trValue = np.array([0. for _ in range(EBEE_NUM)])
    
    def printReport(self):
        print("report:")
        print("bestValue:", self.bestValue, "bestPos:", self.bestPos )
    
    def employedBeePhase(self):
        for i in range(EBEE_NUM):
            self._newFlower.change(i)
            if self.flower[i].value > self._newFlower.value:
                tmp = self._newFlower
                self._newFlower = self.flower[i]
                self.flower[i] = tmp
            self.flower[i].visitNum += 1
    
    def onlookerBeePhase(self):
        for j in range(OBEE_NUM):
            self._trValue = [self.flower[i].value for i in range(EBEE_NUM)]
            self._trValue = np.exp(self._trValue)/np.sum(np.exp(self._trValue))

            r = np.random.uniform(0,1)
            for i in range(EBEE_NUM-1):
                prob = self._trValue[i]
                if r <= prob:
                    break
                r -= prob
            
            self._newFlower.change(i)
            if self.flower[i].value > self._newFlower.value:
                tmp = self._newFlower
                self._newFlower = self.flower[i]
                self.flower[i] = tmp
            self.flower[i].visitNum += 1
    
    def scoutBeePhase(self):
        for i in range(EBEE_NUM):
            if VISIT_MAX <= self.flower[i].visitNum:
                self.flower[i].renew()

    def saveBestPosition(self):
        best = -1
        for i in range(EBEE_NUM):
            if self.bestValue > self.flower[i].value:
                best = i        
        
        if best != -1:
            self.bestPos = self.flower[best].position.copy()
            self.bestValue = self.flower[best].value
    
    def printResult(self):
        self.data.setCoef(self.bestPos)
        self.data.printEquation()