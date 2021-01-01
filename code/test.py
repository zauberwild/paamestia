""" test.py
PLACEHOLDER for testing
"""

import medialib
import pygame
pygame.init()

FPS = 24

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("test")
clock = pygame.time.Clock()

screen.fill((0,0,255))
pygame.display.flip()

test_vid = medialib.Animation("/src/test/")

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
				test_vid.start(audio=False)
			if event.key == pygame.K_2:
				test_vid.start(forwards=False, audio=False)
				print("### playing reverse")
			if event.key == pygame.K_3:
				test_vid.load()
				print("### Loading done")
			if event.key == pygame.K_4:
				test_vid.unload()
				print("### cleared!")
			if event.key == pygame.K_5:
				test_vid.pause()
				print("### pause/play")
			if event.key == pygame.K_6:
				test_vid.stop()
				print("### stopped!")
	
	screen.fill((127,127,127))

	test_vid.draw(screen)

	pygame.display.flip()
	
	clock.tick(FPS)