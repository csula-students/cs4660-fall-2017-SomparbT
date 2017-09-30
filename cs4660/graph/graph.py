"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that graph object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """

    file = open(file_path, encoding='utf-8')
    text = file.read()
    lines = text.split('\n')
    for line in lines[1:]:
        if line:
            from_node_number, to_node_number, weight = map(int, line.split(':'))
            from_node = Node(from_node_number)
            to_node = Node(to_node_number)
            edge = Edge(from_node, to_node, weight)
            graph.add_node(from_node)
            graph.add_node(to_node)
            graph.add_edge(edge)
    file.close();
    return graph

class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}

    def adjacent(self, node_1, node_2):
        neighbors = self.neighbors(node_1)
        for neighbor in neighbors:
            if neighbor == node_2:
                return True
        return False
        

    def neighbors(self, node):
        if node not in self.adjacency_list:
            return [] # node not exists
        return list(map((lambda edge: edge.to_node), self.adjacency_list[node]))

    def add_node(self, node):
        if node in self.adjacency_list:
            return False #node exists
        self.adjacency_list[node] = []
        return True

    def remove_node(self, node):
        if node not in self.adjacency_list:
            return False #node not exists
        del self.adjacency_list[node]
        #remove edge that connected to removed node
        for edges in self.adjacency_list.values():
            for edge in edges:
                if edge.to_node == node:
                    self.remove_edge(edge)
        return True

    def add_edge(self, edge):
        if edge.from_node not in self.adjacency_list or edge.to_node not in self.adjacency_list:
            return False #edge has invalid node 
        adj_edges = self.adjacency_list[edge.from_node]
        for adj_edge in adj_edges:
            if edge == adj_edge:
                return False #edge exist
        adj_edges.append(edge)
        return True

    def remove_edge(self, edge):
        adj_edges = self.adjacency_list[edge.from_node]
        if edge not in adj_edges:
            return False
        adj_edges.remove(edge)
        return True

    def distance(self, node_1, node_2):
        pass

class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        if node_1 not in self.nodes or node_2 not in self.nodes:
            return False
        node_1_index = self.__get_node_index(node_1)
        node_2_index = self.__get_node_index(node_2)
        return True if self.adjacency_matrix[node_1_index][node_2_index] != 0 else False

    def neighbors(self, node):
        if node not in self.nodes:
            return []
        neighbors = []
        node_index = self.__get_node_index(node)
        neighbor_weights = self.adjacency_matrix[node_index]
        for index, existing_node in enumerate(self.nodes):
            if neighbor_weights[index] != 0:
                neighbors.append(existing_node)         
        neighbors.sort(key=lambda node: node.data)
        return neighbors

    def add_node(self, node):
        if node in self.nodes:
            return False
        self.nodes.append(node)
        for existing_weights in self.adjacency_matrix:
            existing_weights.extend([0])
        self.adjacency_matrix.extend([[0] * len(self.nodes)])    
        return True

    def remove_node(self, node):
        if node not in self.nodes:
            return False
        node_index = self.__get_node_index(node)
        del self.nodes[node_index]
        #update matrix
        for existing_weights in self.adjacency_matrix:
            #delete column that other nodes connected to removed note
            del existing_weights[node_index]
        #delete row that contains removed node    
        del self.adjacency_matrix[node_index]
        return True

    def add_edge(self, edge):
        if edge.from_node not in self.nodes or edge.to_node not in self.nodes:
            return False 
        node_1_index = self.__get_node_index(edge.from_node)
        node_2_index = self.__get_node_index(edge.to_node)
        if self.adjacency_matrix[node_1_index][node_2_index] != 0:
            return False #edge exists
        self.adjacency_matrix[node_1_index][node_2_index] = edge.weight #update weight
        return True

    def remove_edge(self, edge):
        if edge.from_node not in self.nodes or edge.to_node not in self.nodes:
            return False
        node_1_index = self.__get_node_index(edge.from_node)
        node_2_index = self.__get_node_index(edge.to_node)
        if self.adjacency_matrix[node_1_index][node_2_index] == 0:
            return False #edge not exist
        self.adjacency_matrix[node_1_index][node_2_index] = 0
        return True

    def distance(self, node_1, node_2):
        pass

    def __get_node_index(self, node):
        """helper method to find node index"""
        return self.nodes.index(node)

class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        for edge in self.edges:
            if edge.from_node == node_1 and edge.to_node == node_2:
                return True
        return False

    def neighbors(self, node):
        neighbors = set()
        for edge in self.edges:
            if edge.from_node == node:
                neighbors.add(edge.to_node)
        return list(neighbors)

    def add_node(self, node):
        if node in self.nodes:
            return False
        self.nodes.append(node)
        return True

    def remove_node(self, node):
        if node not in self.nodes:
            return False
        self.nodes.remove(node)
        #remove edges that connect with removed node
        for edge in self.edges:
            if edge.from_node == node or edge.to_node == node:
                self.remove_edge(edge)
        return True

    def add_edge(self, edge):
        if edge in self.edges:
            return False
        self.edges.append(edge)
        return True

    def remove_edge(self, edge):
        if edge not in self.edges:
            return False
        self.edges.remove(edge)
        return True

    def distance(self, node_1, node_2):
        pass

"""
g = AdjacencyList()
graph = construct_graph_from_file(g, '../test/fixtures/graph-1.txt')
"""

"""
g = AdjacencyMatrix()
graph = construct_graph_from_file(g, '../test/fixtures/graph-1.txt')

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
"""

"""
g = ObjectOriented()
graph = construct_graph_from_file(g, '../test/fixtures/graph-1.txt')
"""
"""
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
