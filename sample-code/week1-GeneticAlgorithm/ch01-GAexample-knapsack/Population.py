import config
from Individual import Individuale
import random

class Population(object):
    def __init__(self):
        self.ind = []
        self.nextInd = []
        for i in range(config.POP_SIZE):
            self.ind.append(Individuale())
            self.nextInd.append(Individuale())
        self.evaluate()
    
    def evaluate(self):
        for i in range(config.POP_SIZE):
            self.ind[i].evaluate();
        self.ind = sorted(self.ind, key=lambda x: x.fitness, reverse=True)
    
    def alternate(self):
        for i in range(config.ELITE):
            for j in range(config.N):
                self.nextInd[i].chrom[j] = self.ind[i].chrom[j]

        for i in range(config.ELITE, config.POP_SIZE):
            p1 = self.select()
            p2 = self.select()
            self.nextInd[i].crossover(self.ind[p1], self.ind[p2])
        
        for i in range(1, config.POP_SIZE):
            self.nextInd[i].mutate()
        
        tmp = self.ind
        self.ind = self.nextInd
        self.nextInd = tmp

        self.evaluate()
    
    def select(self):
        denom = config.POP_SIZE * (config.POP_SIZE + 1) / 2.
        r = random.random()
        for rank in range(1, config.POP_SIZE):
            prob = (config.POP_SIZE - rank + 1)/denom
            if r <= prob:
                break
            r -= prob
            
        return rank-1
    
    def printResult(self):
        print("In knapsack: ", end='')
        for i in range(config.N):
            if self.ind[0].chrom[i] == 1:
                print("%d "%(i+1), end='')
        
        print("\nValue = %f\n"%(self.ind[0].fitness))
        print("\nSize  = %f\n"%(self.ind[0].capacity))
    
    def getMeanFitness(self):
        return sum([i.fitness for i in self.ind])/config.POP_SIZE