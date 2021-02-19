from config import *
from Flowerset import *

def main():
    print("Initialization")
    flowerSet = Flowerset('input.txt')
    flowerSet.printReport()
    for i in range(ITERATION_NUM):
        #print("Emploed BEE Phase")
        flowerSet.employedBeePhase()
        #print("Onlooker BEE Phase")
        flowerSet.onlookerBeePhase()
        #print("Scout Bee Phase")
        flowerSet.scoutBeePhase()
        #print("save best position")
        flowerSet.saveBestPosition()
        print("Iteration #%2d: Best Evaluation Value = %f Best Pos"%(i, flowerSet.bestValue), flowerSet.bestPos)
    flowerSet.printResult()
    del flowerSet

if __name__=="__main__":
    main()