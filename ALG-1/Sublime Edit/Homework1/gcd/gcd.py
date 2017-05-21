# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def better(a,b):
	default_gcd = 1
	
	small=min(a,b)
	big=max(a,b)
	i=0
	while(True):
		rem = big % small
		if(rem==0):
			if(small>default_gcd):
				default_gcd=small
			break
		big=small
		small=rem
		
	return default_gcd

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(better(a, b))
