import numpy as np
import copy

def createGraph(m, n):
    
    graph_matrix = np.arange(n * m).reshape(n, m)

    # construct graph has-map
    graph = {}

    right_max = len(graph_matrix[0]) - 1 
    down_max = len(graph_matrix) - 1

    
    right, left = None, None
    
    for i in range(n):
        vertices = [] # connected vertices
        for j in range(m):
            right = j + 1
            down = i + 1
                
            if (right <= right_max):
                vertices.append(graph_matrix[i][right])
            
            if (down <= down_max):
                vertices.append(graph_matrix[down][j])
            if len(vertices):
                x = copy.copy(vertices)
                graph[graph_matrix[i][j]] = x
                vertices.clear()
    
    start = graph_matrix[0][0] # first element of matrix
    end = graph_matrix[n-1][m-1] # last element of matrix
    
    visited = [False] * (m*n)

    return dfs(graph, start, end, visited)



def find_all_paths(graph, start, end, path=[]):
    path = path + [start] # All paths start from same point 'A'
    
    # base case 1
    if start == end: # i.e graph have only one node(start)
        return [path]
    
    # base case 2
    if start not in graph: # i.e start is not connected
    	return []
    
    paths = []
    for node in graph[start]:
        if node not in path: # avoiding A --> A 
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

    

def dfs(graph, start, end, visited, path=[]):
    
    visited[start] = True
    path.append(str(start))

    if start == end:
        return path
       
    path = []
    for i in graph[start]:
        if visited[i] == False:
            newpaths = dfs(graph, i, end, visited, path)
            for paths in newpaths:
                path.append(paths)
    path.pop()
    visited[start] = True
    return path



if __name__ == '__main__':
	
    print(createGraph(7,3))
    # print(createGraph(23,12))
    






