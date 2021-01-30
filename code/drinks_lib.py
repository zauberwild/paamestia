"""
contains the recipe-class and drink-class
"""

import globals as gl
import io_lib as io
import time

""" ### CLASSES ### """

class Recipe:
	"""
	stores and handles the available recipes
	"""

	def __init__(self, path):
		self.path = path
		self.description = ""
		self.drinks = []
		self.vol = []
		self.loadRecipe(path)

	def loadRecipe(self, new_path):
		""" load recipe
		- new_path: use to set a new recipe up
		"""
		self.path = new_path

class Drink:
	"""
	this class handles the spots, remembers the plugged drinks
	and controls the output
	"""

	def __init__(self,spot, drink=""):
		""" Drink class
		- spot: number of spot [0: cleaning water, 1-6: drink spots]
		- drink="": drink placed in this spot (opt.)
		"""
		self.spot = spot
		self.drink = ""

		self.filling = False
		self.t_start = 0
		self.vol = 0

	def setDrink(self,drink):
		""" set a new drink
		- drink: the new drink
		"""
		self.drink = drink

	def fill(self,vol):
		"""	start to fill the glass
		- vol: the needed volume in ml
		"""
		self.filling = True
		self.t_start = time.time()
		self.vol = vol
	
	def update(self):
		pass


""" ### FUNCTIONS AND VARIABLES ### """

""" drinks list """
drinks_list = []
def refresh_drinks_list():
	""" read "drinks" file and save in list """
	global drinks_list

	file = open(gl.drink_file_path, 'r')		# read file
	drinks_list = file.readlines()
	file.close()
	file = open(gl.drink_file_path, 'r')		# read file
	drinks_list = file.readlines()
	file.close()

	for idx, i in enumerate(drinks_list):		# remove trailing newline characters
		#drinks_list[idx] = drinks_list[idx].removesuffix("\n")
		if drinks_list[idx].endswith('\n'):
			drinks_list[idx] = drinks_list[idx][:-1]

refresh_drinks_list()

""" spots list """
spot = []
for i in range(7):
	spot.append(Drink(i))

""" recipes """