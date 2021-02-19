import config
from Colony import *

def main():
    colony = Colony('input.txt')
    for i in range(config.ITERATION_NUM):
        colony.selectRoute()
        colony.renewPheromone()

    colony.printPheromone()
    del colony


if __name__ == "__main__":
    main()