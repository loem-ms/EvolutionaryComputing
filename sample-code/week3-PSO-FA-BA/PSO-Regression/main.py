#import matplotlib.pyplot as plt
from config import *
from Swarm import *

def main():
    #errors = []
    swarm = Swarm('input.txt')
    for t in range(TIME_MAX):
        swarm.move()
        #errors.append(swarm.gBestValue)
        print("Time: %d : Best Value: %f"%(t, swarm.gBestValue))
    swarm.printResult()
    #plt.plot(list(range(TIME_MAX)), errors)
    #plt.show()
    del swarm

if __name__ == "__main__":
    main()