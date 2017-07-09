# Uses python3
import sys
import collections

def get_lottery_counts(n,p,a,search_items):
	#search_items.sort()
	#print(search_items)
	left = a[0::2]
	right= a[1::2]
	count_items = [0] * p
	#print(left)
	#print(right)
	ranges = dict(zip(left, right))
	#print(ranges)
	od = collections.OrderedDict(sorted(ranges.items()))
	#print(od)
	for l,r in od.items():
		for x in range (0,p):

			if (l<=search_items[x]<=r):
				count_items[x] = count_items[x] + 1
			#else:
				#break



	return count_items



if __name__ == '__main__':
    input = sys.stdin.read()
    n,p, *a = list(map(int, input.split()))
    #print (n)
    #print (p)
    #print (a)
    search_items = a[-p:]
    del a[-p:]
    #print(search_items)
    #print (a)
    results =  get_lottery_counts(n,p,a,search_items)
    print(*results, end = ' ')