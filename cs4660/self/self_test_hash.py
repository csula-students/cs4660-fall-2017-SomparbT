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

tile1 = utils.Tile(12, 2, "")
tile2 = utils.Tile(1, 22, "")
tile3 = utils.Tile(1, 1, "")
tiles = {}
tiles[tile1] = True
print(tile1 in tiles) 
print(tile2 in tiles) 
print(tile3 in tiles) 