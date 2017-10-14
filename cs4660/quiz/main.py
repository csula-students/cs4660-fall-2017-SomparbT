"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!

Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9

TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import json
import codecs

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

from graph import graph as GRAPH
from graph import utils

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
from graph import graph as _graph

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.

    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response

class Room(object):
    """Node represents basic unit of graph"""
    def __init__(self, id, name, effect):
        self.id = id
        self.name = name
        self.effect = effect

    def __str__(self):
        return '{}({}):{}'.format(self.name, self.id, self.effect)
    def __repr__(self):
        return '{}({}):{}'.format(self.name, self.id, self.effect)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

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

        for child in findNeighbors(current):
            if child not in came_from:
                frontier.put(child)
                came_from[child] = current
                
                if child == dest_node:
                    break #early exit
        else:
            continue
        break

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

        for child in findNeighbors(current):
            new_cost = cost_so_far[current] + findDistance(current, child)
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                priority = new_cost
                key += 1
                frontier.put((priority, key, child))
                came_from[child] = current
                
    return construct_path(graph, initial_node, dest_node, came_from)

def findNeighbors(current_node):
    """
    
    """
    json_neighbors = get_state(current_node.data.id)['neighbors']
    neighbors = []
    for json_neighbor in json_neighbors:
        neighbors.append(GRAPH.Node(parse_room(get_state(json_neighbor['id']))))

    return neighbors

def findDistance(current_node, next_node):
    """
    
    """
    return float(transition_state(current_node.data.id, next_node.data.id)['event']['effect'])


def construct_path(graph, initial_node, dest_node, came_from):
    path = []
    current = dest_node
    while current != initial_node:
        parent = came_from[current]
        path.append(_graph.Edge(parent, current, findDistance(parent, current)))
        current = parent
    path.reverse()
    return path

def parse_room(json_room):
    return Room(json_room['id'], json_room['location']['name'], 0) 

if __name__ == "__main__":
    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    #print(empty_room)
    #print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))

    dark_room = get_state('f1f131f647621a4be7c71292e79613f9')

    g1 = GRAPH.AdjacencyList()

    result = bfs(g1, GRAPH.Node(parse_room(empty_room)), GRAPH.Node(parse_room(dark_room)))   
    for edge in result:
        print(edge)

    g2 = GRAPH.AdjacencyList()
    result = dijkstra_search(g2, GRAPH.Node(parse_room(empty_room)), GRAPH.Node(parse_room(dark_room)))   
    for edge in result:
       print(edge)