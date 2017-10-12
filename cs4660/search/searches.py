"""
Searches module defines all different search algorithms
"""
import math
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
from graph import graph as _graph

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    frontier = Q.Queue()
    frontier.put(initial_node)
    came_from = {}
    came_from[initial_node] = None

    while not frontier.empty():
        current = frontier.get()           

        for child in graph.neighbors(current):
            if child not in came_from:
                frontier.put(child)
                came_from[child] = current
                
                if child == dest_node:
                    break #early exit
        else:
            continue
        break

    return construct_path(graph, initial_node, dest_node, came_from)


def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    frontier = [] #implementing stack
    frontier.append(initial_node)
    came_from = {}
    came_from[initial_node] = None

    while frontier: #stack not empty
        current = frontier[-1] #stack.peek()
          
        not_visit_child = [child for child in graph.neighbors(current) if child not in came_from]
        if not_visit_child:
            child = not_visit_child[0]
            frontier.append(child) #stack.push()
            came_from[child] = current
            
            if child == dest_node: 
                break #early exit

        else:
            frontier.pop() #stack.pop()

    return construct_path(graph, initial_node, dest_node, came_from)

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    frontier = Q.PriorityQueue()
    key = 1 #assign to each element to make them oderable
    frontier.put((0, key, initial_node)) #(priority, key, node)
    came_from = {}
    cost_so_far = {}
    came_from[initial_node] = None
    cost_so_far[initial_node] = 0

    while not frontier.empty():
        current = frontier.get()[2]

        if current == dest_node:
            break

        for child in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.distance(current, child)
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                priority = new_cost
                key += 1
                frontier.put((priority, key, child))
                came_from[child] = current
                
    return construct_path(graph, initial_node, dest_node, came_from)            

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    frontier = Q.PriorityQueue()
    key = 1 #assign to each element to make them oderable
    frontier.put((0, key, initial_node)) #(priority, key, node)
    came_from = {}
    cost_so_far = {}
    came_from[initial_node] = None
    cost_so_far[initial_node] = 0

    while not frontier.empty():
        current = frontier.get()[2]

        if current == dest_node:
            break

        for child in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.distance(current, child)
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                priority = new_cost + heuristic(dest_node, child)
                key += 1
                frontier.put((priority, key, child))
                came_from[child] = current
                
    return construct_path(graph, initial_node, dest_node, came_from)

def construct_path(graph, initial_node, dest_node, came_from):
    path = []
    current = dest_node
    while current != initial_node:
        parent = came_from[current]
        path.append(_graph.Edge(parent, current, graph.distance(parent, current)))
        current = parent
    path.reverse()
    return path    

def heuristic(dest_node, current_node):
   # Euclidean distance on a square grid
   dest_tile = dest_node.data
   current_tile = current_node.data
   #return abs(dest_tile.x - current_tile.x) + abs(dest_tile.y - current_tile.y)
   return math.sqrt((dest_tile.x - current_tile.x)**2 + (dest_tile.y - current_tile.y)**2)