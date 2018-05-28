# N-Puzzle Solver

Program to solve the n-puzzle (8 puzzle) problem using search algorithm techniquest BFS and DFS

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. 

### Prerequisites

What things you need to run the program

```
Python 3.2 or greater
```

## Running the program

Explaination on how to run the program from the command prompt

### Copy files into local repository

Type the following example in the prompt to run the program

```
python driver_3.py BFS 123450678
python driver_3.py ALG initialState
```

### Prompt Syntax

```
driver_3.py (main executable)
ALG (algorithm to be used (BFS, DFS, A*(coming soon))
initialState (initial puzzle state to be used by the program)
```

## Output
```
cost_of_path: [moves on board to solve puzzle]
nodes_expanded: [number of nodes expanded from frontier]
search_depth: [depth of search tree where solution was found]
max_search_depth: [maximium depth explored by the search algorithm]
running_time: [time taken for program to execute]
max_ram_usage:[amount of memory used to run program(coming soon)]
```
## File content
```
driver_3.py [main executable]
createNode [class to create node object and attributes]
search_3.py [file containing search algorithm functions]
expandNode_3.py [file containing script to expand node and add children nodes]
stats_3.py [collects search metrics and formulates an output]
output.txt [file containing search metrics]
```