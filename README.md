# 8-puzzle-solver-python
Purpose: A solver for the n-puzzle problem using search techniques BFS and DFS. A* optimality currently being added

Process: 
  1. Run program using CP
    a. provide search technique (BFS, DFS) 
    b. provide initial state string (eg. 123405678)
    c. ex python driver_3.py BFS 123405678
    
  2. Program outputs the solution as: 
    path_to_goal: ['Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Up', ...]
    cost_of_path: 46142 (moves neededf to find goal state)
    nodes_expanded: 51015 (number of nodes explored from frontier to find goal state)
    search_depth: 46142 (search tree depth "d")
    max_search_depth: 46142 (maximum depth explored in search tree)
    running_time: 1.2199117784132805 (program run time)
    max_ram_usage: (needs to be added)
    
  Files:
    1. driver_3.py (main file)
    2. search_3.py (file containing search algorithms)
    3. createNode_3.py (file to create new class instance of node)
    4. expandNode_3.py (file with function to expand existing node/add children))
    5. stats.py (creates the output template and collects necessary metrics)
    6. output.txt (contains program statistics)

