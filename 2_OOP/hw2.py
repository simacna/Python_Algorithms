# R2.4 - Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively represent the 
# name of the flower, its number of petals, and its price. Your class must include a constructor method that initializes
# each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving
# the value of each type

class Flower(name, numberOfPetals, price):

	def __init__(self, name, numberOfPetals, price):
		self.name = name
		self.numberOfPetals = numberOfPetals
		self.price = price

	def setName(name):
		self.name = name
		return self.name
