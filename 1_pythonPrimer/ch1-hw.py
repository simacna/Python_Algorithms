# Reinforcement

# R1.1 - Write a short Pythhon function, is_multiplie(n,m), that takes two integer values and returns True if n is a 
# multiple of m, that is n = mi for some integer i, and False otherwise

def is_multiple(n,m):
	if (n%m == 0):
		return True
	else:
		return False

# R1.2 - Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise.
# However, your function cannot use the multiplication, modulo, or division operator.

def is_even(k):
	try: 
        return int(k) & 1 == 0 
    except ValueError: 
        print(”Number must be Integer values”)


# R1.3 - Write a short Python function, minmax(data), that takes a sequence of one or more numbers and returns the smallest
# and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing
# your solution. 

def minmax(*args):
	return args

	#don't know how to proceed

# R1.4 - Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive
# integers smaller than n


def sum(n):
	return sum([pow(x,2) for x in range(n) if n > 0])














	
