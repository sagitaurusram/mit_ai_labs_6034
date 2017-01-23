# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = False

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = False

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

def bfs(graph, start, goal):
    agenda=[]
    current_node=[]
    visited_set=set([])
    if(start==goal):
        result=[start]
        return result
    current_node=[start]
    visited_set.add(start)
    for node in graph.get_connected_nodes(start):
        agenda.append(current_node + [node])
    current_node=agenda.pop(0)
    while current_node[-1] != None:
        if current_node[-1]==goal:
            return current_node
        else :
            if current_node[-1] not in visited_set:
                visited_set.add(current_node[-1])
                for node in graph.get_connected_nodes(current_node[-1]):
                    if(node != current_node[-2]):
                        agenda.append(current_node + [node])
        current_node=agenda.pop(0)



## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    agenda = []
    current_node = []
    visited_set = set([])
    if (start == goal):
        result = [start]
        return result
    current_node = [start]
    visited_set.add(start)
    for node in graph.get_connected_nodes(start):
        agenda.insert(0,current_node + [node])
    current_node = agenda.pop(0)
    while current_node[-1] != None:
        if current_node[-1] == goal:
            return current_node
        else:
            if current_node[-1] not in visited_set:
                visited_set.add(current_node[-1])
                for node in graph.get_connected_nodes(current_node[-1]):
                    if (node != current_node[-2]):
                        agenda.insert(0,current_node + [node])
        current_node = agenda.pop(0)

def sort_list_by_heuristic(graph,node,goal):
    node_dic={}
    heuristic=-1
    tmp_list=[]
    result=[]
    node_list=graph.get_connected_nodes(node)
    for c_node in node_list:
        heuristic=graph.get_heuristic(c_node,goal)
        if node_dic.get(heuristic) == None:
            node_dic[heuristic]=[c_node]
        else:
            node_dic[heuristic].append(c_node)
        node_dic[heuristic].sort()
    tmp_list=node_dic.keys()
    tmp_list.sort(reverse=1)
    for item in tmp_list:
        for i in node_dic[item]:
            result.append(i)
    return result



## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    agenda = []
    current_node = []
    visited_set = set([])
    if (start == goal):
        result = [start]
        return result
    current_node = [start]
    visited_set.add(start)
    for node in sort_list_by_heuristic(graph,current_node[-1],goal):
        agenda.insert(0, current_node + [node])
    current_node = agenda.pop(0)
    while current_node[-1] != None:
        if current_node[-1] == goal:
            return current_node
        else:
            if current_node[-1] not in visited_set:
                visited_set.add(current_node[-1])
                for node in sort_list_by_heuristic(graph,current_node[-1],goal):
                    if (node != current_node[-2]):
                        agenda.insert(0, current_node + [node])
        current_node = agenda.pop(0)

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    raise NotImplementedError

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    raise NotImplementedError


def branch_and_bound(graph, start, goal):
    raise NotImplementedError

def a_star(graph, start, goal):
    raise NotImplementedError


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''
