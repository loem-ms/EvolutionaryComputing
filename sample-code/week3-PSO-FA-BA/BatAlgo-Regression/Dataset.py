import numpy as np

class Dataset(object):
    def __init__(self, filename):
        with open(filename, 'r') as fi:
            reader = fi.read().splitlines()
        self.X = []
        self.Y = []
        for line in reader:
            data = line.split(',')
            self.X.append([float(i) for i in data[:-1]])
            self.Y.append(float(data[-1]))
        self.X = np.array(self.X)
        self.Y = np.array(self.Y)
        self.numData = self.X.shape[0]
        self.numX = self.X.shape[1]
        self.meanX = np.mean(self.X,axis=0)
        self.stdX = np.std(self.X,axis=0)
        self.meanY = np.mean(self.Y,axis=0)
        self.stdY = np.std(self.Y,axis=0)

        self.Xnorm = (self.X-self.meanX)/self.stdX
        self.Ynorm = (self.Y-self.meanY)/self.stdY
    
    def printDataInfo(self):
        print("X : ",type(self.X)," shape:",self.X.shape)
        print("Y : ",type(self.Y)," shape:",self.Y.shape)

    def setCoef(self, coef_):
        self.coef = self.stdY / self.stdX * coef_
        self.constant = self.meanY - self.coef @ self.meanX
    
    def printEquation(self):
        print("Regression Equation: y = ", end='')
        for i in range(self.numX):
            print("%.3f X%d + "%(self.coef[i], i+1), end='')
        print("%.3f"%(self.constant))