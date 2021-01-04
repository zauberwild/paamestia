"""
contains class for animations and videos
"""

import os							# used to scan for files execute commands from a commandline
from random import randint			# random function to get random list index in video class
import pygame, pygame.mixer			# used in Ainmation-Class for displaying sprites and playing audio files
import cv2 
import numpy as np 
from globals import *

class Animation:
	"""
	this class handles the sprites/spritesheets folders and makes videos out of these.
	"""

	def __init__(self, folder_path):
		""" animation class. uses sprites do display a video
		- video_path: path to media folder
		"""
		self.path = gen_path + folder_path
		self.w, self.h = pygame.display.get_surface().get_size()
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
				self.img.append(pygame.transform.scale(pygame.image.load(i), (self.w, self.h)))
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
				self._start_audio()
		else:
			self.frame = self.n_frames - 1
			if self.audio_backwards != None and audio:
				self._start_audio(forwards=False)
	
	def _start_audio(self, forwards=True):
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
							if not self.audio_mute:					# start over
								self._start_audio()
							self.frame = 0	
						else:
							self.play = False					# stop
				else:
					self.frame -= 1								# advance frame
					if self.frame < 0:							# if at the end
						if self.repeat:							# if repeat on
							self.frame = self.n_frames - 1		# start over
							if not self.audio_mute:
								self._start_audio(forwards=False)
						else:
							self.play = False					# stop

class Video:
	""" 
	uses opencv to play videos
	"""

	def __init__(self, files):
		""" video class. uses opencv to display a video
		- files: list of file paths. by pressing play, one will be chosen randomly
		"""
		self.files = files
		for i in range(len(self.files)):		# add the directory path to the file names
			self.files[i] = gen_path + self.files[i]
		
		delete = []								# test if every file can be found
		for i in range(len(self.files)):
			if not os.path.isfile(self.files[i]):
				delete.append(i)				# if not found, save index, to delete late
		delete.sort(reverse=True)				# sort the list to decreasing values, so the missing indexes won't affect other indexes that need to be deleted
		for i in delete:						# delete all files that couldn't be found
			del self.files[i]


		self.cap = None			# holds the CideoCapture-object for playing the file
		
		# stats / params
		self.play = False
		self.chosen_file = 0
		self.repeat = False
		self.frames = 0
		self.frame_counter = 0

		def start(self, repeat=False):
			""" starts the video
			- repeat=False: set True, to play repeatedly
			"""
			self.play = True
			self.chosen_file = randint(0,len(self.files)-1)		# choose a random fil
			self.cap = cv2.VideoCapture(path + "/intro.mp4")
			self.frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
			self.frame_counter = 0

		def stop(self):
			""" stop the video
			"""
			self.play = False
		
		def draw(self, screen):
			""" draw the video
			- screen: the pygame screen object
			"""
			ret, frame = self.cap.read()
			self.frame_counter += 1

			if(self.frame_counter == self.frames):
				frame_counter = 0
				self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
			
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			frame = frame.swapaxes(0, 1)
			pygame.surfarray.blit_array(screen, frame)




# global variables for video-class:
vlc_start_linux = "cvlc -f --no-video-title-show --play-and-exit --no-loop <path> &"			# command lines for vlc on various platforms
vlc_kill_linux = "killall vlc"																	# <path> will be replaced with a path
vlc_start_windows = "vlc -f --no-video-title-show --play-and-exit --no-loop <path>"
vlc_kill_windows = "TASKKILL /IM VLC.EXE"


class VLCVideo:
	"""
	this class can play videos with VLC Media Player by starting it from the command line
	"""

	def __init__(self, files, length):
		""" video class. starts vlc via commandline
		- files: list with all video files. if given multiple files, one will be chosen at random
		- length: according list with the length of the videos in seconds
		"""
		self.files = files
		self.length = length

		for i in range(len(self.files)):		# add the directory path to the file names
			self.files[i] = gen_path + self.files[i]

		delete = []								# test if every file can be found
		for i in range(len(self.files)):
			if not os.path.isfile(self.files[i]):
				delete.append(i)
		delete.sort(reverse=True)				# sort the list to decreasing values, so the missing indexes won't affect other indexes that need to be deleted
		for i in delete:						# delete all files that couldn't be found
			del self.files[i]
			del self.length[i]
		
		# stats / params
		self.play = False
		self.chosen_file = 0
		self.t_start = 0
	
	def start(self):
		""" start the video
		"""
		commandline = ""		# prepare the commandline
		if os_is_linux:
			commandline = vlc_start_linux
		else:
			commandline = vlc_start_windows
		self.chosen_file = randint(0,len(self.files)-1)		# choose a random file
		commandline = commandline.replace("<path>", str(self.files[self.chosen_file]))
		os.system(commandline)

	def kill(self):
		""" kill VLC process. might kill all running VLC-processes
		"""
		commandline = ""
		if os_is_linux:
			commandline = vlc_kill_linux
		else:
			commandline = vlc_kill_windows
		os.system(commandline)
