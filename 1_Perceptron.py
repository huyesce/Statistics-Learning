import numpy as np 

dataset = np.array([[3,3,1],[4,3,1],[1,1,-1]])

# class Perceptron(object):
# 	def __init__(self,data):
# 		self.data = data
# 		self.w = [0 for i in range(len(data[0])-1)]
# 		self.b = 0

# 	def sign(self,w,b,subdata):
# 		temp = np.dot(subdata[0:-1],w) + b
# 		return temp 

# 	def calc(self,step=1):
# 		L = len(self.data)

# 		Tag = True
# 		while Tag:
# 			Tag = False
# 			index = np.random.randint(0,L)
# 			if self.data[index][-1]*self.sign(self.w,self.b,self.data[index]) <= 0:
# 				self.w += step * self.data[index][-1]*self.data[index][0:-1]
# 				self.b += step * self.data[index][-1]

# 			for i in range(L):
# 				if self.data[i][-1]*self.sign(self.w,self.b,self.data[i]) <= 0:
# 					Tag = True
# 					break
# 		return self.w,self.b

# p = Perceptron(dataset)
# print(p.calc())


class Perceptron(object):
	def __init__(self,data):
		self.data = data 
		self.L = len(data)
		self.dimension = len(data[0])-1
		self.alpha = [0 for i in range(self.L)]
		self.b = 0 
		self.GramMatrix()

	def GramMatrix(self):
		self.Gram = np.array([[np.dot(self.data[i][0:-1],self.data[j][0:-1]) for i in range(self.L)] for j in range(self.L)])

	def sign(self,alpha,b,index):
		temp = (alpha * self.data[:,-1] * self.Gram[index]).sum() + b
		print(temp)
		return temp

	def calc(self,step=1):
		tag = True

		while tag:
			tag = False
			rand_idx = np.random.randint(0,3)

			if (self.data[rand_idx][-1] * self.sign(self.alpha,self.b,rand_idx)) <= 0:
				self.alpha[rand_idx] += step 
				self.b += step * self.data[rand_idx][-1]

			for i in range(self.L):
				if self.data[i][-1] * self.sign(self.alpha,self.b,i) <= 0 :
					tag = True 
					break 
		return self.alpha,self.b


p = Perceptron(dataset)
print(p.calc())