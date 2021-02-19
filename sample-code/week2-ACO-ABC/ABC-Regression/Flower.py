import numpy as np
import random
from config import *

class Flower(object):
    def __init__(self, flowerSet):
        self.flowerSet = flowerSet
        self.position = np.random.uniform(COEF_MIN, COEF_MAX, self.flowerSet.data.numX)
        self.value = 0.0
        self.visitNum = 0
        self.evaluate()
    
    def change(self, base):
        self.position = self.flowerSet.flower[base].position.copy()
        k = random.randint(0,self.flowerSet.data.numX-1)
        l = (base + (random.randint(1,EBEE_NUM-1))) % EBEE_NUM
        self.position[k] = self.position[k] + np.random.uniform(-1,1)*(self.position[k]-self.flowerSet.flower[l].position[k])
        self.visitNum = 0
        self.evaluate()
    
    def renew(self):
        self.position = np.random.uniform(COEF_MIN, COEF_MAX, self.flowerSet.data.numX)
        self.visitNum = 0
        self.evaluate()
    
    def evaluate(self):
        self.value = np.sum((self.flowerSet.data.Ynorm - self.position @ self.flowerSet.data.Xnorm.T)**2)