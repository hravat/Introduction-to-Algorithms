'''
Pseudo code for direction vectors 

dr = [-1,1,0,0]
dc = [0,0,1,-1]

for (i=0,i<4,i++):
    rr=r+dr[i]
    cc=c+dc[i]

    if rr < 0 or cc < 0: continue
    if rr >= R or cc >= C: continue
     
        

'''
import numpy as np

rows=5
columns=7
number_of_nodes=rows*columns
    

def create_dungeon():
    '''
    This method creates the dungeon
    It returns a numpy array
    
    The below are the representations of the cell 
    
    0-EMPTY CELL
    1-START
    2-END
    3-ROCK
    
    Arguments : - 
    rows :- Number of rows 
    columns :- Number of columns 
    start node 
    end node 
    number of rocks 
    '''
    
    
    dungeon_arr = np.zeros([rows,columns])
    
    dungeon_arr[0,0]=1
    dungeon_arr[4,3]=2
    dungeon_arr[4,0]=3
    dungeon_arr[1,1]=3
    dungeon_arr[2,1]=3
    dungeon_arr[3,2]=3
    dungeon_arr[4,2]=3
    dungeon_arr[0,3]=3
    dungeon_arr[3,3]=3
    dungeon_arr[1,5]=3
    dungeon_arr[4,5]=3
    dungeon_arr[4,5]=3
    
    return dungeon_arr
    
    
dungeon_arr=create_dungeon()    
    
def get_adjacent_cells(curr_row,curr_col,dungeon_arr):
    
    '''
    This function is used to get the 
    adjacent cells assuming we can cannot move diagonally
    Arguments :- 
    Current Row 
    Current Column 
    Dungeon Array 
    '''
    
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    adjacent_cells=[]

    for i in range(4):
        
        rr=curr_row+dr[i]
        cc=curr_col+dc[i]

        if cc < 0 or rr < 0 or rr >= rows or cc >= columns or dungeon_arr[rr,cc]==3:
            continue
        else:  
            adjacent_cells.append((rr,cc))
            
    return adjacent_cells        

def graph_to_adjacency_list(rows,columns,dungeon_arr):
    '''
    This function will convert the graph to an adjacency list 
    '''
    
    graph_dict={}
    graph_rev_dict={}
    cnt=0
    adjacency_list={}
    
    for curr_row in range(rows):
        for curr_col in range(columns):
            graph_dict[(curr_row,curr_col)]=cnt
            graph_rev_dict[cnt]=(curr_row,curr_col)
            cnt += 1
            
            
    for curr_row in range(rows):
        for curr_col in range(columns):      
            
            adj_neb_idx =[]
            adjacent_cells=get_adjacent_cells(curr_row,curr_col,dungeon_arr)
            
            for cell in adjacent_cells:
                adj_neb_idx.append(graph_dict[cell])
            adjacency_list[graph_dict[curr_row,curr_col]]=adj_neb_idx
    
    result=np.where(dungeon_arr == 1)
    start_node=list(zip(result[0], result[1]))
    start_node=graph_dict[start_node[0]]
    
    result=np.where(dungeon_arr == 2)
    end_node=list(zip(result[0], result[1])) 
    end_node=graph_dict[end_node[0]]       
            
    return adjacency_list,start_node,end_node,graph_rev_dict      
            
    
adjacency_list,start_node,end_node,graph_rev_dict=graph_to_adjacency_list(rows,columns,dungeon_arr)



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

def bredth_first_search(start_node,end_node):
    prev = solve(start_node)
    path=reconstrucpath(start_node,end_node,prev)
    return path




path =  bredth_first_search(start_node,end_node)
for index in path:
    print(graph_rev_dict[index])  





