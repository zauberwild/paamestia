"""
contains class for videos
"""

import os, pathlib, pygame, pygame.mixer
gen_path = str(pathlib.Path(__file__).parent.absolute())

class Animation:
	"""
	this class handles the sprites/spritesheets folders and makes videos out of these.
	"""

	def __init__(self, folder_path):
		""" vieo class. uses sprites do display a video
		- video_path: path to media folder
		"""
		self.path = gen_path + folder_path
		# Images
		self.img_path = []								# save all paths to the image files
		for filename in os.listdir(self.path):
			if filename != "forwards.wav" and filename != "backwards.wav":
				self.img_path.append(self.path + filename)
		self.img_path.sort()		# make sure they are in the right order
		self.img = []				# will hold the pygame.Surface objects as soon they will be loaded
		self.n_frames = 0			# number of frames. is updated with every change on self.img[]
		# Audio
		self.audio_forwards_path = self.path + "forwards.wav"
		self.audio_backwards_path = self.path + "backwards.wav"
		self.audio_forwards = None		# holds pygame.mixer.Sound object,
		self.audio_backwards = None			# assuming correspoding audio files could be found
		if os.path.isfile(self.audio_forwards_path):		# test if audio files are there
			self.audio_forwards = pygame.mixer.Sound(self.audio_backwards_path)		# create object  with audio-file
		if os.path.isfile(self.audio_backwards_path):
			self.audio_backwards = pygame.mixer.Sound(self.audio_backwards_path)
		# States / params
		self.loaded =  False		# frames loaded
		self.play = False			# video plays
		self.interrupt = False		# video is paused
		self.frame = 0				# durrent frame
		self.forwards = True		# video is played forwards
		self.repeat = False			# video plays on repeat
		self.audio_mute = False		# video on mute

	def load(self):
		""" loads the frames as pygame.Surface. please use sparingly to keep RAM clear
		"""
		if not self.loaded:
			for i in self.img_path:
				self.img.append(pygame.image.load(i))
			self.n_frames = len(self.img)
			self.loaded = True
		

	def unload(self):
		""" unloads the n_frames. use it to clear up ram
		"""
		self.img.clear()
		self.n_frames = len(self.img)
		self.loaded = False

	def start(self,audio=True, forwards=True, repeat=False):
		"""	start video from the beginning
		- audio=True: set False to mute
		- forwards=True: set False, if you want play it backwards
		- repeat=False: set True, to endlessly repeat the video
			(can be stopped with stop())
		"""
		if self.n_frames == 0:		# interrupt when images are not loaded
			return

		self.play = True			# start video
		self.forwards = forwards	# set params
		self.repeat = repeat
		self.audio_mute = not audio
		
		if forwards:				# set start frame and start audio (when exiting and not muted)
			self.frame = 0
			if self.audio_forwards != None and audio:
				self.__start_audio__()
		else:
			self.frame = self.n_frames - 1
			if self.audio_backwards != None and audio:
				self.__start_audio__(forwards=False)
	
	def __start_audio__(self, forwards=True):
		""" play the audio files (internal use only)
		- forwards=True: True: play forwards.wav / False: play backwards.wav
		"""
		if forwards:				# start audio (if exiting)
			if self.audio_forwards != None:
				pygame.mixer.Sound.play(self.audio_forwards)
		else:
			if self.audio_backwards != None:
				pygame.mixer.Sound.play(self.audio_backwards)

	def pause(self):
		""" interrupt / unpause the video
		"""
		self.interrupt = not self.interrupt
	
	def stop(self):
		""" stop the video
		"""
		self.play = False

	def draw(self, local_screen):
		""" draws the video
		"""
		if self.play:		# when video plays
			local_screen.blit(self.img[self.frame], (0, 0))		# draw current frame
			
			if not self.interrupt:		# when not paused
				if self.forwards:		
					self.frame += 1								# advance frame
					if self.frame >= self.n_frames:				# if at the end
						if self.repeat:							# if repeat on
							if not self.audio_mute:
								self.frame = 0						# start over
							self.__start_audio__()
						else:
							self.play = False					# stop
				else:
					self.frame -= 1								# advance frame
					if self.frame < 0:							# if at the end
						if self.repeat:							# if repeat on
							self.frame = self.n_frames - 1		# start over
							if not self.audio_mute:
								self.__start_audio__(forwards=False)
						else:
							self.play = False					# stop
	


