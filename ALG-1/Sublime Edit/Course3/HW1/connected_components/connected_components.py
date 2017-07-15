#Uses python3

import sys

def explore (adj,visited,i):
    if(visited[i]==1):
        return 1
    visited[i] = 1
    for x in range(len(adj[i])):
        if not (visited [adj[i][x]]):
            if(explore(adj, visited,adj[i][x])):
                return 1
    return 0


def number_of_components(adj):
    result = 0
    #write your code here
    # connected component number
    # vertex with connected component array
    # send this info to explore
    con_num = 0
    visited = [0] * len(adj)
    V_c = len(adj)
    for i in range(V_c):
        if not visited[i]:
            explore(adj,visited,i)
            con_num = con_num + 1
    
    #component_number = [0] * len(adj)
    #explore(adj,visited,con_num)
    return con_num


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
