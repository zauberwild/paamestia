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
	gl.prog_pos = 'm'		# DEL when intro needed

	global intro_active, introduction_vid

	if intro_active == False:
		intro_active = True
		introduction_vid.start(audio=False)			# start intro
	
	introduction_vid.draw()				# draw intro

	if introduction_vid.test_for_last_frame():			# test if intro is ending
		intro_active = False
		gl.prog_pos = 'm'

menu_active = False
btn1 = None
btn2 = None
btn3 = None
menu_pos = 0
def main_menu():
	global menu_active, btn1, btn2, btn3, menu_pos	
	
	if menu_active == False:			# setup
		menu_active = True
		btn1 = media_lib.Button("/src/", "prop_black.png", "prop_red.png", "prop_grey.png", 32, 0, 700, 64, selected=True)
		btn2 = media_lib.Button("/src/", "prop_black.png", "prop_yellow.png", "prop_grey.png", 32, 128, 700, 64)
		btn3 = media_lib.Button("/src/", "prop_black.png", "prop_green.png", "prop_grey.png", 32, 256, 700, 64)
		btn1.add_text("erster knopf", gl.debug_font_big, (0,0,255), alignment=1)
		btn2.add_text("zweiter knopf", gl.debug_font_big, (0,0,255), alignment=0)
		btn3.add_text("dritter knopf", gl.debug_font_big, (0,0,255), alignment=2)
	
	# input
	if io.readInput(io.UP):
		menu_pos -= 1
	if io.readInput(io.DOWN):
		menu_pos += 1
	
	# logic
	if menu_pos < 0:
		menu_pos = 2
	if menu_pos > 2:
		menu_pos = 0
	
	btn1.selected = False
	btn2.selected = False
	btn3.selected = False
	if menu_pos == 0:
		btn1.selected = True
	elif menu_pos == 1:
		btn2.selected = True
	elif menu_pos == 2:
		btn3.selected = True

	# draw
	gl.screen.fill((127,127,127))
	btn1.draw()
	btn2.draw()
	btn3.draw()

	gl.debug_text.append("menu_pos: " + str(menu_pos))

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