'''
Psuedo Code

 # Global or Class Scope varaibles 
 
 n = number of nodes in a graph
 g = Adjacency List representing number of nodes in a graph
 visited = [false,....false] n times 
 count=0
 components=[] int list size n 
 
 function find_components
     for i in 1 to n:
         if !visited[i]:
             count++
             dfs(i)
 return comonents,count
 
 
 function dfs(at):
     visited[at] = True
     components[at]=count
     
     neighbours=graph[at]
     for next in neighbours:
         if !visited[next]:
             dfs(next)
'''

number_of_nodes=17
adjacency_list = {}
visited=[False for i in range(number_of_nodes+1)]
components={}
count=0

adjacency_list[0] = [4,8,14,13]
adjacency_list[1] = [5]
adjacency_list[2] = [15,9]
adjacency_list[3]=[9]
adjacency_list[4] = [8,0]
adjacency_list[5]=[17,16,1]
adjacency_list[6]=[7,11]
adjacency_list[7] = [6,11]
adjacency_list[8] = [0,4,14]
adjacency_list[9] = [2,3,15]
adjacency_list[10] = [15]
adjacency_list[11] = [6,7]
adjacency_list[12] = []
adjacency_list[13] = [0,14]
adjacency_list[14] = [0,8,13]
adjacency_list[15] = [2,9,10]
adjacency_list[16] = [5]
adjacency_list[17] = [5]



def find_components(number_of_nodes,
                    adjacency_list,
                    visited,
                    components,
                    count):
    
    for i in range(number_of_nodes+1):
        if visited[i]==False:
            count += 1 
            dfs(i,adjacency_list,visited,components,count)


def dfs(at,adjacency_list,visited,components,count):
    
    visited[at]=True
    components[at]=count
    
    neighbours = adjacency_list[at]
    
    for next in neighbours:
        if not visited[next]:
            dfs(next,adjacency_list,visited,components,count)


find_components(number_of_nodes,
                    adjacency_list,
                    visited,
                    components,
                    count)

print(components)                                            

