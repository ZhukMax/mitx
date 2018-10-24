from Digraph import Digraph
from Edge import Edge
from Graph import Graph
from Node import Node


def build_city_graph(graph_type):
    g = graph_type()
    for name in ['Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles']:
        g.add_node(Node(name))

    g.add_edge(Edge(g.get_node('Boston'), g.get_node('Providence')))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('Boston')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('New York'), g.get_node('Chicago')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Denver')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Los Angeles'), g.get_node('Boston')))
    return g


print(build_city_graph(Graph))
print('\n\n')
print(build_city_graph(Digraph))
