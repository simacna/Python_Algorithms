
def mine(input):
	length = len(input)
	zeros = [0] * length
	for nums in range(length):
		# print nums    0 1 ... (length + 1)
		total = 0
		for inner in range(nums):
			total += input[inner]
		zeros[nums] = total/inner
	return zeroes




def sinaPrefix(S):
	n = len(S)
	A = [0] * n
	for j in range(n):
		total = 0
		for i in range(j + 1):
			total += S[i]
		A[j] = total/(j+1)
	return A

print(mine([1,2,3,4,5]))
print("=========")
print(sinaPrefix([1,2,3,4,5]))
