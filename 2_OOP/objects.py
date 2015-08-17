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
#We demonstrate some basic usage of the CreditCard class, inserting three cards into a list named wallet. We use loops to make some charges and payments, and use various
#accessor to print results into the console.
#These tests are enclosed within a conditional: if __name__ == '__main__':
#so that they can be embedded in the source code with the class definition.

#the test provides METHOD COVERAGE as each of the methods is called at least once, but it does not provide STATEMENT COVERAGE as there is never a case in which a charge is
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

            
























