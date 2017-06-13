#Uses python3

import sys

def Compare_digit_places(d, max_digit):
	if(int(d+max_digit)>=int(max_digit+d)):
		return True
	else:
		return False
def largest_number(a):
    #write your code here
    #print(int_a)
    res = ""
    while (len(a)>0):
    	max_digit = -1
    	for d in a:
    		if (max_digit == - 1 or Compare_digit_places(d,max_digit)):
    			max_digit = d
    	res = res + max_digit
    	a.remove(max_digit)
    
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
