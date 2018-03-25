import sys
import hashlib



class node:
    def __init__(self, state, parent, move, children, depth, matrix=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.children = []
        self.ident = self.setIdent()
        self.depth = depth
        self.matrix = matrix
        

    def addChild(self, child):
        self.children.append(child)

    def getBlank(self):
        return self.state.index(0)

    def getHex(self):
        return self.ident

    def getChildren(self):
        return self.children

    def setIdent(self):
        hashId = hashlib.md5()
        hashId.update(repr(self.state).encode('utf-8'))
        
        return hashId.hexdigest()
    
    def __lt__(self, other):
        return self.ident < other.ident

    def tile_coordinates(self, tile, grid_state):
        for (y, row) in enumerate(grid_state):
            for (x, value) in enumerate(row):
                if value == tile:
                    return (y, x)

    def locate_tile(self, tile, goal):
        for (y, row) in enumerate(goal.matrix):
            for (x, value) in enumerate(row):
                if value == tile:
                    return (y, x)

    
    #Only for A* Algorithm
    def createMatrix(self):
        matrix = [[' ' for x in range(3)] for y in range(3)]

        i = 0
        j = 0
        for x in self.state:
            matrix[i][j] = x
            j += 1
            if j == 3:
                j = 0
                i += 1
        self.matrix = matrix

            
    def manhattan_distance(self, goal):
        distance = 0
        for (y, row) in enumerate(self.matrix):
            for (x, tile) in enumerate(row):
                if tile == 0:
                    continue
                goalCoord = self.locate_tile(tile, goal)
                tileDistance = (abs(goalCoord[0] - y) + abs(goalCoord[1] - x))
        
                distance += tileDistance
        return distance
