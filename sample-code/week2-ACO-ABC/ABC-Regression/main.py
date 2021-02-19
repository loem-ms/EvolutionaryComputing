from config import *
from Flowerset import *

def main():
    flowerSet = Flowerset('input.txt')
    for i in range(REPEAT_NUM):
        flowerSet.employedBeePhase()
        flowerSet.onlookerBeePhase()
        flowerSet.scoutBeePhase()
        flowerSet.saveBestPosition()
        print("Iteration #%2d: Best Evaluation Value = %f Best Pos"%(i, flowerSet.bestValue), flowerSet.bestPos)
    flowerSet.printResult()
    del flowerSet

if __name__=="__main__":
    main()