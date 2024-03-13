from deap import base, creator, tools, algorithms
import random
from matplotlib import pyplot as plt
import numpy as np


def plotterrain(t, filename):
    fig, ax = plt.subplots()

    x = range(len(t))
    sea = [5 for i in range(len(t))]

    ax.fill_between(x, sea, color="turquoise")
    ax.fill_between(x, t, color="sandybrown")
    ax.axis("off")
    plt.savefig(filename)
    plt.close()

def evaluate(population):
    count_under = 0
    count_above = 0
    max_depth = 0
    for individual in population:

        if individual < 5:
            max_depth = max(max_depth,individual - 5)
            count_under = count_under + 1
        else:
            count_above = count_above + 1
    return len(population), 1.0/ sum(population), count_under, count_above, max_depth

def main():
    count = 1000
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox()

    toolbox.register("attr_float", random.randint, 0, 10)
    toolbox.register("individual", tools.initRepeat, creator.Individual,
                     toolbox.attr_float, n=count)
    ind1 = toolbox.individual()
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    pop = toolbox.population(n=count)
    toolbox.register("evaluate", evaluate)
    counter = 1
    x = range(count)
    y = []
    for individual in pop:
        if counter%100 == 0:
            plotterrain(individual, filename=f"./img/du4_individual_{counter}.png")
        counter = counter + 1
        y.append(individual[1])
        print(evaluate(individual))
    plt.close()
    plt.plot(x,y)
    plt.savefig("./img/du4.png")


if __name__ == "__main__":
    main()
