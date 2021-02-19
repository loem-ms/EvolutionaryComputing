import random

import config
import Colony
import Field

class Ant(object):
    def __init__(self, argColony):
        self.colony = argColony
        self.route = [0 for _ in range(self.colony.field.nodeNum)]
        self._candidate = [0 for _ in range(self.colony.field.nodeNum)]
        self.totalDis = 0.

    def selectRoute(self):
        for i in range(1, self.colony.field.nodeNum):
            self._candidate[i] = 1

        self.totalDis = 0.
        for i in range(self.colony.field.nodeNum-2):
            denom = 0.
            for j in range(1, self.colony.field.nodeNum):
                if self._candidate[j] == 1:
                    denom += self.colony.nume[self.route[i]][j]
            
            next_node = -1
            if (denom != 0.) and (random.random() <= config.PHERO_R):
                r = random.random()
                for next_node in range(1, self.colony.field.nodeNum):
                    if self._candidate[next_node] == 1:
                        prob = self.colony.nume[self.route[i]][next_node] / denom
                        if r <= prob:
                            break
                        r -= prob
                if next_node == self.colony.field.nodeNum:
                    next_node = -1
            
            if next_node == -1:
                next_node2 = random.randint(0,self.colony.field.nodeNum-i-2) 
                for next_node in range(1, self.colony.field.nodeNum-1):
                    if self._candidate[next_node] == 1:
                        if next_node2 == 0:
                            break
                        else:
                            next_node2 -= 1
            self.route[i+1] = next_node
            self._candidate[next_node] = 0
            self.totalDis += self.colony.field.distance[self.route[i]][next_node]
        
        # last node
        for next_node in range(1, self.colony.field.nodeNum):
            if self._candidate[next_node] == 1:
                break
        
        self.route[self.colony.field.nodeNum-1] = next_node
        self.totalDis += self.colony.field.distance[self.route[self.colony.field.nodeNum-2]][next_node]
        self.totalDis += self.colony.field.distance[next_node][0]
    
    def putPheromone(self):
        p = config.PHERO_Q / self.totalDis
        for i in range(self.colony.field.nodeNum-1):
            if self.route[i] < self.route[i+1]:
                self.colony.field.pheromone[self.route[i]][self.route[i+1]] += p
            else:
                self.colony.field.pheromone[self.route[i+1]][self.route[i]] += p
        self.colony.field.pheromone[0][self.route[self.colony.field.nodeNum-1]] += p