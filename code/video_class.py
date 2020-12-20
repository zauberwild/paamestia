"""
video_class.py

contains class for videos
"""

import os, pathlib
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
		
		i = 1
		for filename in os.listdir(self.path):
			index = getFrameIndex(self.digits,self.index)
			img.append = pygame.image.load(self.path + self.surfix + self.index + self.prefix)

			i += 1

		self.play = False
	
	def testFeedback(self):
		print(self.path)
		print(self.path + self.surfix + "00001" + self.prefix)

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
	len_of_index = index_str.length()

	out = ""
	for i in range(digits - len_of_index):
		out += "0"
	
	out += index

	return out
	


