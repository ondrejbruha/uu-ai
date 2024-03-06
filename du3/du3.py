import networkx as nx
import matplotlib.pyplot as plt
import random


def readdimacs(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    Gd = nx.Graph()

    for line in lines:
        if line[0] == "e":
            vs = [int(s) for s in line.split() if s.isdigit()]
            Gd.add_edge(vs[0] - 1, vs[1] - 1)
    return Gd


def is_coloring(g: nx.Graph, color: list):
    output = True
    for i in g.nodes():
        for j in g.neighbors(i):
            if g.has_edge(i, j) and color[j] == color[i]:
                output = False
    return output


def coloring(g: nx.Graph, color_num: int, steps: int):
    colors = []
    node_colors = []
    is_valid = False
    for i in range(color_num):
        colors.append(i)
    for i in range(steps):
        print("Step " + str(i))
        node_colors = []
        for _ in g.nodes():
            node_colors.append(random.choice(colors))
        is_valid = is_coloring(g, node_colors)
        if is_valid and i < steps:
            val = coloring(g, color_num - 1, steps)
            if val["is_valid"]:
                node_colors = val["colors"]
        if is_valid:
            break
    color_dict = {}
    for col in node_colors:
        color_dict[col] = col
    count = len(color_dict.keys())
    return {
        "colors": node_colors,
        "is_valid": is_valid,
        "color_dict": color_dict,
        "count": count
    }


def main():
    colmap = ['red', 'green', 'blue', 'black', 'white', 'yellow', 'gray', 'pink', 'purple',
              'orange']
    g = readdimacs("flat300_28_0.col.txt")##nx.erdos_renyi_graph(20, 0.5)
    res = coloring(g, len(colmap), 10000)
    print(res)
    colors = [colmap[c] for c in res["colors"]]
    nx.draw(g, node_color=colors, with_labels=True)
    plt.draw()
    plt.savefig("coloring.png")


if __name__ == "__main__":
    main()
