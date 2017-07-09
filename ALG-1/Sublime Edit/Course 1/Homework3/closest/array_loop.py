#Uses python3
# Array loop problem
import sys

def check_loop(a,n):
	travelled  = 0
	travel_array = [] 
	for x in range(0,len(a)):
		travelled = travelled + a[x]
		if travelled in travel_array and a[x]!=0:
			travel_array.append(travelled)
			return True

		travel_array.append(travelled)

	return False



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:]
    print(check_loop(a,n))
    
