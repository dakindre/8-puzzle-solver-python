import sys
import argparse
import search_3 as search
import createNode_3 as create

        
def main():

    #Parse Input
    parser = argparse.ArgumentParser()
    parser.add_argument('m', type=str)
    parser.add_argument('s', type=str)

    args = parser.parse_args()
    method = args.m
    n = [int(x) for x in args.s.split(',')]


    #Create Initial State Board from input
    board = [n[0], n[1], n[2],
             n[3], n[4], n[5],
             n[6], n[7], n[8]]

    #Create Nodes for Initial State and Goal States
    initialState =  create.node(board, None, None, None, 0)
    goalState = create.node([0,1,2,3,4,5,6,7,8], None, None, None, 0)

    
    #Calls selected search algorithm
    if method == 'bfs':
        search.bfs(initialState, goalState)

    elif method == 'dfs':
        search.dfs(initialState, goalState)

    elif method == 'ast':
        #Creates a matrix for goal state for a* comparisons
        goalState.createMatrix()
        
        search.ast(initialState, goalState)

    
if __name__ == "__main__":
	main()
    



    
