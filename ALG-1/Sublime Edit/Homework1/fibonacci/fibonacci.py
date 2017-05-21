# Uses python3
import time
def calc_fib(n):
    if (n <= 1):
    	return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def better(n):
	if(n<=1):
		return n

	prev = 0
	curr = 1
	for i in range(n-1):
		#prev,curr = curr,prev+curr
		temp = curr
		curr = curr+prev
		prev = temp


	return curr
		 









n = int(input())

#start = time.time() 
print(better(n))
#end = time.time()         

#stopWatch=end-start
#print(stopWatch)
