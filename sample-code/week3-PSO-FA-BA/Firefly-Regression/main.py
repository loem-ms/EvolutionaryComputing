from config import *
from Population import *

def main():
    pop = Population('input.txt')
    for t in range(TIME_MAX):
        pop.move()
        print("Time: %3d : Best Intensity: %f"%(t, pop.bestIntensity))
    pop.printResult()
    del pop

if __name__ == "__main__":
    main()