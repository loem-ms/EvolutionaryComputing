import math

class Field(object):
    def __init__(self, filename):
        with open(filename, 'r') as fi:
            reader = fi.readlines()
        nodes = []
        for point in reader:
            xy = point.split(',')
            nodes.append((float(xy[0]),float(xy[1])))

        self.nodeNum = len(nodes)
        self.distance = [[0. for _ in range(self.nodeNum)] for _ in range(self.nodeNum)]
        self.pheromone = [[0. for _ in range(self.nodeNum)] for _ in range(self.nodeNum)]

        for i in range(self.nodeNum):
            for j in range(self.nodeNum):
                self.distance[i][j] = math.sqrt((nodes[i][0]-nodes[j][0])**2+(nodes[i][1]-nodes[j][1])**2)
        print("Distance list")
        for i in range(self.nodeNum):
            for j in range(self.nodeNum):
                print("%8.3f"%(self.distance[i][j]), end='')
            print("\n")