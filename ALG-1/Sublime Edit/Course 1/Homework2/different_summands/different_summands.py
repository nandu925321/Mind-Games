# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    k = n
    l = 1
    
    if(k<=2):
    	summands.append(k)
    	return summands
    
    while (k>0):

    	if(k<=(2*l)):
    		summands.append(k)
    		k = k - (2*l)
    	else:
    		summands.append(l)
    		k = k - l
    		l = l + 1



    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
