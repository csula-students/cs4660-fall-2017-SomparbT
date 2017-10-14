"""
for self test graph

"""

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from graph import graph

#g = AdjacencyList()
#g = AdjacencyMatrix()
g1 = graph.ObjectOriented()
    
graph1 = graph.construct_graph_from_file(g1, '../test/fixtures/graph-1.txt')
    
    
print(graph1.distance(graph.Node(4), graph.Node(7))) # -> 1


"""

print(graph.adjacency_matrix)
print(graph.nodes)
print(graph.neighbors(Node(4)))
print(graph.add_node(Node(1)))
print(graph.add_node(Node(6)))
print(graph.add_node(Node(11)))
print(graph.nodes)
print(graph.remove_node(Node(6)))
print(graph.nodes)
print(graph.neighbors(Node(9)))
print(graph.neighbors(Node(1)))
print(graph.neighbors(Node(20)))
print(graph.adjacent(Node(1), Node(2)))#true
print(graph.adjacent(Node(20), Node(2)))#not exist
print(graph.adjacent(Node(1), Node(5)))#false
print(graph.add_node(Node(1)))#False
print(graph.add_node(Node(20)))#True
print(graph.remove_node(Node(2)))#True
print(graph.add_edge(Edge(Node(0), Node(3), 9)))
print(graph.remove_edge(Edge(Node(0), Node(10), 9)))
""" 