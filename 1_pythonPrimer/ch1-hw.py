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

def randz(data):
    length = len(data)
    indixList = random.randrange(0,length)
    return data[indixList] #I'm proud of this one!




#CREATIVITY 

# C1.13 - Write a pseudo-code description of a function that reverses a list of n integrs, so that the numbers are listed 
# in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same
# thing

def reverse(ints):

	for idx in ints:
		interim = []
		current = ints[idx] #initially i was going to try a for loops but with splicig you can do the below:

	return ints[::-1]

	# OR list comprehension below:

	return [array[n] for n in range(len(array)-1, -1, -1)]

# Another option using for loops

def reverse(my_list):
  L = len(my_list)
  for i in range(L/2):
    my_list[i], my_list[L-i - 1] = my_list[L-i-1], my_list[i]
  return my_list

 # C1.14 - Write a short Python function that takes a sequence of integer values and determines if there is a distint pair 
 # of numbers in the sequence whose product is odd.

 # The function below returns a list of unique odd numbers - any number in the returned list can be multiplied with any
 # other number to return an odd number



def oddPair(data):
	mySet = set(data)
	uniqueList = list(mySet)
	odds = []

	for idx in uniqueList:
		if (idx % 2 != 0):
			odds.append(idx)
	return odds

# practice = [1,1,2,3,4,4,5]

# print oddPair(practice) => output is [1,3,5]

# C1.15 - Write a Python function that takes a sequence of numbers and determines if all the numbers are different 
# from each other (that is, they are distinct)

# I'll have the program turn the list into a set then back into a list and compare the initial list with the new list
# that is unique values only and return True if they're the same

def unique(data):
	firstList = set(data)
	secondList = list(firstList)

	if(data == secondList):
		return True
	else:
		return False

# C1.16 - In our implementation of the scale function, the body of the loop executes the command data[j] *= factor. We have
# discussed that numeric types are immutable, and that use of the *= operator in this context causes the creation
# of a new instance (not the mutation of an existent instance). How is it still possible then, that our implementation
# of scale changes the actual parameter sent by the caller?

scale = scale * factor

#C1.17 Had we implemented the scale function as follows, does it work properly?

def scale(data, factor):
	for val in data:
		val *= factor
	return val #the book didn't have returned for the scale example -- python returns None type without a return statement

				#are they changing a global data variable, i.e. list? lists are mutable...

# C1.18 - Demonstrate how to use the Python's list comprehension syntax to produce the list 
#[0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
  # 2  4  6   8  10  12

return [x for x in range(91) ]
[idx*x for idx, x in enumerate(range(1,10))] #go over enumerate() function 


# C1.19 - Demonstrate how to use Python's list comprehension syntax to produce the list ['a', 'b', 'c'..'z']
# but without having to type all 26 such characters literally 

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]


# C1.20 - Python's random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the
# elements. Using only randint function, implement your own version of the shuffle function

# t = [1,2,3]
# a = t
# shuffle(a)

# print t [why do both print a and print t produce a shuffled t array? a is a pointer to t and t is not being shuffled]

#the below is not my version as I wasn't able to implement the code, but i'm studying it

def sub_shuffle(data, indexlist): 
    import random 
    index = random.randint(0, len(indexlist)-1) #this returns a random number
    #between 0 and the one less than indexlist
    rElement = data[indexlist[index]] #returns a random value from data array
    indexlist.pop(index) #remove the value from indexlist as to not repeat
    # value the data. if this didn't happen, the same number, say in [1,2,3] 
    # could be [1, 1, 2]
    return rElement 
 
def custome_shuffle(data): 
    indexes_of_data = range(len(data)) 
    return [sub_shuffle(data, indexes_of_data) for e in range(len(data))]


# print custome_shuffle([1,2,3,4])

# C1.21 - Write a python program that repeatedly reads lines from standard input until an EOFError is raised, and
# then outputs those lines in reverse order (a user can indicate end of input by typing ctrl-D)

def read(data):
	age = 1
	if age < 2:
		try:
			age = int(input("Enter other person's name"))
			data.append(age)
			if age < 0:
				print("Age must be a positive integer")
			read(data)
		except EOFError:
			print data[::-1]

if __name__ == "__main__": 
    data = [2,3,4] 
    read(data)















	
