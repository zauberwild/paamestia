"""
contains class for videos
"""

import os, pathlib, pygame	
gen_path = str(pathlib.Path(__file__).parent.absolute())

class video:
	"""
	this class handles the sprites/spritesheets folders and makes videos out of these.
	"""

	def __init__(self, video_path):
		""" vieo class. uses sprites do display a video
		- video_path: path to folder
		"""
		self.path = gen_path + video_path
		self.img = []
		self.audio_path = ""
		
		for filename in os.listdir(self.path):
			if ".wav" in filename:					# filters the audio file out
				self.audio_path = self.path + filename
			else:
				self.img.append(pygame.image.load(self.path + filename))
		
		self.audio = pygame.mixer.Sound(self.audio_path)

		self.frames = len(self.img)

		self.play = False
		self.cur_frame = 0
		self.forwards = True
		self.repeat = False

	def start(self, forwards=True, repeat=False):
		"""	start video 
		- forwards=True: set False, if you want play it backwards
		"""
		self.play = True
		self.forwards = forwards
		self.repeat = repeat
		if forwards:
			self.cur_frame = 0
		else:
			self.cur_frame = self.frames - 1

		pygame.mixer.Sound.play(self.audio)

		print("now playing, forwards=" + str(self.forwards) + ", repeat=" + str(self.repeat))

	def pause(self):
		""" pause / unpause the video
		"""
		self.play != self.play

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
	


