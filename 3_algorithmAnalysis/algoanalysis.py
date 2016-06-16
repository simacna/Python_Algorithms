# We are interested in characterizing an algorithm's running time as a function of the input size.

# 3.1 - Experimental studies

from time import time
# start_tinme = time()
# # run algorithm
# end_time = time()
# elapsed = end_time - start_time

# Because many processes share use of a computer central processing unit (CPU), the elapsed time will depend on what other
# processes are running on the computer when the test is performed. 
# A fairer metric is the number of CPU cycles that used by the algorithm. This can be determined using the clock function of the time
# module, but even this measure might not be consistent if repeating the identical algo on the identical input

# start_time = time()
#below function is a O(n)
def find_max(input):
	""" Return the maximum element from a nonempty Python list. """
	biggest = input[0]
	for idx in input:
		if idx > biggest:
			biggest = idx
	return biggest

# elapsed_time = start_time - end_time
# print(elapsed_time)
start_time = time()
find_max([1,3,4,5,6,7])
end_time = time()

elapsed_time = start_time - end_time

# print(elapsed_time)

def rice(number_of_boxes):
	max_size = number_of_boxes
	init = 1
	increasing = 1
	while init < max_size:
		increasing *= 2
		max_size -= 1
	return increasing
# print(rice(64))


def Prefix1(S):
	""" 
	This algo has a O(n^2) running time
	"""
	n = len(S) #executes in constant time
	A = [0] * n #causes the creation of and initialization of a python list with len n
	# this uses a constant number of primitive operations per element, and thus runs O(n)

	#below are two nested for loops which are controlled by counters j, i. body of outer loop is controlled by counter j n times, so total = 0
	# and A[j] = total/(j+1) are executed n times each
	for j in range(n):
		total = 0
		for i in range(j + 1): #n(n+1)/2 => O(n^2)
			total += S[i]
		A[j] = total/(j+1)
	return A




















