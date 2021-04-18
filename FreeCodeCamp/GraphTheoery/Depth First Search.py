#Reference Videos 

#https://www.youtube.com/watch?v=09_LlHjoEiY&t=1692s
#https://www.youtube.com/watch?v=QVcsSaGeSH0
     
"""
Psuedo Code 


 # Global or Class Scope varaibles 
 
 n = number of nodes in a graph
 g = Adjacency List representing number of nodes in a graph 
 visisted = [false,....false] n times 
 
 function dfs(at):
     if visited[at] : return
     visited[at]=True
     
     neighbours=graph[at]
     for next in neighbours:
         dfs(next)
         
 #Start dfs at node 0 
 start_node=0
 dfs(start_node)
  
"""

number_of_nodes=11
adjacency_list = {}
visited=[False for i in range(number_of_nodes+1)]

adjacency_list[0] = [1,9]
adjacency_list[1] = [8]
adjacency_list[2] = []
adjacency_list[3]=[2,4,5]
adjacency_list[4] = []
adjacency_list[5]=[6]
adjacency_list[6]=[7]
adjacency_list[7] = [10,3]
adjacency_list[8] = [7]
adjacency_list[9] = [8]
adjacency_list[10] = [11]
adjacency_list[11] = [7]


def dfs(number_of_nodes,adjacency_list,at,visited,path):
    
    v_number_of_nodes=number_of_nodes
    v_adjacency_list=adjacency_list
    v_at=at
    v_visited=visited
    v_path=path
    
    if v_visited[v_at]:
        return
    else:
        v_visited[at]=True    
        
    neighbours = v_adjacency_list[at]
    
    v_path=v_path+' '+str(v_at)
    
    print('=============================at=============================')
    print(v_at)
    print('=============================path=============================')
    print(v_path)
    
    for next_node in neighbours:
        dfs(v_number_of_nodes,v_adjacency_list,next_node,v_visited,v_path)
    
visited=[False for i in range(number_of_nodes+1)]
dfs(number_of_nodes,adjacency_list,0,visited,path='')    




