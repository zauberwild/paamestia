"""
contains the recipe-class and drink-class
"""

import globals as gl
import io_lib as io
import os
import time

""" ### PATHS ### """
dir_recipes = gl.gen_path + "/src/recipes/"

""" ### STORAGE ### """
plugs = ["cleaning_water", "", "", "", "", "", ""]			# stores the drinks plugged in

drinks = []													# stores the available drinks to choose from

recipes = []												# stores all recipes that could be found in the recipe folder


""" ### SETUP ### """
# this part will run once, as soon this file is imported somewhere

# look for drinks
file1 = open(gl.gen_path + "/src/drinks", 'r')			# open file
drinks = file1.readlines()								# save lines as a list
file1.close()

for idx, i in enumerate(drinks):						# remove trailing newline characters
		if drinks[idx].endswith('\n'):
			drinks[idx] = drinks[idx][:-1]

# look for recipes
for filename in os.listdir(gl.gen_path + "/src/recipes"):
	recipes.append(filename)

""" ### test availability ### """
def _test_availability(recipe):
	global drinks

	file1 = open(dir_recipes + recipe, 'r')			# open file
	needed_drinks = file1.readlines()								# save lines as a list
	file1.close()

	needed_drinks.pop(0)			# remove info line

	for idx, i in enumerate(needed_drinks):
		if needed_drinks[idx].endswith('\n'):						# remove trailing newline characters
			needed_drinks[idx] = needed_drinks[idx][:-1]

		c_idx = needed_drinks[idx].find(',')						# remove volume information
		needed_drinks[idx] = needed_drinks[idx][:c_idx]
	
	#print("DR TA needed drinks:")
	#print(needed_drinks)
	#print("DR TA set drinks:")
	#print(plugs)
	
	for d in needed_drinks:
		if not d in plugs:
			#print("DR TA d: " + str(d))
			return False												# return False, if drink d is not plugged in
	
	return True															# return True, as everything seems to be there


""" ### set drinks ### """
def set_drink(plug, drink):
	""" set drink
	plug: number of the plug (1-6) [int]
	drink: EITHER drink name or "None" for reset [string] OR index for drinks list (1-end of list, because 0 is cleaning_water) (-1: reset) [int]
	"""
	global drinks, plugs

	print("DR SD set drinks started")

	if plug < 1 or plug > 6:
		return					# break when wrong plug given
	
	print("DR SD plug range test passed")

	if not (type(drink) == int or type(drink) == str or drink is None):		# break when input type not correct
		return
	
	print("DR SD drink type test passed")

	if type(drink) == int:		# get drink name when index given
		drink = drinks[drink]
	
	print("DR SD index conversion passed")
	
	if not (drink in drinks or drink is None):
		return					# break when drink is not available
	
	print("DR SD drink existence check passed")
	
	plugs[plug] = drink			# set drink on plug


""" ### GETTER METHODS ### """
def get_drinks():
	return drinks

def get_plugs():
	return plugs

def get_recipes(available=None):
	""" returns recipes
	available=None: filter recipes 
	[None: no filter, True: returns only available recipes, False: returns only unavailable recipes]
	"""
	global recipes

	return_list = []

	if available == None:
		return_list = recipes
	elif available == True:
		for r in recipes:
			if _test_availability(r):
				return_list.append(r)
	elif available == False:
		for r in recipes:
			if not _test_availability(r):
				return_list.append(r)
	
	return return_list


""" ### ### MIXING METHODS ### ### """
""" variables """
is_mixing = False
recipe_step = 0
commands = []
finishing_time = 0

""" function """
def start_mixing(recipe):
	""" starts the mixing process.
	recipe: EITHER as string with recipe name OR as int with index in recipes list
	"""
	global is_mixing, recipe_step, commands, recipes

	#print("DR function started")

	if type(recipe) != int and type(recipe) != str:		# break when input type not correct
		return
	
	#print("DR input type check passed")

	if type(recipe) == int:								# get recipe name when index given
		recipe = recipes[recipe]
	
	#print("DR index conversion passed")
	
	if not _test_availability(recipe):					# break when recipe not available
		return
	
	#print("DR availability check passed")
	
	file1 = open(dir_recipes + recipe, 'r')			# open file
	steps = file1.readlines()								# save steps as a list
	file1.close()

	steps.pop(0)			# remove info line

	for idx, i in enumerate(steps):
		if steps[idx].endswith('\n'):						# remove trailing newline characters
			steps[idx] = steps[idx][:-1]

	commands.clear() 		# delete previous commands
	""" compile recipe """
	for step in steps:
		list = step.split(',')							# [<drink>, <volume>]
		time = int(list[1]) * gl.TIME_PER_ML			# calculate needed time
		plug = plugs.index(list[0])						# get the plug

		#print("DR compile log, step:" + str(step) + " ; volume: " + str(int(list[1])) + " ; time: " + str(time))
		# add steps to commands list
		commands.append("o" + str(plug))
		commands.append("t" + str(time))
		commands.append("w")
		commands.append("c" + str(plug))
	
	commands.append("e")
	#print("DR gl.TIME_PER_ML = " + str(gl.TIME_PER_ML))
	print("DR SM compiling done")
	print("DR commands:")
	for c in commands:
		print(c)

	# start the mixing process
	is_mixing = True
	recipe_step = 0	


def update_mixing():
	global is_mixing, recipe_step, commands, finishing_time

	if is_mixing:				# stop if no cocktail is currently mixed
		cmd = commands[recipe_step]
		if cmd[0] == 'o':					# open valve
			print("DR UM open valve " + str(cmd[1]))
			io.writeOutput(io.VALVES[int(cmd[1])], 1)
			io.writeOutput(io.PUMP, 1)
			recipe_step += 1 					# advance to next step

		elif cmd[0] == 'c':					# close valve
			print("DR UM close valve " + str(cmd[1]))
			io.writeOutput(io.VALVES[int(cmd[1])], 0)
			io.writeOutput(io.PUMP, 0)
			recipe_step += 1 					# advance to next step

		elif cmd[0] == 't':					# set timer
			print("DR UM set timer " + str(float(cmd[1:]) / 1000.0))
			finishing_time = time.time() + (float(cmd[1:]) / 1000.0)
			recipe_step += 1 					# advance to next step

		elif cmd[0] == 'w':					# wait
			t = time.time()
			#print(str(finishing_time) + " ::: " + str(t) + " ::: " + str(t >= finishing_time))
			if t >= finishing_time:				# if waited long enough, advance to next step
				recipe_step += 1
				
		elif cmd[0] == 'e':					# end sign
			print("DR UM end mixing")
			is_mixing = False	
		

		# add debug information
		if gl.show_debug:
			gl.debug_text.append("MIX cur. cmd.: " + str(cmd) + "; prev. cmd.: " + str(commands[recipe_step-1]))
			gl.debug_text.append("MIX cmd nr.: " + str(recipe_step) + " / " + str(len(commands)))

def get_still_mixing():
	global is_mixing
	return is_mixing