#this is recursive dfs

def dfs_recursive(graph,node,visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(f"Visiting {node}")
        visited.add(node)
        for neighbour in graph[node]:
            dfs_recursive(graph,neighbour,visited)


def dfs_iterative(graph,start):
    visited = set()
    stack = [start]   # stack starts with first node

    while stack:
        node = stack.pop()   # take from top of stack
        if node not in visited:
            print(f"Visiting {node}")
            visited.add(node)
            # add neighbors to stack (reversed so left-to-right order)
            stack.extend(reversed(graph[node]))


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

#dfs_recursive(graph,'A')
dfs_iterative(graph,'A')



