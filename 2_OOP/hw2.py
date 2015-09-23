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

