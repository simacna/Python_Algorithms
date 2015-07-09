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


# R1.5 - Give a single command that computes the sum from Excercise 1.4

# R1.6/R1.7 Write a short fufunction that takes a positive integer n and returns the sum of the squares of all the odd
# positive integers smaller than n

def oddSquare(n):
	return sum([x*2 for x in range(n) if (x%2 !=0)])

# R1.8 - Python allows negative integers to be used as indices into a sequence, such a a string. If string s has length n
# and expression s[k] is used for index -n <= k < 0, what is the equivalent index j>= 0 such that s[j] references the same 
# element?

strings = "testing" #string s (strings) with length n (7) 
#s[k] =>strings[k] index -n(-7) <= k < 0. j >= 0

def kay(n):
    for idx in n:
        print idx
        
        
        
kay(strings)

# R1.9 - What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80
return range(50, 90, 10)

#R1.10 - What parameters should be sent to the range constructor, to produce range with values to produce 8, 6, 4, 2...-8
return range(8, -10, -2)

#R1.11 - Demonstrate how to use Python's list comprehension syntax to produce the list [1,2,4,8,16,32,64,256]

return [pow(2,x) for x in range(0,9)]

# R1.12 - Python's random module includes a function choice(data) that returns a random element from a non-empty sequence. 
# The random module includes a more basic function randrange, with parametization similar to the built in range function,
# that returns a random choice from the given range. Using only the randrange function, implement your own version of the
# choice function




















	
