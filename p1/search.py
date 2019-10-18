import sys
from collections import deque
import queue as Q


# BREATH FIRST SEARCH

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return [start]
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return []

"""
def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in set(graph[start]) - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])
"""

# DEPTH FIRST SEARCH

def dfs_search(graph, start, end, path=[], visited=[]):
    if start in visited:
        return path
    path += [start]
    visited += [start]
    if start == end:
        return path
    for edge in graph[start]:
        if edge not in visited:
            return dfs_search(graph,edge,end,path,visited)

# UNIFORM COST SEARCH

def ucs_search(graph, start, end):
    if start not in graph:
        raise TypeError(str(start) + ' not found in graph !')
        return
    if end not in graph:
        raise TypeError(str(end) + ' not found in graph !')
        return
    
    queue = Q.PriorityQueue()
    queue.put((0, [start]))
    
    while not queue.empty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        
        if end in node[1]:
            #print("Path found: " + str(node[1]) + ", Cost = " + str(node[0]))
            return node[1]
            break
        
        cost = node[0]
        for neighbor in graph[current]:
            temp = node[1][:]
            temp.append(neighbor)
            queue.put((cost + graph[current][neighbor], temp))

argv= sys.argv
f = open(argv[1], "r")

graphDict={}
graphDictWithCost={}
lineNumber=0

for line in f:
    lineNumber=lineNumber+1
    if(line[-1]=="\n"):
        line=line[:-1]
    lineSplit=line.split(":", 1)
    key=lineSplit[0]
    values=lineSplit[1][1:-1].split(", ")
    valueDict={}
    for value in values:
        value=value.split(":")
        valueDict[value[0]]=int(value[1])
    noCostGraph=[i for i in valueDict if valueDict[i]!=0]
    graphDict[key]=noCostGraph
    """ Intersection for graph with cost """
    keys = set(noCostGraph).intersection(set(valueDict.keys()))
    result = {k:valueDict[k] for k in keys}
    graphDictWithCost[key]=result


start=input("Please enter the start state : ")
end=input("Please enter the goal state : ")

bfs=bfs_shortest_path(graphDict, start, end)

dfs=dfs_search(graphDict,start,end)

ucs=ucs_search(graphDictWithCost, start, end)


print("BFS :",(" - ").join(bfs))
print("DFS :",(" - ").join(dfs))
print("UCS :",(" - ").join(ucs))
