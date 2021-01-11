"""
this file stores all global variables and constants
"""

from pathlib import Path								# used to get the complete path of the working directory
gen_path = str(Path(__file__).parent.absolute())		# get the complete path of the "code"-directory
from os import path											# used to get the complete path of the working directory
os_is_linux = not path.isfile(gen_path + "/src/.windows")		# look for a ".windows" file, which only exists on my Windows-PC

FPS = 24				# frames per second
W, H = 800, 600			# width and height of the window

prog_pos = "i"			# saves current position in program flow