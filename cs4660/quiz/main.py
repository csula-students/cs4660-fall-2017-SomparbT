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
import time

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

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

def bfs(initial_room, dest_room):
    """
    Breadth First Search
    uses graph to do search from the initial_room to dest_room
    returns a list of transitions going from the initial_room to dest_room
    """
    frontier = Q.Queue()
    frontier.put(initial_room)
    came_from = {}
    came_from[initial_room] = None

    while not frontier.empty():
        current = frontier.get()           

        for child in findNeighbors(current):
            if child not in came_from:
                frontier.put(child)
                came_from[child] = current
                
                if child == dest_room:
                    break #early exit
        else:
            continue
        break

    return construct_path(initial_room, dest_room, came_from)

def dijkstra_search(initial_room, dest_room):
    """
    Dijkstra Search
    uses graph to do search from the initial_room to dest_room
    returns a list of transitions going from the initial_room to dest_room
    """
    frontier = Q.PriorityQueue()
    key = 1 #assign to each element to make them oderable
    frontier.put((0, key, initial_room)) #(priority, key, node)
    came_from = {}
    cost_so_far = {}
    came_from[initial_room] = None
    cost_so_far[initial_room] = 0
    visited_node = set()

    while not frontier.empty():
        current = frontier.get()[2]

        if current == dest_room:
            break

        if current in visited_node:
            continue

        visited_node.add(current)

        for child in filter(lambda child: child not in visited_node, findNeighbors(current)):
            new_cost = cost_so_far[current] - findDistance(current, child)
            if child not in cost_so_far or new_cost < cost_so_far[child]:
                cost_so_far[child] = new_cost
                priority = new_cost
                key += 1
                frontier.put((priority, key, child))
                came_from[child] = current

    return construct_path(initial_room, dest_room, came_from)

def findNeighbors(current_room):
    """
    private helper method parsing JSON string of current room
    returns a list of neightbors id
    """
    json_neighbors = get_state_local(current_room)['neighbors']

    return list(map((lambda json_neighbor: json_neighbor['id']), json_neighbors))
    #return neighbors

def findDistance(current_room, next_room):
    """
    private helper method parsing JSON string of transition
    returns effect which defines cost of moving from current_room to next_room
    """
    return float(transition_state_local(current_room, next_room)['event']['effect'])


def construct_path(initial_room, dest_room, came_from):
    """
    private helper method for constructing moving path from initial_room to dest_room
    returns a list of transitions from initial_room to dest_room
    """
    path = []
    current = dest_room
    hp = 0
    while current != initial_room:
        parent = came_from[current]
        effect = transition_state_local(parent, current)['event']['effect']
        hp += effect
        path.append('{}({}):{}({}):{}'.format(get_state_local(parent)['location']['name'], parent, get_state_local(current)['location']['name'], current, effect))
        current = parent
    path.reverse()
    path.append('Total hp: {}'.format(hp))
    return path

def get_state_local(room_id):
    """
    private helper method for storing state's JSON from server at local
    """
    global local_state
    try:
        return local_state[room_id]
    except KeyError:
        local_state[room_id] = get_state(room_id)
        return local_state[room_id]

def transition_state_local(room_id, next_room_id):
    """
    private helper method for storing transition's JSON from server at local
    """
    global local_transition
    try:
        return local_transition[(room_id, next_room_id)]
    except KeyError:
        local_transition[(room_id, next_room_id)] = transition_state(room_id, next_room_id)
        return local_transition[(room_id, next_room_id)]     

if __name__ == "__main__":
    # Your code starts here
    local_state = {}
    local_transition = {}
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    #print(empty_room)
    #print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))

    dark_room = get_state('f1f131f647621a4be7c71292e79613f9')

    print('BFS Path:')
    start_time = time.time()
    result = bfs(empty_room['id'], dark_room['id'])
    for edge in result:
        print(edge)

    print("bfs: %.2f seconds" % (time.time() - start_time))
    print()
    print('Dijkstra Path:')

    start_time = time.time()
    result = dijkstra_search(empty_room['id'], dark_room['id']) 
    for edge in result:
       print(edge)

    print("dijkstra: %.2f seconds" % (time.time() - start_time))