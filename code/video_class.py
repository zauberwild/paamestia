"""
video_class.py

contains class for videos
"""

class video:
	"""
	this class handles the sprites/spritesheets folders and makes videos out of these.
	It is also possible to give a list of folder-paths, in this case the video will be
	chosen randomly.
	"""

	def __init__(self, video_path):
		""" vieo class. uses sprites do display a video
		- video_path: path to folder
		"""
		self.path = video_path
		self.img = []
		self.play = False

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

	


