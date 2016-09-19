from math import log 
from functools import reduce


def entropy(data):
	l = len(data)
	data_set = set(data)

	temp_entropy = 0

	for subdata in data_set:
		temp_prob = data.count(subdata) / l
		temp_entropy -= temp_prob * log(temp_prob,2)
	return temp_entropy

def conEntropy(data,target_idx,entropy_idx=-1):

	l = len(data)
	target_set = set(data[i][target_idx] for i in range(l))
	temp_dict = {}
	temp_con_entropy = 0 

	for target in target_set:
		temp_dict[target] = []

		for j in range(l):
			if data[j][target_idx] == target:
				temp_dict[target].append(data[j][entropy_idx])

		target_prob = len(temp_dict[target]) / l
		temp_con_entropy += entropy(temp_dict[target]) * target_prob
		
	return temp_con_entropy


# def conEntropy(dataset,target_idx,entropy_idx=-1):
# 	l = len(dataset)
# 	target_list = [dataset[i][target_idx] for i in range(l)]
# 	target_set = set(target_list)
# 	conen_dict = {}
# 	temp_con_entropy = 0

# 	for target in target_set:
# 		conen_dict[target] = []
# 		for i in range(l):
# 			if dataset[i][target_idx] == target:
# 				conen_dict[target].append(dataset[i][entropy_idx])
# 		conen_dict[target] = [entropy(conen_dict[target])]
# 		conen_dict[target].append(target_list.count(target)/l)
# 		temp_con_entropy += reduce(lambda x,y:x*y,conen_dict[target])

# 	return temp_con_entropy



dataset = [[1,0,0,1,0],
			[1,0,0,2,0],
			[1,1,0,2,1],
			[1,1,1,1,1],
			[1,0,0,1,0],
			[2,0,0,1,0],
			[2,0,0,2,0],
			[2,1,1,2,1],
			[2,0,1,3,1],
			[2,0,1,3,1],
			[3,0,1,3,1],
			[3,0,1,2,1],
			[3,1,0,2,1],
			[3,1,0,3,1],
			[3,0,0,1,0]]

print(conEntropy(dataset,2))