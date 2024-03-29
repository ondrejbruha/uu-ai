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


def get_color_count(node_colors):
    color_dict = {}
    for col in node_colors:
        color_dict[col] = col
    return len(color_dict.keys()), color_dict


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
            num, _ = get_color_count(node_colors)
            val = coloring(g, num - 1, steps - i)
            if val["is_valid"]:
                node_colors = val["colors"]
        if is_valid:
            break
    count, color_dict = get_color_count(node_colors)
    return {
        "colors": node_colors,
        "is_valid": is_valid,
        "color_dict": color_dict,
        "count": count
    }


def get_color():
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = "#"
    for i in range(6):
        color.join(random.choice(symbols))
    return color


def main():
    num_colors = 2000
    g = readdimacs("r250.5.col.txt")  ##nx.erdos_renyi_graph(20, 0.5)
    res = coloring(g, num_colors, 100000)
    print("Colors: " + str(res["colors"]))
    print("Color Dict: " + str(res["color_dict"]))
    print("Is Valid: " + str(res["is_valid"]))
    print("Count: " + str(res["count"]))
    nx.draw(g, with_labels=True)
    plt.draw()
    plt.savefig("coloring.png")


if __name__ == "__main__":
    main()
