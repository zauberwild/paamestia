"""
recipe_class.py

contains the recipe-class
"""

class recipe:
	"""
	stores and handles the available recipes
	"""

	def __init__(self, path):
		self.path = path
		self.description
		self.drinks = []
		self.vol = []
		self.loadRecipe()

	def loadRecipe(self, new_path = self.path):
		""" load recipe
		- new_path: use to set a new recipe up
		"""
	
	def mixRecipe(self):
		"""ISSUE NEEDED? """