"""
this file include all methods for the user interface
"""

import globals as gl
import media_lib
import drinks_lib
import io_lib as io

""" ### ### SETUP / LOOP ### ### """
""" actions that need to be executed once on startup are here 
	This includes object creation, reading files in, etc.
"""

# intro
introduction_vid = media_lib.Video("/src/media/intro/intro.mp4", "/src/media/intro/audio.wav")

""" EOF SETUP """

def loop():
	""" actions that need to be executed every loop (independently from prog_pos are here)
		this method will be called before any other actions in the main loop
	"""
	io.keyboard_input()		# keyboard input
	io.update_input()		# button input

	# debug information about input and output
	if not gl.prog_pos == 'i':
		i_s = "O: "
		for i in io.valves_state:
			i_s += str(int(i)) + "; "
		i_s += str(int(io.pump_state))
		gl.debug_text.append(i_s)
		i_s = "I: up: " + str(int(io.readInput(io.UP))) + "; down: " + str(int(io.readInput(io.DOWN))) + "; left: " + str(int(io.readInput(io.LEFT))) + "; right: " + str(int(io.readInput(io.RIGHT))) + ";"
		gl.debug_text.append(i_s)
		i_s = "I: next: " + str(int(io.readInput(io.NEXT))) + "; back: " + str(int(io.readInput(io.BACK)))
		gl.debug_text.append(i_s)

""" ### ### INTRO / MAIN MENU ### ### """
intro_active = False
def intro():
	#gl.prog_pos = 'm'		# DEL when intro needed

	global intro_active, introduction_vid

	if intro_active == False:
		intro_active = True
		introduction_vid.start(audio=False)			# start intro
	
	introduction_vid.draw()				# draw intro

	if introduction_vid.test_for_last_frame():			# test if intro is ending
		intro_active = False
		gl.prog_pos = 'm'

def main_menu():
	gl.screen.fill((127,127,127))
	if io.readInput(io.UP):
		io.writeOutput(io.VALVES[1], not io.valves_state[1])
	if io.readInput(io.DOWN):
		io.writeOutput(io.VALVES[2], not io.valves_state[2])
	if io.readInput(io.LEFT):
		io.writeOutput(io.VALVES[3], not io.valves_state[3])
	if io.readInput(io.RIGHT):
		io.writeOutput(io.VALVES[4], not io.valves_state[4])
	if io.readInput(io.NEXT):
		io.writeOutput(io.PUMP, 1)
	if io.readInput(io.BACK):
		io.writeOutput(io.PUMP, 0)

""" ### ### FREE MIXING ### ### """
def free_transition():
	pass

def free_choose():
	pass

def free_output():
	pass


""" ### ### RECIPE ### ### """
def recipe_transition():
	pass

def recipe_choose():
	pass

def recipe_output():
	pass


""" ### ### SETTINGS ### ### """
def settings():
	pass

""" ### SHUTDOWN ### """
def shutdown():
	pass