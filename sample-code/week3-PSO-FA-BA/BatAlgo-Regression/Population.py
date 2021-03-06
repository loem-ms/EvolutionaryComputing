import numpy as np
from config import *
from Bat import *
from Dataset import *

class Population(object):
    def __init__(self, filename):
        self.data = Dataset(filename)
        self.bat = [Bat(self) for _ in range(POP_SIZE)]
        self._sort_value()
        self.bestPosition = self.bat[0].position.copy()
        self.bestValue = self.bat[0].value.copy()

    def _sort_value(self):
        self.bat = sorted(self.bat, key=lambda x: x.value)
    
    def move(self, t):
        for i in range(0, POP_SIZE):
            self.bat[i].move(t)
        
        self._sort_value()
        
        if self.bat[0].value < self.bestValue:
            self.bestPosition = self.bat[0].position.copy()
            self.bestValue = self.bat[0].value.copy()
    
    def printResult(self):
        self.data.setCoef(self.bestPosition)
        self.data.printEquation()