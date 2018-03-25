'''
 Gets Search Algorithm effectiveness statistics
'''

def getMaxDepth(explored):
    if not explored: return 0
    else: return max(node.depth for node in explored)

    
def finalResult(size, Moves, expanded, time, maxDepth):
    sl = '['+', '.join(Moves)+']'
    f = open('output.txt','w')
    f.write('path_to_goal: ' + sl + '\n')
    f.write('cost_of_path: ' + str(size) + '\n')
    f.write('nodes_expanded: '+ str(expanded) + '\n')
    f.write('search_depth: ' + str(size) + '\n')
    f.write('max_search_depth: ' + str(maxDepth) + '\n')
    f.write('running_time: ' + str(time) + '\n')
    f.write('max_ram_usage: ')
    f.close()
