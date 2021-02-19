import random

GEN_MAX     = 500
POP_SIZE    = 500
ELITE       = 1
MUTATE_PROB = 0.01
N           = 200
B           = 800

weights = [random.randint(1,10) for _ in range(N)]
values = [random.randint(10, 100) for _ in range(N)]

ITEMS       = [(weight, value) for (weight,value) in zip(weights,values)]