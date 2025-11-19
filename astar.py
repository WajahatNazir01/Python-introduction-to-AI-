import heapq
def astar(graph, start, goal, heuristic):
    pq=[(heuristic[start],0,start,[start])]
    visited={}
    while pq :
        f, g, node, path = heapq.heappop(pq)
        if node in visited and visited[node] <= g:
            continue
        visited[node]=g

        if node==goal:
            return g, path
        
        #exploring all other neighboring nodes
        for neighbor, edge_cost in graph[node]:
            new_g=g+edge_cost
            new_f = new_g + heuristic[neighbor]
            new_path = path+[neighbor]
            heapq.heappush(pq, (new_f, new_g, neighbor, new_path))

    return None



graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7), ('E', 3)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values (straight-line estimates to goal 'F')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}


result= astar(graph,'A','D',heuristic)
print("minimum cost is :"+ str(result))


#-------------------------------------------------------------------------------------------------------

