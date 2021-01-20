"""
handles input / output
"""
import globals as gl
import pygame
pygame_events = None

""" ### ### general input ### ### """
def keyboard_input():
	global pygame_events

	pygame_events = pygame.event.get()			# save all current events

	for event in pygame_events:					# check for keyboard input
			# closing window / exit program
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				gl.prog_active = False
			if event.type == pygame.KEYDOWN:
				# debug information
				if event.key == pygame.K_d:
					gl.show_debug = not gl.show_debug
				# return to intro
				if event.key == pygame.K_i:
					gl.prog_pos = 'i'

""" ### ### button input ### ### """
UP, DOWN, LEFT, RIGHT, NEXT, BACK = 14, 15, 21, 23, 24, 25		# NOTE Buttons: set corresponding pins here

if gl.os_is_linux:								# create button objects to read gpio pins
	from gpiozero import Button, LED
	UP_BT, DOWN_BT, LEFT_BT, RIGHT_BT, NEXT_BT, BACK_BT = Button(UP), Button(DOWN), Button(LEFT), Button(RIGHT), Button(NEXT), Button(BACK)
def readInput(input):
	""" read signal from input. returns bool
	input: chosen input [UP, DOWN, LEFT, RIGHT, NEXT, BACK] or any other gpio pin
	"""
	global UP, DOWN, LEFT, RIGHT, NEXT, BACK, pygame_events
	global UP_BT, DOWN_BT, LEFT_BT, RIGHT_BT, NEXT_BT, BACK_BT
	is_pressed = False				# this variable will be set True when asked button is pressed. Otherwise it won't change

	if gl.os_is_linux:		# for the raspberry pi
		keys = [(UP, UP_BT), (DOWN, DOWN_BT), (LEFT, LEFT_BT), (RIGHT, RIGHT_BT), 
				(NEXT, NEXT_BT), (BACK, BACK_BT)]		# list of possible inputs and matching button objects
		for key in keys:								# loop through and check if button has been pressed
			if input == key[0]:
				is_pressed = not key[1].is_pressed		# invert reading, because pins are pulldown?

	else:			# for windows / developing
		# keyboard input
		for event in pygame_events:
			if event.type == pygame.KEYDOWN:
				keys = [(UP, pygame.K_UP), (DOWN, pygame.K_DOWN), (LEFT, pygame.K_LEFT), (RIGHT, pygame.K_RIGHT), 
						(NEXT, pygame.K_RETURN), (BACK, pygame.K_DELETE)]		# list of possible inputs and matching keys on keyboard
				for key in keys:					# loop through and check if key has been pressed
					if input == key[0] and event.key == key[1]:
						is_pressed = True
	
	return is_pressed

""" ### ### output ### ### """
if not gl.os_is_linux:
	import serial
	PORT, BAUD = "COM4", 9600		# NOTE settings for serial comm.
	ser = serial.Serial(PORT, BAUD)

VALVES = [11, 0, 26, 19, 27, 22, 10]			# NOTE Valves: set corresponding pins here ([0] is the valve for water, then going from left to right)
PUMP = 9	
if gl.os_is_linux:									# 		 Pump: set gpio pin for pump here
	VALVES_OUT = [LED(VALVES[0]), LED(VALVES[1]), LED(VALVES[2]), LED(VALVES[3]), LED(VALVES[4]), LED(VALVES[5]), LED(VALVES[6])]
	PUMP_OUT = LED(PUMP)
valves_state = [False, False, False, False, False, False, False]			# states of the pins
pump_state = False

def writeOutput(out, state):
	""" set output
	out: pin to set [VALVES[0:7], PUMP] or any other gpio pin
	state: state [True / 1, False / 0]
	"""
	global HIGH, LOW, VALVES, PUMP, valves_state, pump_state
	global VALVES_OUT, PUMP_OUT

	if gl.os_is_linux:			# for the raspberry pi
		keys = [(VALVES[0], VALVES_OUT[0]), (VALVES[1], VALVES_OUT[1]), (VALVES[2], VALVES_OUT[2]),
				(VALVES[3], VALVES_OUT[3]), (VALVES[4], VALVES_OUT[4]), (VALVES[5], VALVES_OUT[5]),
				(VALVES[6], VALVES_OUT[6]), (PUMP, PUMP_OUT)]		# list of possible outputs and matching led objects
		for key in keys:
			if key[0] == out:
				if state:
					key[1].on()
				else:
					key[1].off()

	else:						# for the windows machine
		text = ""		# text to send to arduino. the text should contain two digits, the first one for the valve (0-7) or pump (8).
						# The second is the state (1 = on, 0 = off).
		# set valve / output
		for idx, valve in enumerate(VALVES):
			if out == valve:
				text = str(idx)
		if out == PUMP:
			text = "7"
		text += str(int(state)) + '\n'		# add state and newline carrier
		ser.write(text.encode('utf-8'))		# send text
	
	# keep the saved states up-to-date
	for idx, valve in enumerate(VALVES):
		if out == valve:
			valves_state[idx] = state
	if out == PUMP:
		pump_state = state