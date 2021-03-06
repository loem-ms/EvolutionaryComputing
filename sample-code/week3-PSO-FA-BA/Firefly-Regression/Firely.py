import numpy as np
from config import *
from Population import *

class Firely(object):
    def __init__(self, population):
        self.population = population
        self.position = np.random.uniform(COEF_MIN, COEF_MAX, self.population.data.numX)
        self._evaluate()

    def move(self, base):
        if self.intensity > base.intensity:
            dis = np.sum((base.position-self.position)**2)

            self.position = self.position + ATTRACT * np.exp(-1 * ABSORB * dis) * (base.position - self.position)\
                                          + RANDOMIZE * np.random.uniform(-0.5,0.5)

            self._evaluate()
    
    def _evaluate(self):
        self.intensity = np.sum((self.population.data.Ynorm - self.position @ self.population.data.Xnorm.T)**2)
