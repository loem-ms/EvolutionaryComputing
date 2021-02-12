import config
from Population import Population

def main():
    pop = Population()
    for i in range(config.GEN_MAX):
        pop.alternate()
        if i%1 == 0:
            print("Gen. #%3d : Fitness= %f"%(i, pop.ind[0].fitness))
    
    pop.printResult()
    del pop

if __name__ == "__main__":
    main()