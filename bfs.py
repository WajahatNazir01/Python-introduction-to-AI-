from collections import deque
def bfs(graph,start):
    #make a set of visisted nodes that is empty at first
    visited = set()
    # initialize queue with the starting node
    queue  = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(f"Visiting {node}")
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    print(f" --> Adding {neighbour} to queue")
                    queue.append(neighbour)

#make graph in from of dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
bfs(graph,'A')














