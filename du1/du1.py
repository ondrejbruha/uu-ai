import random
import numpy as np
import cv2 as cv
import math


def generate_random_population(num):
    population = []
    for i in range(num):
        random_number = 1##random.randint(0, 1)
        population.append(random_number)
    population[math.floor(num/2)] = 0
    population[num - 1] = 0
    population[0] = 0
    return population


def step(prev):
    plus = []
    num = random.randint(-2, 2)
    for i in range(len(prev)):
        if i < len(prev) - num:
            plus.append(prev[i] * prev[i + num])
        else:
            plus.append(prev[i] * prev[num])
    return plus


def main():
    population = [generate_random_population(100)]
    steps = 100
    for i in range(steps):
        population.append(step(population[i]))
    arr = np.array(population)
    arr = arr * 255
    cv.imwrite("output.png", arr)


if __name__ == '__main__':
    main()
