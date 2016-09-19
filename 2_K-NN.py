import numpy as np 
from collections import deque

dataset = np.array([[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]])
# dataset = np.random.randint(0,20000,size=(10000,2))

class Node(object):
	def __init__(self,point,left,right,split):
		self.point = point 
		self.left = left 
		self.right = right 
		self.split = split 

	def display(self,indent=0):
		print("(%d) %s %s"%(indent,'  '*indent,self.point))
		if self.left != None:
			self.left.display(indent+1)
		if self.right != None:
			self.right.display(indent+1)

	def __str__(self):
		return ("%s"%self.point)

def calcVariance(data):
	temp = ((data**2).mean()) - ((data.mean())**2)
	return temp 

def calcDistance(p1,p2):
	temp = sum((p1 - p2)**2)
	return temp

def constructKDTree(dataset):
	L = len(dataset)
	if L == 0:
		return 
	median = L //2 

	dimension = len(dataset[0])
	Vars = [calcVariance(dataset[:,i]) for i in range(dimension)]
	split = Vars.index(max(Vars))

	sorted_index = np.argsort(dataset[:,split])
	left_data = dataset[sorted_index[:median]]
	right_data = dataset[sorted_index[median+1:]]

	return Node(dataset[sorted_index[median]],
		constructKDTree(left_data),
		constructKDTree(right_data),
		split
		)

def constructDeque(kdtree,target,kddeque):

	while kdtree:	
		kddeque.append(kdtree)
		split = kdtree.split
		if target[split] < kdtree.point[split]:
			kdtree = kdtree.left
		else:
			kdtree = kdtree.right

	return kddeque 

def findNN(kdtree,target,k=1):

	kd_deque = constructDeque(kdtree,target,deque())
	kd_node = kd_deque.pop()
	min_point = kd_node.point 
	min_dist = calcDistance(target,min_point)

	while kd_deque:

		kd_node = kd_deque.pop()

		if calcDistance(target,kd_node.point) < min_dist:
			min_point = kd_node.point 
			min_dist = calcDistance(target,kd_node.point)

		s = kd_node.split

		if abs(target[s] - kd_node.point[s]) < min_dist:
			if target[s] < kd_node.point[s]:
				constructDeque(kd_node.right,target,kd_deque)
			else:
				constructDeque(kd_node.left,target,kd_deque)

	return min_point,min_dist 


tree = constructKDTree(dataset)
tree.display()
target = [5.1,3.1]
p,d = findNN(tree,target)
print(p)
print(d)