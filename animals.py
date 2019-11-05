class Mammal:
	def __init__(self, species='Unknown'):
		self.__species=species

	def showSpecies(self):
		print('I am a ', self.__species)

	def makeSound(self):
		print('Grrr')

class Dog(Mammal):
	def __init__(self):
		Mammal.__init__(self,'dog')
	def makeSound(self):
		print('Wof Wof')

class Cat(Mammal):
	def __init__(self):
		Mammal.__init__(self,'cat')
	def makeSound(self):
		print('Meow')