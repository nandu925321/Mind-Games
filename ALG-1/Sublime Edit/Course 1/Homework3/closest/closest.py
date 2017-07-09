#Uses python3
import sys
import math
def calculate_strip(strip,distances,d):

	# this loop rund only 6 times according to a geometric proof 
	sorted_strip = sorted(strip , key = lambda p:(p[1],p[0]))
	for x in range(0,len(strip)):
		point_a = strip[x]
		for y in range(x+1, len(strip)):
			point_b = strip[y]
			new_d = eud(point_a,point_b)
			if(new_d<d):
				d = new_d
				distances[d] = zip(point_a,point_b)

	return d

def eud(point_one,point_two):
	part_one = (point_one[0]-point_two[0]) ** 2
	part_two = (point_one[1]-point_two[1]) ** 2
	return math.sqrt(part_one+part_two)

def xcal_eu(A,B,distances,n):
	# if len of A and B is not n and A and B is not empty calculate eu
	#print(A)
	#print(B)
	#if(a+b!=n):
	while(len(A)>0 and len(B)>0):
			for x in range(len(A)):
				point_one = A[x]
				for y in range(len(B)):
					
					point_two = B[y]
					distance = eud(point_one,point_two)
					distances.append(distance)

def calc_dis(sorted_points,distances):

# return the minimum of calculated distances
	for x in range(0,len(sorted_points)):
		point_one = sorted_points[x]
		for y in range(x+1,len(sorted_points)):
			point_two = sorted_points[y]
			distance = eud(point_one,point_two)
			#add zero distance optimization here
			if distance == 0:
				distances[distance] = zip(point_one,point_two)
				return 0

			distances[distance] = zip(point_one,point_two)
	return min(distances)




def recursive_count(sorted_points,distances,n):
	if len(sorted_points)<=4:
		return calc_dis(sorted_points,distances)
	mid = len(sorted_points)//2

	# write to recursively calculate eucledian distances and append to the distance array
	minL = recursive_count(sorted_points[:mid],distances,n)
	minR = recursive_count(sorted_points[mid:],distances,n)

	d  = min(minL,minR)
	#print(sorted_points[mid])
	mid_point = sorted_points[mid]
	strip = []
	for point in sorted_points:
		#check distance from mid line based on x axis, if the point is mid point ignore.
		if point==mid_point:
			continue
		if(abs(point[0]-mid_point[0])<d):
			strip.append(point)

	#print(strip)
	if(len(strip)>2):
		min_y = calculate_strip(strip,distances,d)
		d = min(min_y,d)
	
	#return d
	return d

def minimum_distance(n,x,y):
    #write your code here
    #create a ordered tuple from the x and y points
    points = []
    distances = {}
    for i in range(n):
    	points.append((x[i],y[i]))
    # sort the points based on x co ord first if the same x co ord sort it with y co ord
    sorted_points = sorted(points , key = lambda p:(p[0],p[1]))
    #print(sorted_points)
    min_d = recursive_count(sorted_points,distances,n)

    #return 10 ** 18
    return  min_d

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(n,x, y)))
