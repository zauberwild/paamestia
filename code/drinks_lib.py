"""
contains the recipe-class and drink-class
"""

class recipe:
	"""
	stores and handles the available recipes
	TODO rework / optimisation
	"""

	def __init__(self, path):
		self.path = path
		self.description = ""
		self.drinks = []
		self.vol = []
		self.loadRecipe()

	def loadRecipe(self, new_path = ""):
		""" load recipe
		- new_path: use to set a new recipe up
		"""
		if new_path == "":
			new_path = self.path

class drink:
	"""
	this class handles the spots, remembers the plugged drinks
	and controls the output
	"""

	def __init__(self,spot):
		self.spot = spot
		self.drink

	def assignDrink(self,drink):
		""" set a new drink
		- drink: the new drink
		"""
		pass

	def fill(self,vol):
		"""	start to fill the glass
		- vol: the needed volume in ml
		"""
		pass
