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


