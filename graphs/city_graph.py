from graphs.Digraph import Digraph
from graphs.Edge import Edge
from graphs.Node import Node
from graphs.search import shortest_path, print_path, shortest_bfs_path


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


def test_sp(source, destination, func=shortest_path):
    g = build_city_graph(Digraph)
    sp = func(g, g.get_node(source), g.get_node(destination), to_print=True)
    if sp is not None:
        print('Shortest path from', source, 'to', destination, 'is', print_path(sp))
    else:
        print('There is no path from', source, 'to', destination)


test_sp('Chicago', 'Boston')
print('#' * 12)
print('\n')
test_sp('Boston', 'Phoenix')
print('#' * 12)
print('\n')
test_sp('Boston', 'Phoenix', shortest_bfs_path)
