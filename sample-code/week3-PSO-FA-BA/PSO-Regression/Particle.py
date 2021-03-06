import numpy.random._examples.cffi
import numpy as np
from config import *

class Particle(object):
    def __init__(self, swarm):
        self.swarm = swarm
        self.position = np.random.uniform(COEF_MIN, COEF_MAX, self.swarm.data.numX)
        self.velocity = np.random.uniform(COEF_MIN, COEF_MAX, self.swarm.data.numX)
        self._pBestPosition = np.zeros(self.swarm.data.numX)
        self._pBestValue = float('inf')
        self._evaluate()
    
    def move(self):
        # v(t+1) = Iv(t) + Ag{g(t)-x(t)} + Ap{p(t)-x(t)}
        self.velocity = INERTIA * self.velocity \
                         + ACCEL_G * (self.swarm.gBestPosition - self.position) * np.random.uniform(0,1) \
                         + ACCEL_P * (self._pBestPosition - self.position) * np.random.uniform(0,1)
        
        # x(t+1) = x(t) + v(t+1)
        self.position = self.position + self.velocity
        
        self._evaluate()
    
    def _evaluate(self):
        self.value = np.sum((self.swarm.data.Ynorm - self.position @ self.swarm.data.Xnorm.T)**2)

        if self._pBestValue > self.value:
            self._pBestPosition = self.position.copy()
            self._pBestValue = self.value