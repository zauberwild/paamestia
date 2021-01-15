"""
this file include all methods for the user interface
"""

import pygame				# ISSUE [i7] drawing single sprites: in method or as class in medialib ?
import globals as gl
import media_lib
import drinks_lib
import io_lib as io

""" ### ### INTRO / MAIN MENU ### ### """
def intro():
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
		io.writeOutput(io.VALVES[0], 1)
	if io.readInput(io.BACK):
		io.writeOutput(io.VALVES[0], 0)

def main_menu():
	pass

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