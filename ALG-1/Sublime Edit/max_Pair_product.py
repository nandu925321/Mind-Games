# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
def max_pairwise_quadratic(a):

	for i in range(0, n):
	    for j in range(i+1, n):
	        if a[i]*a[j] > result:
	            result = a[i]*a[j]



def max_pairwise_product_2n(a):
	max_one = -1
	max_two = -1
	for i in range (0,n):
		if(a[max_one]<a[i] or max_one==-1):
			max_one = i



	for j in range(0,n):
		if((j!=max_one) and (a[max_two]<a[j] or max_two==-1)):
			max_two = j

	return a[max_one] * a[max_two]

print(max_pairwise_product_2n(a))
#print(result)
