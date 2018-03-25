import createNode_3 as create

'''
Class handles creating children nodes for parent node
'''

class expandNode:
    def __init__(self, node, search):
        self.parent = node
        self.position = create.node.getBlank(node)
        self.search = search
        self.children = []

        self.moveup()
        self.movedown()
        self.moveleft()
        self.moveright()

    ''' Functions to handle the movement of the 0 tile '''
    def moveup(self):
        if self.position not in [0,1,2]:
            newState = self.move('U')
            self.parent.addChild(create.node(newState, self.parent, "'Up'", None, self.parent.depth+1))

    def movedown(self):
        if self.position not in [6,7,8]:
            newState = self.move('D')
            self.parent.addChild(create.node(newState, self.parent, "'Down'", None, self.parent.depth+1))

    def moveleft(self):
        if self.position not in [0,3,6]:
            newState = self.move('L')
            self.parent.addChild(create.node(newState, self.parent, "'Left'", None, self.parent.depth+1))

    def moveright(self):
        if self.position not in [2,5,8]:
            newState = self.move('R')
            self.parent.addChild(create.node(newState, self.parent, "'Right'", None, self.parent.depth+1))

    ''' Main movement controller and tile reordering '''
    def move(self, direction):
        state = self.parent.state[:]
        if direction == 'U':
            state[self.position], state[self.position-3] = state[self.position-3], state[self.position]
             
        elif direction == 'D':
            state[self.position], state[self.position+3] = state[self.position+3], state[self.position]
     
        elif direction == 'L':
            state[self.position], state[self.position-1] = state[self.position-1], state[self.position]

        elif direction == 'R':
            state[self.position], state[self.position+1] = state[self.position+1], state[self.position]
            
        return state
