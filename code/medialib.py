"""
video_class.py

contains class for videos
"""

import os, pathlib, pygame		#ISSUE [i1] how to handle pygame/drawing the video? (REF at Varroa Invaders)	
gen_path = str(pathlib.Path(__file__).parent.absolute())

class video:
	"""
	this class handles the sprites/spritesheets folders and makes videos out of these.
	It is also possible to give a list of folder-paths, in this case the video will be
	chosen randomly.
	ISSUE Won't be included, if not specifcally needed
	"""

	def __init__(self, video_path):
		""" vieo class. uses sprites do display a video
		- video_path: path to folder
		"""
		self.path = gen_path + video_path
		self.img = []
		self.audio = ""
		
		for filename in os.listdir(self.path):
			if ".wav" in filename:					# filters the audio file out
				self.audio = self.path + filename
			else:
				#print(self.path + filename)											#DEL
				self.img.append(pygame.image.load(self.path + filename))
		
		self.frames = len(self.img)
		self.play = False

	def start(self, forwards=True):
		"""	start video 
		- forwards=True: set False, if you want play it backwards
		"""
		pass

	def pause(self):
		""" pause / unpause the video
		ISSUE is it neccesarry?
		"""
		pass

	def draw(self):
		""" draws the video
		"""
		pass
	


