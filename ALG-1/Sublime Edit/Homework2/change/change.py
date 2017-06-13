# Uses python3
# Implement change conversion problem in denominations of 1, 5 and 10
import sys

def get_change(m):
    #write your code here
    coins = 0
    while(m>0):
    
    	# start with higher denominations first
    	if(m-(m%10)>0):
    		m = m - 10
    		coins = coins + 1
    		continue
    	if(m-(m%5)>0):
    		m = m - 5
    		coins = coins + 1
    		continue
    	if(m-(m%1)>0):
    		m = m - 1
    		coins = coins + 1
    		continue
    
    return coins


    

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
