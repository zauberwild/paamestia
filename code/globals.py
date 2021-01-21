"""
this file stores all global variables and constants
"""

from pathlib import Path								# used to get the complete path of the working directory
gen_path = str(Path(__file__).parent.absolute())		# get the complete path of the "code"-directory
from os import path											# used to get the complete path of the working directory
os_is_linux = not path.isfile(gen_path + "/src/.windows")		# looks for a ".windows" file, which only exists on my Windows-PC
import pygame

prog_active = True		# set to False to end program

FPS = 24				# frames per second
W, H = 800, 600			# width and height of the window

prog_pos = 'i'			# saves current position in program flow

show_debug = True		# show debugging information (fps,...)
debug_text = []			# debug list with all parameters to show. append parameters to this list every loop

debug_font = pygame.freetype.Font(gen_path + "/src/fonts/CamingoCode-Regular.ttf", 24)		# debug font
debug_font_big = pygame.freetype.Font(gen_path + "/src/fonts/CamingoCode-Regular.ttf", 48)		# debug font, but bigger

# setting the window up
import pygame
screen = None
if os_is_linux:
	screen = pygame.display.set_mode((W,H), pygame.FULLSCREEN)
else:
	screen = pygame.display.set_mode((W,H))

pygame.display.set_caption("paamestia_main")
clock = pygame.time.Clock()