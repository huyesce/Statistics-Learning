def calcProb(data,target,target_idx,lambda_=1):
    # lambda =1 : Laplace smoothing 
	l = len(data)
	target_idx_list = [data[i][target_idx] for i in range(l)]
	S = len(set(target_idx_list))

	temp_prob = (target_idx_list.count(target) + lambda_) / (l + S * lambda_)

	return temp_prob


def getSubData(dataset,target,target_idx):

	l = len(dataset)
	temp_set = []

	for i in range(l):
		if dataset[i][target_idx] == target:
			temp_set.append(dataset[i])

	return temp_set


def navieBayes(data,target):
	L = len(data)
	D = len(data[0]) - 1

	class_label = set(data[i][-1] for i in range(L))

	CL_prob = {}

	for label in class_label:
		temp_data = getSubData(data,label,-1)
		temp_prob = calcProb(data,label,-1)


		for i in range(D):
			temp_prob *= calcProb(temp_data,target[i],i)    


		CL_prob[label] = temp_prob
	return CL_prob


if __name__ == "__main__":
	dataset = [[1,1,-1],
				[1,2,-1],
				[1,2,1],
				[1,1,1],
				[1,1,-1],
				[2,1,-1],
				[2,2,-1],
				[2,2,1],
				[2,3,1],
				[2,3,1],
				[3,3,1],
				[3,2,1],
				[3,2,1],
				[3,3,1],
				[3,3,-1]]
	target = [2,1]

	print(navieBayes(dataset,target))
	print(1/45)
	print(1/15)