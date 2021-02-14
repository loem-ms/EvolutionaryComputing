import random
import math
import config

class Individuale(object):
    def __init__(self):
        self.chrom = [random.randint(0,1) for _ in range(config.N)]
        self.fitness = 0.0
        self.capacity = 0.0
    
    def evaluate(self):
        self.fitness = 0.0
        self.capacity = 0.0
        for i in range(config.N):
            self.fitness += (self.chrom[i]) * config.ITEMS[i][1]
            self.capacity += (self.chrom[i]) * config.ITEMS[i][0]
        if self.capacity > config.B:
            self.fitness = 0.0
    
    def crossover(self, p1, p2):
        point = random.randint(0,config.N-2)
        for i in range(point):
            self.chrom[i] = p1.chrom[i]
        for i in range(point, config.N):
            self.chrom[i] = p2.chrom[i]

    def mutate(self):
        for i in range(config.N):
            if random.random() < config.MUTATE_PROB:
                self.chrom[i] = 1 - self.chrom[i]