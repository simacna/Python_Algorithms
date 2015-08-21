# This chapter deals with objects


#Example of a CreditCard class

class CreditCard:
	 """A consumer credit card"""

     def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.
        The initial balance is zero.
        customer  the name of the customer (e.g. 'John Bowman')
        bank      the name of the bank (e.g. 'California Savings')
        acnt      the account identifier (e.g. '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """ Return name of customer. """
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """ Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied."""

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """ Process customer payment that reduces balance."""
        return self._balance -= amount



# The Constructor

cc = CreditCard("John Doe", '1st Bank', '5391 1111 1111 1111', 1000)



#Testing the Class
#We demonstrate some basic usage of the CreditCard class, inserting three cards into a list named wallet. We use loops to make some charges and payments, 
#and use various
#accessor to print results into the console.
#These tests are enclosed within a conditional: if __name__ == '__main__':
#so that they can be embedded in the source code with the class definition.

#the test provides METHOD COVERAGE as each of the methods is called at least once, but it does not provide STATEMENT COVERAGE as there is never a 
#case in which a charge is
#rejected due to the credit limit. 

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '1111 1111 1111 1111', 2500))
    wallet.append(CreditCard('John Cowman', 'California Federal', '2222 2222 2222 2222', 3500))
    wallet.append(CreditCard('John Dowman', 'California Finance', '3333 3333 3333 3333', 4500))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer=', wallet[c].get_customer())
        print('Bank=', wallet[c].get_bank())
        print('Account=', wallet[c].get_account())
        print('Limit=', wallet[c].get_limit())
        print('Balance=', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print ('New balance=', wallet[c].get_balance())
            print()

#Creating a class named Vector. 

class Vector:
    """ Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros"""
        self._coords =[0]*d

    def __len__(self):
        """Return the dimension of the vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """ Return jth coordinate of vector"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """set jth coordinate of vector a given value"""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other): #relies on __len__ method
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))  #start with vector of zeros

        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result #
    def __eq__(self, other):
        """Return True if vector has same coordinates as other"""
        return self._coords == other._coords #Personal question - other._coords? That isn't clicking for some reason
    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other
    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1]+ '>' #adapt list representation -- QUESTION. why not str.(self._coords)[0:-1]?


# vec1 = Vector(2)
# vec1.__setitem__(0,1)
# vec1[0] = 0
# vec1[1] = 1
# print vec1 ==> <0,1>. What is being called with vec1[x]? how is that being set?

#2.3.4

class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence"""
        self._seq = sequence #keep a reference to the underlying data
        self._k = -1    #will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1
        print "self._k", self._k #adding this to see what state self._k is in

        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return as an iterator."""
        return self


#Above does keep looping through as below example shows:

seq = SequenceIterator([2,3,5])
print seq.__next__() #2
print seq.__next__() #3
print seq.__next__() #5

#Below we implement out own range method

class Range:

    def __init__(self, start, stop=None, step=1):
        """Initializes a Range instance.
        Semantics is simlar to build-in range class"""

        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start #should be treaated as range(0, n)

        #calculate the effective length once
        self._length = max(0, (stop - start + step -1)//step)
        #need knowlede of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length
    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)"""
        if k<0:
            k+= len(self) #attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexErro('index out of range')

        return self._start + k * self._step



            
#2.4 - Inheritance. There are two ways in which a subclass can differentiate itself from its superclass. A subclass may specialize
# an existing behavior by providing a new implementation that overrides an existing method. A subcalss may also extend its superclass
# by providing brand new methods. 

#We'll examine our previous CreditCard class by providing examples of both specialization and extension.  Our definition begins
#with the syntax:

class PredatoryCreditCard(CreditCard):
    pass

#The body of the new class provides three member functions: __init__, charge, and process_month. The __init__ constructor serves
#very similar role to the original CreditCard constructor, except that for our new class, there is an extra parameter to specify
#the annual percentage rate.

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Creates a new predatory credit card instance. The initial balance is zero. 

        customer  the name of the customer (e.g. 'John Smith')
        bank      the name of bank
        acnt      the account identifier    
        limit     credit limit (measured in dollars)
        apr       annual percentage rate (e.g. 0.0825 for 8.25% APR)

        """

        super().__init__(customer, bank, acnt, limit)
        self._apr = apr


    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit. 
        Return True if charge was processed
        Return False and assess $5 fee if charge is denied

        """

        success = super().charge(price) #call inherited method
        if not success:
            self._balance += 5 #assess penalty
        return success  #caller expects return value

    def pocess_months(self):
        """Assess monthly interest on outstanding balanace."""

        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor


class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2 ...
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = 




#################################### Below is from book - stackoverflow questions #######################################

class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

ChildA() 
ChildB()

#Difference between the two above -- ChildB you don't explicitly call the Base class. For Python 3+ you can call super as such:
super().__init__()

###########################################################################################################################

#2.4.2 Hierarchy of Numeric Progressions
#As a second example of numeric progression, we develop a hierarchy of classes for iterating numeric progressions. 

class Progression:
    """ Iterator producing a generic progression

    Default iterator produces the whole numbers 0, 1, 2...
    """

    def __init__(self, start=0):
        """ Initialize current to the first value of progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.
        This should be overriden by a subclass to customize progression.
        By convention, if current is set to None, this designated the end of a finite progression.
        """

        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""

        if self._current is None:
            raise StopIteration
        else:
            answer = self._current  # record current value to return
            self._advance()         # advance to prepare for next time
            return answer           # return the answer

    def __iter__(self):
       """By convention, an iterator must return itself as an iterator"""
       return self #QUESTION - what does this return? The init constructor?

    def print_progression(self, n):
        """  Print next n values of the progression."""

        print (''.join(str(next(self)) for j in range(n))) #this line of code I do not understand







#An arithmetic progression class - while the default progression increases its value by one in each step, an arithmetic
#progression adds a fixed constant to one term of the progression to the next. 

class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression"""

    def __init__(self, increment=1, start=0):
        """ Create a new arithmetic progression
        increment the fixed constant to add to each term (default 1)
        start     the first term of the progression
        """

        super().__init__(start) #call super constructor/initialize base class
        self._increment = increment

    def _advance(self): #override inherited version
        """ Update current value by adding the fixed increment"""
        self._current += self._increment

#Geometric Progression

class GeometricProgression(Progression):
    """ Iterator producing a geometric progression"""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression

    base the fixed constant multiplied to each term (default 2)
    start first term of the progression
        """

        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying base"""

        self._current *= self._base


#Fibonacci Progression Class

class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""


    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression

        first   the first term of the progression (default 0)
        second  the second term of the progression (default 1)
        """

        super().__init__(first)  #start progression at first
        self._prev = second - first  #fictious value preceding the first

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current


#  QUESTION - why doesn't below work? What am I doing wrong here?
#h = FibonacciProgression(first=3, second=4)
#print (h._advance())



#Testing our subclasses below along with the desired output

if __name__ = '__main__':
    print('Default progression:')
    Progression().print_progression(10)

    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)

    print('Arithmetic progression with incrememnt 5 and start 2:')
    ArithmeticProgression(5,2).print_progression(10)

    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)

    print('GeometricProgression with base 3:')
    print GeometricProgression(3).print_progression(10)

    print('Fibonacci progression with default start values:')
    FibonacciProgression().print_progression(10)

    print('Fibonacci progression with start values 4 and 6:')
    FibonacciProgression(4,6).print_progression(10)


#2.4.3 - Abstract Base Classes

#Below is an example of using template method pattern and using abstract base classes

from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """Our own versioin of collections.Sequence abstract base class."""

    @abstractmethod

    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod

    def __getitem__(self, j):
        """ Return the elemnt at index j of the sequence. """

    def __contains__(self, val):
        """ Return True if val found in the sequence; False otherwise."""

        for j in range(len(self)):
            if self[j] == val:
                return True     #found match
        return False

        raise ValueError('value not in sequence') #never found a match

    def index(self, val):
        """ Return leftmost index at which val is found (or raise ValueError)"""

        for j in range(len(val)):
            if self[j] == val:  #leftmost match
                return j
        raise ValueError('value not in sequence') #never found a match

    def count(self, val):
        """Return the number of elememnts equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k


#two advanced Python techniques were used:
#1. We declare the ABCMeta class of the abc module as a metaclass of our Sequence class. A metaclass is different from a 
#superclass in that it provies a template for the class definition itself. Specifically, the ABCMeta declaration assures that the 
#constructor for the class raises an error. READ MORE ABOUT META CLASSES

#2. @abstractmethod decorator immediately before the __len__ and __getitem__ methods are declared. That declares
#these two particular methods to be abstract, meaning that we do not provide an implementation within our Sequence base class,
#but that we expect any concrete subclasses to support those two methods. Python enforces this expectation, by disallowing
#instantiation for any subclass that does not override the abstract methods with concrete implementation. !YOWZA!















