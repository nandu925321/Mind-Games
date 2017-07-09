# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    values = [[0 for j in range(W+1)] for i  in range(n+1)]
    #print(values)
    for i in range(n+1):
    	for j in range(W+1):
    		if i==0 or j==0:
    			values[i][j] = 0
    		elif w[i-1] <= j:
    			values[i][j] = max(w[i-1] + values[i-1][j-w[i-1]], values[i-1][j])
    		else:
    			values[i][j] = values[i-1][j]

    #print(values)
    return values[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    #print(W)
    #print(w)
    print(optimal_weight(W, w))
