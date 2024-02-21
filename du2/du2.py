import random
from matplotlib import pyplot as plt


def distance(point1, point2):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5


class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rat = 0
        self.type = random.choice(["a", "b"])


class Population:
    def __init__(self, size, agent_count, diam, threshold):
        self.size = size
        self.agent_count = agent_count
        self.population = []
        self.diam = diam
        self.count = 0
        self.threshold = threshold

    def initialize(self):
        for i in range(self.agent_count):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            agent = Agent(x, y)
            self.population.append(agent)

    def rate(self):
        for agent in self.population:
            all_agents = 0
            same_agents = 0
            for other in self.population:
                if agent != other and distance(agent, other) <= self.diam:
                    if agent.type == other.type:
                        same_agents += 1
                    all_agents += 1
            agent.rat = same_agents / all_agents

    def chose(self, tol):
        arr = []
        for agent in self.population:
            if agent.rat < tol:
                arr.append(agent)
        if len(arr) == 0:
            return None
        return random.choice(arr)

    def step(self):
        x = None
        y = None
        self.count = 0
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            is_free = True
            for other in self.population:
                if other.rat < self.threshold:
                    self.count = self.count + 1
                if x == other.x and y == other.y:
                    is_free = False
            if is_free:
                break
        a = self.chose(self.threshold)
        if a is None:
            return
        a.x = x
        a.y = y


def plot(popul, indx):
    x_a = []
    x_b = []
    y_b = []
    y_a = []
    for agent in popul.population:
        if agent.type == "a":
            x_a.append(agent.x)
            y_a.append(agent.y)
        else:
            x_b.append(agent.x)
            y_b.append(agent.y)
    plt.scatter(x_a, y_a, color='red', label="a")
    plt.scatter(x_b, y_b, color='blue', label="b")
    plt.legend()
    plt.savefig(f"./PLT/plots_{indx}.png")
    plt.close()


if __name__ == "__main__":
    pop = Population(50, 600, 10, 0.5)
    iters = 1000
    pop.initialize()
    pop.rate()
    pop.step()
    counts = []
    for i in range(iters):
        pop.rate()
        pop.step()
        counts.append(pop.count)
        if i % 10 == 0:
            plot(pop, i)
    plot(pop, iters - 1)
    plt.plot(counts)
    plt.savefig("./PLT/line.png")

## vysledny graf hustší
## pocet spokojenych / nespokojenych v case
