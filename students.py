from Edge import Edge
from Graph import Graph
from Node import Node

nodes = [Node("ABC"), Node("ACB"), Node("BAC"), Node("BCA"), Node("CAB"), Node("CBA")]

g = Graph()
for n in nodes:
    g.add_node(n)

g.add_edge(Edge(g.get_node("ABC"), g.get_node("ACB")))
g.add_edge(Edge(g.get_node("ABC"), g.get_node("BAC")))
g.add_edge(Edge(g.get_node("CAB"), g.get_node("ACB")))
g.add_edge(Edge(g.get_node("BCA"), g.get_node("BAC")))
g.add_edge(Edge(g.get_node("BCA"), g.get_node("CBA")))
g.add_edge(Edge(g.get_node("CAB"), g.get_node("CBA")))

print(g)
