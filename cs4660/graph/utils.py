"""
utils package is for some quick utility methods

such as parsing
"""
from .graph import Node
from .graph import Edge

class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.symbol)



def parse_grid_file(graph, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph

    Returns graph object
    """
    # TODO: read the filepath line by line to construct nodes & edges
    
    file = open(file_path, encoding='utf-8')
    text = file.read()
    lines = text.split('\n')
    grid = []
    for line in lines:
        if line:
            grid.append([line[i:i+2] for i in range(1, len(line[1:-1]), 2)])
    grid = grid[1:-1]        
    
    file.close()
    """
    example of grid
    grid = [
       [[##], [@1], [##]],
       [[##], [##], [##]],
       [[##], [##], [@3]]
    ]
    """
    # TODO: for each node/edge above, add it to graph
    tiles = {}

    for y in range(len(grid)):
        for x in range (len(grid[0])):
            tile = Tile(x, y, grid[y][x])
            graph.add_node(Node(tile))
            tiles[(x, y)] = tile

    for y in range(len(grid)):
        for x in range (len(grid[0])):
            current_tile = Tile(x, y, grid[y][x])

            if current_tile.symbol == "##":
                continue #obstacle tile not suppose to have edge

            #check that adjacent tiles are valid, order is N -> E -> W -> S
            
            if (x, y - 1) in tiles:
                upper_tile = tiles[(x, y - 1)]
                if upper_tile.symbol != "##":
                    graph.add_edge(Edge(Node(current_tile), Node(upper_tile), 1))   

            if (x + 1, y) in tiles:
                right_tile = tiles[(x + 1, y)]
                if right_tile.symbol != "##":
                    graph.add_edge(Edge(Node(current_tile), Node(right_tile), 1))

            if (x - 1, y) in tiles:
                left_tile = tiles[(x - 1, y)]
                if left_tile.symbol != "##":
                    graph.add_edge(Edge(Node(current_tile), Node(left_tile), 1))

            if (x, y + 1) in tiles:
                lower_tile = tiles[(x, y + 1)]
                if lower_tile.symbol != "##":
                    graph.add_edge(Edge(Node(current_tile), Node(lower_tile), 1))


    return graph

def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile

    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    e.g. Edge(Node(Tile(1, 2)), Node(Tile(2, 2)), 1) => "S"
    """
    #print(edges)
    path = ""
    for edge in edges:
        tile1 = edge.from_node.data
        tile2 = edge.to_node.data
        if (tile2.x - tile1.x) > 0 :
            path += "E"
        elif (tile2.x - tile1.x) < 0 :
            path += "W"
        elif (tile2.y - tile1.y) > 0 :
            path += "S"
        else:
            path += "N"    
    return path
