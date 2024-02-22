import random
import numpy as np
import cv2 as cv


def generate_random_population(num):
    population = []
    for i in range(num):
        random_number = random.randint(1, 2)
        if i % random_number == 0:
            population.append(1)
        else:
            population.append(0)
    return population


def step(prev):
    plus = []
    for i in range(len(prev)):
        if i < len(prev) - 1:
            plus.append(prev[i] * prev[i + 1])
        else:
            plus.append(prev[i] * prev[0])
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
