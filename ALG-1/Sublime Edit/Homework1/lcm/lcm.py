# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def better(a,b):
	# use lcm * gcd = a*b
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

	lcm = (a * b)//default_gcd
	return lcm

if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(better(a, b))

