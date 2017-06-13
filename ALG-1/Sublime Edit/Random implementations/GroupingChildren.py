# Grouping children into a group of two where the age diference is at maximum one unit.
#Inputs:
#1. Array of children :-A
#2. Age gap difference :-D

# if these implementations are costly think of this as car fuelling problem with capacity D and distances in sorted order!! 
#Where the travel is not possible break and form a group. then starta  new group or simply skip the places 

import itertools
import sys
import numpy
from random import randint
import time

# implementation with itertools - save for later
#stuff = [1, 2, 3]
#for L in range(0, len(stuff)+1):
#  for subset in itertools.combinations(stuff, L):
#    print(subset)

# takes n squared + n
def groups_naive(age,D):
	result = []
	for i in range (len(age)):
		for j in range(i+1, len(age)):
			if ((max(age[i],age[j]) - min (age[i],age[j]))<=D):
				result.append([age[i],age[j]])

	print(result)
	#for x in result:
		#age.remove(x[0])
		#age.remove(x[1])
	
	return len(result)#+len(age)

# takes n 
def groups_itertools(age,D):
	#for i in range (0, len(age)+1):
	no = 0
	for subset in itertools.combinations(age,2):
		if((max(subset)-min(subset))<=D):
			no = no + 1


	return no #+ (len(age) - 2 * no)






#main
#ages = sys.stdin.readline()
#age = list(map(int, ages.split()))
#print(age)
#da = int(da)
#D = int(input("Enter age differece"))
age1 = numpy.random.randint(low=1, high=100, size = 10000)
D = randint(0,9)
print("length of the array", len(age1),age1)
print("difference ",D)
start = time.clock()
age1 = age1.tolist()
#age1 = sorted(age1)
print(groups_itertools(age1,D))
print("time taken ", time.clock() - start)  