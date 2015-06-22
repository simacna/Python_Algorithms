print("Welcome to the GPA calculator")
print('Please enter all your letter grades, one per line.')
print("Enter a blank line to designate the end.")

points = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+': 3.33, 'B':3.0, 'B-':2.67,
			'C+': 2.33, 'C': 2.0, 'C-':1.67, 'D+': 1.33, 'D':1.0, 'F': 0.0}

num_courses = 0
total_points = 0
done = False

while not done:
	grade = input()
	if grade =='':
		done = True
	elif grade not in points
		print ('Unknown grade "{0}" being ignored'.format(grade))
	else:
		num_courses += 1
		total_points += points[grade]

if num_courses > 0:
	print('Your GPA is {0:.3'.format(total_points / num_courses))

#1.5 Functions

#first function example
#the first line, beginning with the keyword def, serves as the function's signature. 

def count(data, target):
	n = 0

	for item in data:
		if item == target:
			n += 1
	return n

#default parameter values. Python provides means for functions to support more than one possible calling signature called polymorphic functions
#say we declare:

def foo(a, b=15, c=16):


#say you give above foo(1,2,3), it will take those values; if you give it one (foo(1)), it will default to foo(1,15,16)
#however it is illegal to decalre a function as such: foo(a, b=15, c); if a parameter is set, all future parameters need to be defined


#1.6 Simple input and output

#sample program of using input

age = int(input('Enter your age in years: '))
max_heart_rate = 206.9 - (0.67 * age)
target = 0.65 * max_heart_rate
print('Your target fat-burning heart rate is', target)




#1.6.2 Files
# built in function open to open a file, with a second optional parameter determining the access mode. fp = open('sample.txt')
# r = reading, w = writing, a = appending
# fp.close(). files also support the for-loop syntax, with iteration being line by line (e.g. for line in fp:)

# Writing to a file
# when a file is writeable (fp = open('results.txt', 'w')), the syntax fp.write('Hello world. \n') writes a single
# line to the file with the given string. 

# 1.7 exception handling

# exception might result from a logical error or an unanticipated situation. exceptions (or errors) are objects that are
# raise (or thrown) by the code that encounters an unespected circumance. The Python interpreter can also raise
# an exception should it encounter an unexpected condition, like running out of memory.

# A raise error may be caught by a surrounding context that "handles" the exception in an appropriate fashion

def sqrt(x):
    if not isinstance(x, (int,float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative!')
    
    return math.sqrt(x)


# the built-in function, isinstance(obj, cls) reteurns True if object (obj), is an instance of class (cls), or any subclass
# of that type. 
# How much error checking to perform is a matter of debate as it can slow the program. Take below for example:

def sum(values):
	if not isinstance(values, collections.Iterable):
		raise TypeError("parameter must be an iterable type")
	total = 0
	for v in values:
		if not isinstance(v, (int, float)):
			raise TypeError('elements must be numeric')
		total += v
	return total

# A far more direct and clear implementation of this function:

def sum(values):
	total = 0
	for v in values:
		total += v
	return total


# Even without the explicit checks, appropriate exceptions are raised naturally by the code. In particular,
# if values is not an iterable type, the attempt to use the for loop raises TypeError reporting obj is not iterable


# 1.7.2 Cathing an Exception
# in order to not constantly check for raising an exception, it is best to use some methodologies that follow:
# 1. "look before you leap" - better to ensure that an error cannot rise rather than try catching it

if y!= 0:
	ratio = x/y
else:
	# ...do something else


# 2. "it is easier to ask for forgiveness than it is to get permission". implement this using try-except:

try:
	ratio = x/y
except ZeroDivisionError:
	# ...do something else

# the try block is the primary code to be executed. best used when thinking that the except case is unlikely
# exception handling is particularly useful when working with user input, or when reading from or writing files,
# because these are less predicble. 
# Exception are objects that can be examined when caught.

try:
	fp = open('sample.txt')
except IOError as e:
	print('Unable to open the file:', e)


# A try-statement may handle more than one type of exeption. For example consider the following:

age = int(input('Enter your age in years: '))

# this could fail for a variety of reasons. If we want to handle two or more types of errors in the same way,
# we can use a single except-statement as follow:

age = -1

while age <= 0:
	try:
		age = int(input('Enter your age in years'))
		if age <= 0:
			print('your age must be positive')
	except(ValueError, EOFError):
		print("invalid response")

# we use the tuple (ValueError, EOFError) to designate the types of errors that we wish to catch

# if we preferred to have the while loop continue without printing the 'invalid response' message, we could write:

	except(ValueError, EOFError):
		pass



# In order to provide different responses to different types of errors, we may use two or more except-clause
# as part of a try-structure. 

age = -1
while age <= 0:
	try:
		age = int(input("enter your age in yeras"))
		if age <= 0:
			print('Your age must be positive')
	except ValueError:
		print("That is an invalid age specification")
	except EOFError:
		print("There was an unexpected error reading input")
		raise


# 1.8 Iterators and generators

# Lazy evaluation: range(1000000) does not return a list of numbers; it returns a range object that is iterable
# # this object generates the million values one at a time, and only as needed. 

# We see lazy evaluation used in many of Python's libraries. E.g. the dictionary class supports methods keys(), values()
# and items(), which respective produce a 'view' of all keys, values, or (key, value) pairs within a dictionary. 


The most convenient technique for creating python iterators is through generators. generators look very similar to
functions but instead of returning a value, a yield statement is executed to indicate each element of the series.

As an ex. consider the goal of determing all factors of a positive integer. e.g. 100 has factors 1,2,4,5,10..100.

A traditional function might produce an return a list:

def factors(n):
	results = []

	for k in range(1, n+1):
		if n % k ==0:
			results.append(k)
		return results

In contrast, an implementation of a generator for computing those factors could be implemented as follows:

def factors(n):
	for k in range(1, n+1):
		if n%k==0:
			yield k

# yield keyword designates a generator. It is illegal to combine yield and return statements in the same implementation


# 1.9 Additional python conveniences

# 1.9.1 Conditional expression

# Python supports a conditional expression syntax that can replace a simple control structure. 
# General syntax is: expr1 if condition else expr2

# Ex:

if n>= 0:
	param = n
else:
	param = -n
result = foo(param)

# could be written as:

param = n if n >= 0 else -n
result = foo(param)

# OR:

result = foo(n if n >= 0 else -n)

# 1.9.2 Comprehension syntax

# In general, list Comprehension syntax:

# [expression for value in iterable if condition]. this is equivalent to:

result = []
for value in iterable:
	if condition:
		result.append(expression)

# ex:

squares = []
for k in range(1, n+1):
	squares.append(k*k)

# with list comprehension, this is equivalent to:
squares = [k*k for k in range(1, n+1)]





















