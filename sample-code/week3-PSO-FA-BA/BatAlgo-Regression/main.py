from config import *
from Population import *

def main():
    pop = Population('input.txt')
    for t in range(TIME_MAX):
        pop.move(t)
        print("Time: %3d : Best Value: %f"%(t, pop.bestValue))
    pop.printResult()
    del pop

if __name__ == "__main__":
    main()