# R2.4 - Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively represent the 
# name of the flower, its number of petals, and its price. Your class must include a constructor method that initializes
# each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving
# the value of each type

class Flower:

	def __init__(self, name, numberOfPetals, price):
		self.name = name
		self.numberOfPetals = numberOfPetals
		self.price = price

	def setName(name):
		self.name = name
		return type(self.name), self.name #if currently I take out the return self.name and run the below code below, the correct answer will 
		#still be returned... why? Is it changing the constructor?
		#also return type doesn't return the type, why


    def setPetals(self, numOfPets):
        self.numberOfPetals = numOfPets
        return type(self.numberOfPetals)

    def setPrice(self, price):
        self.price = price
        return self.price




new = Flower('rose', 5, 4)
new.setName("sun")
print(new.name)
#The above code works except for the return type of the values

#R2.5 - Use the techniques of Section 1.7 to revise the charge and make_payment methods of the CreditCard class to ensure that
#the caller sends a number as a parameter
#R2.6 - If the parameter to make_payment is negative, it will raise the balance. Add a ValueError for this case

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
        self._balance = 10

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

        # if price + self._balance > self._limit:
        #     return False
        # else:
        #     self._balance += price
        #     return True
        if not isinstance(price, (int,float)):
            raise TypeError('Price must be an integer')
        else:
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True

    def make_payment(self, amount):
        """ Process customer payment that reduces balance."""
        if not isinstance(amount, (int,float)) :
            raise TypeError("Amount must be a number")
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        else:
            self._balance -= amount


#R2.9 - Implement the __sub__ method for the Vector class of section 2.3.3 so that the expression u-v returns a new vector instance
#representing the difference between two vectors

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
    def __sub__(self, other):
        """Return the subtraction of two vectors"""
        sub = []
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        for v in self._coords:
            a = self._coords[v] - other[v]  #the add class just does self[j] whereas i do self._coords[j]..any difference?
            sub.append(a)
        return sub

vex = Vector(4)
a = vex.__sub__([3,3,3,3])
print(a)





