""" test.py
PLACEHOLDER for testing
"""

import media_lib
import pygame
from globals import *
pygame.init()
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.font.init()
myfont = pygame.font.SysFont('Calibri', 30)

FPS = 24

screen = None
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("test")
clock = pygame.time.Clock()

screen.fill((0,0,255))
pygame.display.flip()

test_anim = media_lib.Animation("/src/test_klein/")

vid_files = "/src/intro_7.mp4"
test_vid = media_lib.Video(vid_files, "/src/test/forwards.wav")

bar = media_lib.Image("/src/prop_red.png", 0, 300, 800, 300, direct_load=True)

prog_active = True
while prog_active:
	# input
	for event in pygame.event.get():
    	# closing the window
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			prog_active = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				print("### playing")
				test_anim.start(audio=False)
			if event.key == pygame.K_2:
				test_anim.start(forwards=False, audio = False)
				print("### playing reverse")
			if event.key == pygame.K_3:
				test_anim.load()
				print("### Loading done")
			if event.key == pygame.K_4:
				test_anim.unload()
				print("### cleared!")
			if event.key == pygame.K_5:
				test_anim.pause()
				print("### pause/play")
			if event.key == pygame.K_6:
				test_anim.stop()
				print("### stopped!")
			if event.key == pygame.K_7:
				test_vid.start()
				print("### Video start")
			if event.key == pygame.K_8:
				test_vid.stop()
				print("### Video stopped!")
	
	if not test_anim.play and not test_vid.play:
		screen.fill((127,127,127))

	test_anim.draw()

	test_vid.draw()

	bar.draw()

	fps = str(clock.get_fps())
	textsur = myfont.render(fps[0:6], False, (0,255,0))
	screen.blit(textsur, (0,0))

	pygame.display.flip()

	#print(clock.get_fps())
	
	clock.tick(FPS)