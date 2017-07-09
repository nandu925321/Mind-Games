# Uses python3
import sys
import random

count = 0
def Merge(B,C,D):
	# D is an array with the length of len(B) + len(C)
	global count 
	while len(B)>0 and len(C)>0:
		b = B[0]
		c = C[0]

		if b<=c:
			#cs = cs + 1
			#set_global_count(cs)
			D.append(b)
			B.remove(b)
		else:
			count = count +(len(B))
			#set_global_count(cs)
			D.append(c)
			C.remove(c)
	if(len(B)>0):
		D = D + B
	if(len(C)>0):
		D = D + C

	return D


def MergeSort(a):
	n=len(a)
	if(n<2):
		return a

	
	D = []
	#count = 0
	m = n//2
	#left
	B = MergeSort(a[:m])
	C = MergeSort(a[m:])

	new_A = Merge(B,C,D)
	#count = count+m
	
	
	

	return new_A

def msort3(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x) / 2)
    y = msort3(x[:mid])
    z = msort3(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


def msort2(x):
    if len(x) < 2:
        return x
    result = []          # moved!
    mid = int(len(x) / 2)
    y = msort2(x[:mid])
    z = msort2(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    return result

def merge_sort(x):

    if len(x) < 2:return x

    result,mid = [],int(len(x)/2)

    y = merge_sort(x[:mid])
    z = merge_sort(x[mid:])

    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:result.append(z.pop(0))   
            else:result.append(y.pop(0))

    result.extend(y+z)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    l = []
    a=MergeSort(a)
    #count = a[len(a)-1]
    #a.remove(count)
    #a=merge_sort(a)
    for x in a:
        print(x, end=' ')
    print("The number of inversions are",count )
