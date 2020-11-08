# Lecture: https://youtu.be/Qwg4b6bKyW0

"""
You are given an undirected graph with its maximum degree (the degree of a node
is the number of edges connected to the node).

You need to write a function that can take an undirected graph as its argument
and color the graph legally (a legal graph coloring is when no adjacent nodes
have the same color).

The number of colors necessary to complete a legal coloring is always one more
than the graph's maximum degree.

*Note: We can color a graph in linear time and space. Also, make sure that your
solution can handle a loop in a reasonable way.*
"""
# Definition for a graph node.
class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def color_graph(graph, colors):
    # Your code here

# Glenna: We didn't get to demonstration_1.py today, but here's some starter code to build a graph and test

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)

b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]

color_graph(graph, ["red", "blue", "green"])

for node in graph:
    print(f"{node.label} has color {node.color}. Neighbors: {[n.label for n in node.neighbors]}")