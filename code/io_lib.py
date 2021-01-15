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

	for event in pygame_events:
			# closing window / exit program
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
				gl.prog_active = False
			if event.type == pygame.KEYDOWN:
				# debug information
				if event.key == pygame.K_d:
					gl.show_debug = not gl.show_debug

""" ### ### button input ### ### """
UP, DOWN, LEFT, RIGHT, NEXT, BACK = 0, 1, 2, 3, 4, 5		# NOTE Buttons: set corresponding pins here
def readInput(input):
	""" read signal from input. returns bool
	input: chosen input [UP, DOWN, LEFT, RIGHT, NEXT, BACK] or any other gpio pin
	"""
	global UP, DOWN, LEFT, RIGHT, NEXT, BACK, pygame_events
	ret = False				# this variable will be set True when asked button is pressed. Otherwise it won't change

	if gl.os_is_linux:		# for the raspberry pi
		button = Button(input)
		if button.is_pressed:
			ret = True
	else:			# for the windows machine
		# keyboard input
		for event in pygame_events:
			if event.type == pygame.KEYDOWN:
				keys = [(UP, pygame.K_UP), (DOWN, pygame.K_DOWN), (LEFT, pygame.K_LEFT), (RIGHT, pygame.K_RIGHT), (NEXT, pygame.K_RETURN), (BACK, pygame.K_DELETE)]		# list of possible inputs and matching keys on keyboard
				for key in keys:					# loop through and check if key has been pressed
					if input == key[0] and event.key == key[1]:
						ret = True
	
	return ret

""" ### ### output ### ### """
if gl.os_is_linux:
	from gpiozero import Button, LED
else:
	import serial
	PORT, BAUD = "COM4", 9600		# settings for serial comm.
	ser = serial.Serial(PORT, BAUD)

HIGH, LOW = 1, 0
VALVES = [0, 1, 2, 3, 42, 5, 69]			# NOTE Valves: set corresponding pins here ([0] being valve for water, then going from left to right)
PUMP = 420									# NOTE Pump: set gpio pin for pump here
valves_state = [False, False, False, False, False, False, False]			# states of the pins
pump_state = False

def writeOutput(out, state):
	""" set output
	out: pin to set [VALVES[0:7], PUMP] or any other gpio pin
	state: state [HIGH / True / 1, LOW / False / 0]
	"""
	global HIGH, LOW, VALVES, PUMP, valves_state, pump_state

	if gl.os_is_linux:			# for the raspberry pi
		led = LED(out)
		if state:
			led.on()
		else:
			led.off()
	else:						# for the windows machine
		text = ""		# text to send to arduino. the text should contain two digits, the first one for the valve (0-7) or pump (8).
						# THe second is the state (1 = on, 0 = off).

		# set valve
		for idx, valve in enumerate(VALVES):
			if out == valve:
				text = str(idx)
		if out == PUMP:
			text = "7"
		text += str(int(state)) + '\n'		# set state
		ser.write(text.encode('utf-8'))
	
	# refresh the states
	for idx, valve in enumerate(VALVES):
		if out == valve:
			valves_state[idx] = state
	if out == PUMP:
		pump_state = state