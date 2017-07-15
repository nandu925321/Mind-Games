#Uses python3
import sys
def reach(adj, x, y):
    #write your code here
    #create a visited array to keep track of visits
    #give a connected component number 
    con_num = 1
    visited = [0] * len(adj)
    return explore(adj, x, y, visited,con_num)
	
def explore(adj, x, y, visited):
    if (x == y):
        return 1
    visited[x] = 1
    for i in range(len(adj[x])):
        if (not visited[adj[x][i]]):
            if(explore(adj, adj[x][i], y, visited)):
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # seperate data into n and m and remove from the list
    n,m = data[0:2]
    del data[0:2]
    # seperate the search path and remove from list
    u,v = data[-2:]
    del data[-2:]
    # seperate edges
    V = data[0:len(data):2]
    W = data[1:len(data)+1:2]
    # create edges array
    edges = []
    for i in range(0,m):
    	edge = (V[i],W[i])
    	edges.append(edge)
    # create an adjagency array # _ is just a throwaway variable not used anywhere in the loop
    adj = [[] for _ in range(n)]
    
    # fill the adjagency array # array starts from zero , add both directions [undirected graph]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # array starts from 0
    
    # perform direct link checks and validate
    if (u,v) in edges:
    	print(1)
    elif not adj[u-1]:
    	print (0)
    else:
    	u,v = u-1,v-1
    	#print(adj)
    	print(reach(adj,u,v))
    
    



    







