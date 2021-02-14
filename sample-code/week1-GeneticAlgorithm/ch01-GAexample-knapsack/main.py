import config
from Population import Population
import matplotlib.pyplot as plt

def main():

    meanFitness = []
    maxFitness = []
    pop = Population()
    for i in range(config.GEN_MAX):
        pop.alternate()
        if i%100 == 0:
            print("Generation #%3d : Fitness= %f (Capacity:%4d/%4d)"%(i, pop.ind[0].fitness, pop.ind[0].capacity, config.B))
        meanFitness.append(pop.getMeanFitness())
        maxFitness.append(pop.ind[0].fitness)
    

    plt.plot(list(range(config.GEN_MAX)), meanFitness)
    plt.plot(list(range(config.GEN_MAX)), maxFitness)
    plt.legend(['mean fitness', 'max fitness'])
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.title('Knapsack N='+str(config.N))
    plt.show()
    
    pop.printResult()
    del pop

if __name__ == "__main__":
    main()