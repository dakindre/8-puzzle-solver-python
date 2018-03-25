import sys
import timeit
import queue
from collections import deque
from queue import PriorityQueue

import stats_3 as stats
import createNode_3 as create
import expandNode_3 as expand

'''
BFS search algorithm using a dequque
'''
def bfs(initialState, goalState):
    start = timeit.default_timer()
    
    frontier = deque([initialState])
    explored = set() 
    
    while frontier:
        ''' Remove from frontier and add to explored '''
        current = frontier.popleft()
        explored.add(current.getHex())

        ''' If goal state reached '''
        if current.state == goalState.state:
            stop = timeit.default_timer()
            Moves =[]
            while current.parent != None:
                Moves.insert(0, current.move)
                current = current.parent
                
            ''' Create bfs statistic output file '''
            stats.finalResult(len(Moves), Moves,len(explored)-1, stop-start, stats.getMaxDepth(frontier))
            break
        
        ''' Expand node and add to the frontier queue '''
        expand.expandNode(current, False)
        fringe = current.getChildren()
        for x in fringe:
            if x.ident not in explored:
                frontier.append(x)


'''
DFS search algorithm using a dequque with reverse ordering input
'''
def dfs(initialState, goalState):
    start = timeit.default_timer()
    
    frontier = deque([initialState])
    exploredFull = set()
    
    ''' Keep list of hex values for quick check because can't figure out how to
        iterate a list of objects attributes '''
    explored = set()
    frontierList = set()
    
    while frontier:
        current = frontier.pop()
        exploredFull.add(current)
        
        explored.add(current.getHex())
        
        
        if current.state == goalState.state:
            stop = timeit.default_timer()
            Moves =[]
            while current.parent != None:
                Moves.insert(0, current.move)
                current = current.parent
                
            ''' Create dfs statistic output file '''
            stats.finalResult(len(Moves), Moves,len(explored)-1, stop-start, stats.getMaxDepth(frontier))
            break

        expand.expandNode(current, False)
        fringe = current.getChildren()

        ''' Add in reverse order to get desired LIFO'''
        for x in reversed(fringe):
            if frontier:
                if x.ident not in explored and x.ident not in frontierList:
                    frontier.append(x)
                    frontierList.add(x.getHex())
            else:
                frontier.append(x)
                frontierList.add(x.getHex())
