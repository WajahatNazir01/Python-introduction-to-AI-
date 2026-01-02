graph = {
   'S':{'I':9,'H':4,'A':8},
    'I':{'C':5,'H':2,'S':9},
    'A':{'H':3,'B':5,'S':8},
    'H':{'A':3,'B':9,'C':1,'I':2,'S':4},
    'B':{'A':5,'H':9,'C':6,'D':6},
    'C':{'B':6,'H':1,'D':2,'F':7,'I':5},
    'D':{'B':6,'C':2,'F':2,'E':5},
    'F':{'C':7,'D':2,'E':1,'G':8},
    'E':{'D':5,'F':1,'G':4},
    'G':{'E':4,'F':8}
}

def heuristic(node):
    heuristics={'S':10,'A':9,'B':7,'C':4,'D':3,'E':2,'F':4,'G':0,'H':6,'I':7}
    return heuristics[node]

def reconstructPath(start,goal,parent):
    path=[]
    node=goal
    while node is not None:
        path.append(node)
        node=parent.get(node)
    path.reverse()
    return path if path[0]==start else None

def astar(start,goal,graph,heuristic):
    queue=[(heuristic(start),0,start)]
    parent={start:None}
    g_score={start:0}

    while queue:
        min_index=0
        for i in range (1,len(queue)):
            if queue[i][0]<queue[min_index][0]:
                min_index=i
        f_score,current_g,current_node = queue.pop(min_index)
        if(current_node==goal):
            return reconstructPath(start,goal,parent),g_score[current_node]
        for neighbor,edge_cost in graph[current_node].items():
            new_g_score=current_g+edge_cost
            if neighbor not in g_score or new_g_score < g_score[neighbor]:
                g_score[neighbor]=new_g_score
                parent[neighbor]=current_node
                new_f_score=new_g_score+heuristic(neighbor)
                queue.append((new_f_score,new_g_score,neighbor))
    return []

def ucs(start,goal,graph):
    queue=[(0,start)]
    visited={start:0}
    parent={start:None}
    clsoed=set()
    while queue:
        min_index=0
        for i in range (1,len(queue)):
            if queue[i][0]<queue[min_index][0]:
                min_index=i
        cost,node=queue.pop(min_index)
        if node in clsoed:
            continue
        clsoed.add(node)
        if node == goal :
            path=[]
            c_node = node
            while c_node is not None:
                path.append(c_node)
                c_node=parent[c_node]
            path.reverse()
            if path[0] == start:
                return cost, path
            else:
                return float('inf'), []
    
        for neighbor,n_cost in graph.get(node,{}).items():
            new_cost=cost+n_cost
            if neighbor not in visited or new_cost< visited[neighbor]:
                visited[neighbor]=new_cost
                parent[neighbor]=node
                queue.append((new_cost,neighbor))
    return float('inf'), []

# def f(x):
#     return (-(x**4)/8)+(x**3/2)+2*(x**2)-4*(x)+5

# def hill_climbq2(start_x,step=0.1,minStep=0.0001):
#     while step > minStep :
#         current = f(start_x)
#         right=start_x+minStep
#         left=start_x-minStep
#         f_right=f(right)
#         f_left=f(left)
#         if(f_right>current):
#             start_x=right
#             step=step*1.1
#         elif(f_left>current):
#             start_x=left
#             step=step*1.1
#         else:
#             step=step*0.8
        
#     return start_x,current
def f(x):
    return (-(x**4)/8)+(x**3/2)+2*(x**2)-4*(x)+5

def hill_climbq2(start_x, step=0.1, minStep=0.0001):
    while step > minStep:
        current = f(start_x)
        right = start_x + step
        left = start_x - step
        f_right = f(right)
        f_left = f(left)

        if f_right > current:
            start_x = right
            step *= 1.1        
        elif f_left > current:
            start_x = left
            step *= 1.1
        else:
            step *= 0.8        

    return start_x, current



def hill_climbsimple(start_x,step=0.1,iter=1000):
    for i in range (iter):
        current = f(start_x)
        right=start_x+step
        left=start_x-step
        f_right=f(right)
        f_left=f(left)
        if(f_right>current):
            start_x=right
        elif(f_left>current):
            start_x=left
        else:
            break
        
    return start_x,current


if __name__=="__main__":
    print("====================================")
    print("Astar implementation of graph")
    start='S'
    goal='G'
    path,costt=astar(start,goal,graph,heuristic)
    print("Shortest path is",path)
    print("Cost to reach there is ",costt)
    print("====================================") 
    print()
    print()
    print("====================================")
    print("Implementing ucs")
    cost,path=ucs(start,goal,graph)
    print("Best shortest path is :",path)
    print("Cost for this path is ",cost)
    print("====================================")   
    print()
    print()
    print("====================================")
    print("Simple hill_climb implementation on give f(x)")
    best_x,max_fx=hill_climbsimple(-2)
    print("Best value of x is ", best_x)
    print("Best value of f(x) is ", max_fx)

    print("Question 2 paper :")
    starting_value=float(input("Give Starting value"))
    best_x2,max_fx2= hill_climbq2(starting_value)
    print("Best value of x is ", best_x2)
    print("Best value of f(x) is ", max_fx2)
    print("====================================")  
    





