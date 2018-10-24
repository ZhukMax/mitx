from graphs.Digraph import Digraph
from graphs.Edge import Edge
from graphs.Node import Node


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


def print_path(path):
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


# Depth First Search
def dfs(graph, start, end, path, shortest, to_print=False):
    path = path + [start]
    if to_print:
        print('Current DFS path:', print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:
            if shortest is None or len(path) < len(shortest):
                new_path = dfs(graph, node, end, path, shortest, to_print)
                if new_path is not None:
                    shortest = new_path
        elif to_print:
            print('Already visited', node)
    return shortest


def shortest_path(graph, start, end, to_print=False):
    return dfs(graph, start, end, [], None, to_print)


# Breadth First Search
def bfs(graph, start, end, to_print=False):
    init_path = [start]
    path_queue = [init_path]
    if to_print:
        print('Current BFS path:', print_path(path_queue))

    while len(path_queue) != 0:
        tmp_path = path_queue.pop(0)
        print('Current BFS path:', print_path(tmp_path))
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path

        for next_node in graph.children_of(last_node):
            if next_node not in tmp_path:
                new_path = tmp_path + [next_node]
                path_queue.append(new_path)

    return None


def shortest_bfs_path(graph, start, end, to_print=False):
    return bfs(graph, start, end, to_print)


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
