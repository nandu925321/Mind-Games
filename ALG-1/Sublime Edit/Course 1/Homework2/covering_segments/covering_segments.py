# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments=sorted(segments, key=attrgetter('end'))
    min_end = segments[0].end
    points.append(min_end)
    #print(points[-1])
    i = 1
    for s in segments:

    	if(i>1):
    		min_end = s.end
    	if(points[-1] in range (s.start, s.end)):
    		continue
    	if(s.start<=min_end):
    		if (min_end not in points):
    			points.append(min_end)

    	i = i + 1

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    #print (data)
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
