"""
contains class for videos
"""

import os, pathlib, pygame, pygame.mixer
gen_path = str(pathlib.Path(__file__).parent.absolute())

class video:
	"""
	this class handles the sprites/spritesheets folders and makes videos out of these.
	"""

	def __init__(self, folder_path):
		""" vieo class. uses sprites do display a video
		- video_path: path to folder
		"""
		self.path = gen_path + folder_path

		self.img_path = []
		for filename in os.listdir(self.path):
			if filename != "forwards.wav" and filename != "backwards.wav":
				self.img_path.append(self.path + filename)
		self.img_path.sort()
		self.img = []
		self.n_frames = len(self.img_path)

		self.audio_forwards_path = self.path + "forwards.wav"
		self.audio_backwards_path = self.path + "backwards.wav"
		self.audio_forwards = pygame.mixer.Sound(self.audio_backwards_path)
		self.audio_backwards = pygame.mixer.Sound(self.audio_backwards_path)
		self.play = False
		self.frame = 0
		self.forwards = True
		self.repeat = False
	
	def load(self):
		""" loads the frames as pygame.surface. please use sparingly
		"""
		for i in range(self.n_frames):
			path = self.path

	def start(self, forwards=True, repeat=False):
		"""	start video 
		- forwards=True: set False, if you want play it backwards
		- repeat=False: set True, to endlessly repeat the video
			(can be stopped with stop())
		"""
		self.play = True
		self.forwards = forwards
		self.repeat = repeat
		if forwards:
			self.cur_frame = 0
			pygame.mixer.Sound.play(self.audio_forward)
		else:
			self.cur_frame = self.frames - 1
			pygame.mixer.Sound.play(self.audio_backwards)

		print("now playing, forwards=" + str(self.forwards) + ", repeat=" + str(self.repeat))

	def pause(self):
		""" pause / unpause the video
		"""
		self.play != self.play
	
	def stop(self):
		""" stop the video
		"""
		self.play = False

	def draw(self, local_screen):
		""" draws the video
		"""
		if self.play:
			local_screen.blit(self.img[self.cur_frame], (0, 0))
			
			if self.forwards:
				self.cur_frame += 1
				if self.cur_frame >= self.frames:
					if self.repeat:
						self.cur_frame = 0
					else:
						self.play = False
						print("stopped playing")
			else:
				self.cur_frame -= 1
				if self.cur_frame < 0:
					if self.repeat:
						self.cur_frame = self.frames - 1
					else:
						self.play = False
						print("stopped playing")			
	


