def ucs(start,goal,graph,cost):
    #queue to store node with its cost
    queue=[(0,start)]
    # visited to keep minimum cost so far to any node
    visited={start:0}
    #to keep track of parent of every node
    parent = {start: None}

    while queue:
        min_index=0
        for i in range(1,len(queue)):
            if queue[i][0] < queue[min_index][0]:
                min_index=i


        #saving cost and node of node with min cost
        current_cost,current_node =queue.pop(min_index)
        if current_node==goal:
            #recosntruct the path
            path =[]
            node=current_node
            while node is not None:
                path.append(node)
                node =parent[node]
            path.reverse()
            return current_cost,path;

        # Explore all neighbors
        for neighbor in graph.get(current_node, []):
            # Calculate new cost to reach this neighbor
            edge_cost = cost.get((current_node, neighbor), float('inf'))
            new_cost = current_cost + edge_cost

            # If we found a new node or a cheaper path to existing node
            if neighbor not in visited or new_cost < visited[neighbor]:
                visited[neighbor] = new_cost
                parent[neighbor] = current_node
                queue.append((new_cost, neighbor))

    # If goal not found
    return float('inf'), []


if __name__ == '__main__':
    print("=== Uniform Cost Search Example ===")
    print("Graph: Nodes 0-6 with various connections")
    print()

    # Define the graph structure
    graph = {
        0: [1, 3],    # Node 0 connects to 1 and 3
        1: [6],        # Node 1 connects to 6
        2: [1],        # Node 2 connects to 1
        3: [1, 6, 4], # Node 3 connects to 1, 6, and 4
        4: [2, 5],     # Node 4 connects to 2 and 5
        5: [2, 6],     # Node 5 connects to 2 and 6
        6: [4]         # Node 6 connects to 4
    }

    # Define the cost of each edge
    cost = {
        (0, 1): 2,  # Cost from 0 to 1 is 2
        (0, 3): 5,  # Cost from 0 to 3 is 5
        (1, 6): 1,  # Cost from 1 to 6 is 1
        (3, 1): 5,  # Cost from 3 to 1 is 5
        (3, 6): 6,  # Cost from 3 to 6 is 6
        (3, 4): 2,  # Cost from 3 to 4 is 2
        (2, 1): 4,  # Cost from 2 to 1 is 4
        (4, 2): 4,  # Cost from 4 to 2 is 4
        (4, 5): 3,  # Cost from 4 to 5 is 3
        (5, 2): 6,  # Cost from 5 to 2 is 6
        (5, 6): 3,  # Cost from 5 to 6 is 3
        (6, 4): 7   # Cost from 6 to 4 is 7
    }

    # Find the shortest path from node 0 to node 6
    min_cost, path = ucs(0, 6, graph, cost)

    print(f"Starting node: {0}")
    print(f"Goal node: {6}")
    print(f"Minimum cost: {min_cost}")
    print(f"Path: {' -> '.join(map(str, path))}")
