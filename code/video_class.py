"""
video_class.py

contains class for videos
"""

import os, pathlib, pygame
gen_path = str(pathlib.Path(__file__).parent.absolute())

class video:
	"""
	this class handles the sprites/spritesheets folders and makes videos out of these.
	It is also possible to give a list of folder-paths, in this case the video will be
	chosen randomly.
	"""

	def __init__(self, video_path,surfix,digits,prefix):
		""" vieo class. uses sprites do display a video
		- video_path: path to folder
		- surfix: file-surfix (e.g. frames-)
		- prefix: file-prefix (e.g. .png)
		"""
		self.path = gen_path + video_path
		self.surfix = surfix
		self.digits = digits
		self.prefix = prefix
		self.img = []
		
		for i, filename in enumerate(os.listdir(self.path)):
			index = getFrameIndex(self.digits,i+1)
			print(self.path + self.surfix + index + self.prefix)
			self.img.append(pygame.image.load(self.path + self.surfix + index + self.prefix))
		
		self.play = False
	
	def testFeedback(self):
		pass

	def start(self, forwards=True):
		"""	start video 
		- forwards=True: set False, if you want play it backwards
		"""
		pass

	def pause(self):
		""" pause / unpause the video
		"""
		pass

	def draw(self):
		""" draws the video
		"""
		pass

def getFrameIndex(digits, index):
	""" return string of index with trailing zeros
	- digits: number of digits
	- index: number to return
	"""
	index_str = str(index)
	len_of_index = len(str(index))

	out = ""
	for i in range(digits - len_of_index):
		out += "0"
	
	out += str(index)

	return out
	


