import numpy as np
from config import *

class Bat(object):
    def __init__(self, population):
        self.population = population
        self.position = np.random.uniform(COEF_MIN, COEF_MAX, self.population.data.numX)
        self.velocity = np.zeros(self.population.data.numX)
        self.value = self._evaluate(self.position)
        self.freq = 0.0
        self.pulse = 0.0
        self.loudness = LOUD_0
        self._newPosition1 = np.zeros(self.population.data.numX)
        self._newPosition2 = np.zeros(self.population.data.numX)
    
    def move(self, t):
        # Case1: Move toward the location of best bats
        self.freq = np.random.uniform(FREQ_MIN, FREQ_MAX)
        self.velocity += (self.population.bestPosition - self.position) * self.freq
        self.position += self.velocity
        self.value = self._evaluate(self.position)

        # Case2: Move to the vicinity of the good bat 
        if np.random.uniform(0,1) > self.pulse:
            r = np.random.randint(0, POP_SIZE*BEST_RATE)
            aveLoud = np.mean(np.array([bat_.loudness for bat_ in self.population.bat]))
            self._newPosition1 = self.population.bat[r].position + np.random.uniform(-1,1, self.population.data.numX)*aveLoud
            self._newValue1 = self._evaluate(self._newPosition1)
        else:
            self._newValue1 = float('inf')
        
        # Case3: Move randomly
        self._newPosition2 = np.random.uniform(COEF_MIN, COEF_MAX, self.population.data.numX)
        self._newValue2 = self._evaluate(self._newPosition2)

        if ((self._newValue1 < self.value or self._newValue2 < self.value) and (np.random.uniform(0,1) < self.loudness)):
            if self._newValue1 < self._newValue2:
                tmp = self.position.copy()
                self.position = self._newPosition1.copy()
                self._newPosition1 = tmp.copy()
                self.value = self._newValue1.copy()
            else:
                tmp = self.position.copy()
                self.position = self._newPosition2.copy()
                self._newPosition2 = tmp.copy()
                self.value = self._newValue2.copy()

            self.pulse = PULSE_0 * (1 - np.exp(-PULSE_R * t))
            self.loudness *= LOUD_R

    def _evaluate(self, pos):
        value = np.sum((self.population.data.Ynorm - pos @ self.population.data.Xnorm.T)**2)
        return value