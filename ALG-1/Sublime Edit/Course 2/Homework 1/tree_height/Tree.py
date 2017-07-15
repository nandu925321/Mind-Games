# python3

import sys


def explore(x, tree, height):
	
def TreeHeight_DFS(tree,n,start):

	# sort the list first to get root at the start
	#tree = tree.sort(key = lambda x:x.key)

	height = 1
	children = tree[start].children
	for x in children:
		explore(x,tree,height)

	return height


class Node:
	def __init__(self,key,parent,children):
		self.key = key
		self.parent = parent
		self.children = children


def Build(n,parents):
	# Tree represented as array of nodes
	tree = []
	# fill the tree

	if not parents:
		return 0 
	for i in range (0,n):
		label = i
		key = parents[i]
		# exception for root
		if key== -1:
			parent = -1
			label = -1
			children = [i for i, x in enumerate(parents) if x == 1]
		else:
			parent = parents[key]
			children = [s for s, x in enumerate(parents) if x == i]
		n = Node(label,parent,children)
		#n.allocate(key,parent,children)
		tree.insert(i,n)

		

	# check if the tree is built properly
	for n in tree:
		print(n.key)
		print(n.parent)
		print(n.children)
		print("----------------------")

	start = parents.index(-1)
	#return TreeHeight_DFS(tree,n,start)







n = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))
Build(n,parents)