# car fuelling implementation

#problem :- select the minimum number of stops for fuel along the path length L. Assume initially the car has full tank gas.
#capacity of the car is C
# inputs:
#1.Array of stops in distance from start to end
#2.Capacity of the car C
#3.Total path distance L

import sys
def stops(da,capacity,length):
	tank = capacity
	stops = 0
	distance_travelled = 0
	for i in range(len(da)):
		distance_travelled = distance_travelled + da[i]
		tank = tank-da[i]
		if(tank>=da[i]):
			print("no refuel continue")
			#continue
			if(i == len(da)-1):
				if(tank>=length-distance_travelled):
					continue
				else:
					print("travel not possible")
					break


		elif(tank<da[i] and length-distance_travelled>0):
			stops = stops + 1
			to_fill = capacity-tank
			tank = tank + to_fill
			if(i == len(da)-1):
				if(tank>=length-distance_travelled):
					continue
				else:
					print("travel not possible")
					break



	return stops


#main
distances = sys.stdin.readline()
da = list(map(int, distances.split()))
print(da)
#da = int(da)
capacity = int(input("Enter tank capacity"))
length = int(input("Enter the total length of the path"))
print("Number of stops are:")
print(stops(da,capacity,length))
#main - copy paste code to read from standard input - modify this
#input = sys.stdin.readline()
#n = int(input)
#print(fib(n))