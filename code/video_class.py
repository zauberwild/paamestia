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

	def __init__(self):
		play = False

	def play(self, forwards=True):
		"""	start video 
		!! will start video from beginning. please use pause() to unpause
		- forwards=True: set False, if you want play backwards
		"""