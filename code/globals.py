from pathlib import Path								# used to get the complete path of the working directory
gen_path = str(Path(__file__).parent.absolute())		# get the complete path of the "code"-directory
from os import path											# used to get the complete path of the working directory
os_is_linux = not path.isfile(gen_path + "/src/.windows")		# look for a ".windows" file, which only exists on my Windows-PC