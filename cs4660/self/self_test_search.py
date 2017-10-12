"""
for self test search

"""

import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from search import searches
from graph import graph
from graph import utils

g1 = graph.AdjacencyList()
g2 = graph.AdjacencyList()
g3 = graph.AdjacencyList()
g4 = graph.AdjacencyList()
g5 = graph.AdjacencyList()
g6 = graph.AdjacencyList()
g7 = graph.AdjacencyList()
"""
g1 = graph.AdjacencyMatrix()
g2 = graph.AdjacencyMatrix()
g3 = graph.AdjacencyMatrix()
g4 = graph.AdjacencyMatrix()
g5 = graph.AdjacencyMatrix()
g6 = graph.AdjacencyMatrix()
g7 = graph.AdjacencyMatrix()

g1 = graph.ObjectOriented()
g2 = graph.ObjectOriented()
g3 = graph.ObjectOriented()
g4 = graph.ObjectOriented()
g5 = graph.ObjectOriented()
g6 = graph.ObjectOriented()
g7 = graph.ObjectOriented()
"""  
graph1 = graph.construct_graph_from_file(g1, '../test/fixtures/graph-1.txt')
graph2 = graph.construct_graph_from_file(g2, '../test/fixtures/graph-2.txt')
graph3 = utils.parse_grid_file(g3, '../test/fixtures/grid-1.txt')
graph4 = utils.parse_grid_file(g4, '../test/fixtures/grid-2.txt')
graph5 = utils.parse_grid_file(g5, '../test/fixtures/grid-3.txt')
graph6 = utils.parse_grid_file(g6, '../test/fixtures/grid-4.txt')
graph7 = utils.parse_grid_file(g7, '../test/fixtures/grid-5.txt')

    

result = searches.bfs(graph1, graph.Node(1), graph.Node(8))   
print(result)
print(result == [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1),
                    graph.Edge(graph.Node(10), graph.Node(8), 1)
                ])
result = searches.bfs(graph1, graph.Node(1), graph.Node(10))   
print(result)
print(result == [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1)
                ])
result = searches.bfs(graph1, graph.Node(1), graph.Node(5))   
print(result)
print(result == [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1)
                ])
result = searches.bfs(graph2, graph.Node(0), graph.Node(5))   
print(result)
print(result == [
                    graph.Edge(graph.Node(0), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(5), 11)
                ])
result = searches.bfs(graph2, graph.Node(0), graph.Node(2))   
print(result)
print(result == [
                    graph.Edge(graph.Node(0), graph.Node(1), 4),
                    graph.Edge(graph.Node(1), graph.Node(2), 7)
                ])                                                               

print()

result = searches.dfs(graph1, graph.Node(1), graph.Node(8))   
print(result)
print(result == [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1),
                    graph.Edge(graph.Node(5), graph.Node(0), 1),
                    graph.Edge(graph.Node(0), graph.Node(7), 1),
                    graph.Edge(graph.Node(7), graph.Node(8), 1)
                ])
result = searches.dfs(graph1, graph.Node(1), graph.Node(10))   
print(result)
print(result == [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1),
                    graph.Edge(graph.Node(5), graph.Node(0), 1),
                    graph.Edge(graph.Node(0), graph.Node(7), 1),
                    graph.Edge(graph.Node(7), graph.Node(10), 1)
                ])
result = searches.dfs(graph1, graph.Node(1), graph.Node(5))   
print(result)
print(result == [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1)
                ])
result = searches.dfs(graph2, graph.Node(0), graph.Node(5))   
print(result)
print(result == [
                    graph.Edge(graph.Node(0), graph.Node(1), 4),
                    graph.Edge(graph.Node(1), graph.Node(2), 7),
                    graph.Edge(graph.Node(2), graph.Node(5), 2)
                ])
result = searches.dfs(graph2, graph.Node(0), graph.Node(2))   
print(result)
print(result == [
                    graph.Edge(graph.Node(0), graph.Node(1), 4),
                    graph.Edge(graph.Node(1), graph.Node(2), 7)
                ])           

print()

result = searches.dijkstra_search(graph1, graph.Node(1), graph.Node(8))   
print(result)
print(result == [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1),
                    graph.Edge(graph.Node(10), graph.Node(8), 1)
                ])
result = searches.dijkstra_search(graph1, graph.Node(1), graph.Node(10))   
print(result)
print(result == [
                    graph.Edge(graph.Node(1), graph.Node(3), 1),
                    graph.Edge(graph.Node(3), graph.Node(10), 1)
                ])
result = searches.dijkstra_search(graph1, graph.Node(1), graph.Node(5))   
print(result)
print(result == [
                    graph.Edge(graph.Node(1), graph.Node(2), 1),
                    graph.Edge(graph.Node(2), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 1)
                ])
result = searches.dijkstra_search(graph2, graph.Node(1), graph.Node(5))   
print(result)
print(result == [
                    graph.Edge(graph.Node(1), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 5)
                ])
result = searches.dijkstra_search(graph2, graph.Node(0), graph.Node(5))   
print(result)
print(result == [
                    graph.Edge(graph.Node(0), graph.Node(6), 3),
                    graph.Edge(graph.Node(6), graph.Node(4), 1),
                    graph.Edge(graph.Node(4), graph.Node(5), 5)
                ])           

print()

result = utils.convert_edge_to_grid_actions(
                    searches.a_star_search(
                        graph3,
                        graph.Node(utils.Tile(3, 0, "@1")),
                        graph.Node(utils.Tile(4, 4, "@6"))
                    )
                )
print(result)                
print(result == "SSSSE")

result = utils.convert_edge_to_grid_actions(
                searches.a_star_search(
                    graph4,
                    graph.Node(utils.Tile(3, 0, "@1")),
                    graph.Node(utils.Tile(13, 0, "@8"))
                )
            )
print(result)
print(result == "SSSSEEEEEEEEEEEEENNWNWNW") 

result = utils.convert_edge_to_grid_actions(
                searches.a_star_search(
                    graph5,
                    graph.Node(utils.Tile(3, 0, "@1")),
                    graph.Node(utils.Tile(2, 7, "@2"))
                )
            )
print(result)
print(result == "SSSSEESESSWWWW") 

result = utils.convert_edge_to_grid_actions(
            searches.a_star_search(
                graph6,
                graph.Node(utils.Tile(4, 0, "@1")),
                graph.Node(utils.Tile(6, 201, "@4"))
            )
        )
print(result)
print(result == "SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSESE")

result = utils.convert_edge_to_grid_actions(
            searches.a_star_search(
                graph7,
                graph.Node(utils.Tile(4, 0, "@1")),
                graph.Node(utils.Tile(201, 206, "@5"))
            )
        )
print(result)
print(result == "SSSSSSSSSSEESSEESESESSEESSEESESESESESSEESESESESESESSESEESESESSESEESSEESSEESESESESESSESEESSESESEESSESEESESSESEESESESESESSEESESESESESESESESESSEESESESESESESSEESSEESESSESEESSEESESSEESESESESESESSEESESESSEESESSESEESSEESESESESSEESSESEESESSESESESESEESSEESESESESESESESESESESESESESESESSEESESSEESSEESESESESSEESESESSEESESESSEESESESESESESESESESESESESESSESEESSEESESSEESESSEESSEESESSEESESESESESESESESESESSEESEEEESSSSSE") 


 