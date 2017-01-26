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
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

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

def sort_list_by_heuristic_beamwidth(graph, level_node_list, goal,beam_width):
    node_dic = {}
    heuristic = -1
    tmp_list = []
    result = []
    for c_node in level_node_list:
        heuristic = graph.get_heuristic(c_node[-1], goal)
        if node_dic.get(heuristic) == None:
            node_dic[heuristic] = [c_node]
        else:
            node_dic[heuristic].append(c_node)
        node_dic[heuristic].sort()
    tmp_list = node_dic.keys()
    tmp_list.sort(reverse=0)
    for item in tmp_list:
        for i in node_dic[item]:
            result.append(i)
    if len(result) > beam_width:
        result = result[:beam_width]
    return result
## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    agenda = []
    visited_set = set([])
    agenda.append([start])
    level_list=[]
    sorted_list=[]
    loop_check_set_l=[]
    while len(agenda) >0:
        for node in agenda:
            if node[-1]==goal:
                return node
           # if node[-1] not in visited_set:
            for item in graph.get_connected_nodes(node[-1]):
                if len(node) < 2:
                    level_list.append(node + [item])
                elif item != node[-2]:
                    level_list.append(node+[item])
            #visited_set.add(node[-1])
        agenda=[]
        sorted_list=sort_list_by_heuristic_beamwidth(graph, level_list, goal, beam_width)
        level_list=[]
        agenda=agenda+sorted_list
        sorted_list = []
        for item in agenda:
            sorted_list.append(item[-1])
        sorted_list.sort()
        if sorted_list in loop_check_set_l:
            return []
        loop_check_set_l.append(sorted_list)
    return []

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    result=0
    if len(node_names) < 2:
        return result
    while len(node_names) > 1:
        edge=graph.get_edge(node_names[0],node_names[1])
        if edge==None:
            return 0
        result=result+edge.length
        node_names=node_names[1:]
    return result


def sort_list_by_pathlength(graph,agenda):
    node_dic={}
    path_len=0
    tmp_list=[]
    result=[]
    for path in agenda:
        path_len=path_length(graph,path)
        if node_dic.get(path_len)==None:
            node_dic[path_len]=[path]
        else:
            node_dic[path_len].append(path)
    tmp_list = node_dic.keys()
    tmp_list.sort(reverse=0)
    for item in tmp_list:
        for i in node_dic[item]:
            result.append(i)
    return result


def branch_and_bound(graph, start, goal):
    agenda=[]
    current_node=[]
    current_node=[start]
    while current_node!=None:
        if current_node[-1]==goal:
            return current_node
        for node in graph.get_connected_nodes(current_node[-1]):
            if len(current_node)>1 :
                if  (node != current_node[-2]):
                 agenda.append(current_node + [node])
            else:
                agenda.append(current_node+[node])
        agenda=sort_list_by_pathlength(graph,agenda)
        current_node=agenda.pop(0)
    return []

def sort_list_by_pathlength_and_heuristic(graph,agenda,goal):
    node_dic={}
    path_len=0
    tmp_list=[]
    result=[]
    for path in agenda:
        path_len=path_length(graph,path)
        heuristic=graph.get_heuristic(path[-1],goal)
        if node_dic.get(path_len+heuristic)==None:
            node_dic[path_len+heuristic]=[path]
        else:
            node_dic[path_len+heuristic].append(path)
    tmp_list = node_dic.keys()
    tmp_list.sort(reverse=0)
    for item in tmp_list:
        for i in node_dic[item]:
            result.append(i)
    return result

def a_star(graph, start, goal):
    agenda = []
    current_node = []
    visited_set=set([])
    current_node = [start]
    while current_node != None:
        if current_node[-1] == goal:
            return current_node
        if current_node[-1] not in visited_set:
            for node in graph.get_connected_nodes(current_node[-1]):
                if len(current_node) > 1:
                    if (node != current_node[-2]):
                        agenda.append(current_node + [node])
                else:
                    agenda.append(current_node + [node])
            visited_set.add(current_node[-1])
            agenda = sort_list_by_pathlength_and_heuristic(graph, agenda,goal)
        current_node = agenda.pop(0)
    return []


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?
def get_all_nodes(graph,goal):
    result=[]
    agenda=[goal]
    result.append(goal)
    while len(agenda) > 0:
        for node in graph.get_connected_nodes(agenda[0]):
            if node not in result:
                result.append(node)
                agenda.append(node)
        agenda.pop(0)
    return result

def is_admissible(graph, goal):
    for node in get_all_nodes(graph,goal):
        optimal_path_len=a_star(graph, node, goal)
        optimal_path_len=path_length(graph,optimal_path_len)
        heuristic=graph.get_heuristic(node,goal)
        if heuristic > optimal_path_len:
            return False
    return True

def get_all_node_pairs(graph,goal):
    result=[]
    glob_node_list=get_all_nodes(graph,goal)
    for node in glob_node_list:
        part_node_list=glob_node_list[:]
        part_node_list.remove(node)
        for  i_node in part_node_list:
            result.append([node,i_node])
    return result


def is_consistent(graph, goal):
    node_pairs= get_all_node_pairs(graph,goal)
    for node_pair in node_pairs:
        h_x_g=graph.get_heuristic(node_pair[0],goal)
        h_y_g = graph.get_heuristic(node_pair[1], goal)
        d_x_y=a_star(graph,node_pair[0],node_pair[1])
        d_x_y=path_length(graph,d_x_y)
        if abs(h_x_g - h_y_g) > d_x_y:
            return False
    return True
HOW_MANY_HOURS_THIS_PSET_TOOK = '14'
WHAT_I_FOUND_INTERESTING = 'the complexity'
WHAT_I_FOUND_BORING = 'nothing'
