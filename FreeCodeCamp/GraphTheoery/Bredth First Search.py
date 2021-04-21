'''
Psuedo Code 1
n= number of nodes in the graph
g= adjacency list representing unweihgted graph

s=start_node
e=end_node
0<=e
s<n

function bfs(s)

    # Do a BFS starting at node n 
    prev=solve(s)

    # Return Reconstructed path from s -> e 
    return reconstrucpath(s,e,prev)
'''

'''
Psuedo Code 2 

solve(s)    
    q = queue data structure with enqueu and dequeue
    q.enqueu(s)
    
    visited = [false,false..] #size n
    visited[s]=True
    
    prev = [false,false..] #size n
    while !q.isempty():
        node=q.dequeu()
        neighbours=g.getnode(node)
        
        for(next:neighbours):
            if !visited[next]:
                q.enqueu(next)
                visited[next]=True
                prev[next]=node
                
    return prev
'''

'''
Psuedo Code 3 
reconstruct path(s,e,prev)
    path=[]
    for(at=e,at!=null,at=prev[at]):
        path.add(at)
    path.reverse
    
    return path    
'''



number_of_nodes=13
adjacency_list={}
adjacency_list[0] = [7,9,11]
adjacency_list[1] = [8,10]
adjacency_list[2] = [3,12]
adjacency_list[3]=[2,4]
adjacency_list[4] = [3]
adjacency_list[5]=[6]
adjacency_list[6]=[5,7]
adjacency_list[7] = [0,3,6,11]
adjacency_list[8] = [1,9,12]
adjacency_list[9] = [0,8,10]
adjacency_list[10] = [1,9]
adjacency_list[11] = [0,7]
adjacency_list[12] = [2,8]

def solve(start_node):
    
    global number_of_nodes
    global adjacency_list
    
    graph_queue=[]
    graph_queue.append(start_node)
    
    visited=[False for i in range(number_of_nodes+1)]
    prev=[False for i in range(number_of_nodes+1)]
    
    visited[start_node]=True
    
    while len(graph_queue)!= 0:
        curr_node=graph_queue.pop()
        neighbours= adjacency_list[curr_node]
        
        for next_node in neighbours:
            if not visited[next_node]:
                graph_queue.append(next_node)
                visited[next_node]=True
                prev[next_node]=curr_node
                
    return prev            
                

def reconstrucpath(start_node,end_node,prev):
    path=[]
    node_at=end_node

    while type(node_at) != bool:
        path.append(node_at)
        node_at=prev[node_at]
        
        
    return [node for node in reversed(path)]


start_node=0
end_node=12

def bredth_first_search(start_node,end_node):
    prev = solve(start_node)
    path=reconstrucpath(start_node,end_node,prev)
    return path

path =  bredth_first_search(0,12)
print(path)   













