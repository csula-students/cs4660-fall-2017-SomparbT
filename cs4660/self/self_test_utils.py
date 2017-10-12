"""
for self test utils

"""

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from search import searches
from graph import graph
from graph import utils
from io import open

g1 = graph.AdjacencyList()
g2 = graph.AdjacencyList()
#g1 = AdjacencyMatrix()
#g2 = AdjacencyMatrix()
#g1 = ObjectOriented()
#g2 = ObjectOriented()
    
"""    
graph1 = graph.construct_graph_from_file(g1, '../test/fixtures/graph-1.txt')
graph2 = graph.construct_graph_from_file(g2, '../test/fixtures/graph-2.txt')
    

print(utils.convert_edge_to_grid_actions([
    graph.Edge(graph.Node(utils.Tile(1, 2, "##")), graph.Node(utils.Tile(2, 2, "##")), 1),
    graph.Edge(graph.Node(utils.Tile(1, 2, "##")), graph.Node(utils.Tile(1, 3, "##")), 1),
    graph.Edge(graph.Node(utils.Tile(1, 2, "##")), graph.Node(utils.Tile(0, 2, "##")), 1),
    graph.Edge(graph.Node(utils.Tile(1, 2, "##")), graph.Node(utils.Tile(1, 1, "##")), 1),
    ]))   # -> SENW
"""

file_path = '../test/fixtures/grid-1.txt'

file = open(file_path, encoding='utf-8')
text = file.read()
lines = text.split('\n')
grid = []
for line in lines:
    if line:
        #from_node_number, to_node_number, weight = map(int, line.split(':'))
        #print(utils.chunkstring(line[1:-1], 2))
        grid.append([line[i:i+2] for i in range(1, len(line[1:-1]), 2)])
        #print(line)
        
grid = grid[1:-1]
print(grid)
file.close()

for y in range(len(grid)):
    for x in range (len(grid[0])):
        print (grid[x][y])

test = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

for y in range(len(test[1:-1])):
    print(y)

print(utils.parse_grid_file(g1, file_path).adjacency_list[graph.Node(utils.Tile(3, 0, "@1"))])