""" test.py
PLACEHOLDER for testing
"""

from os import P_OVERLAY
import medialib
import pygame
pygame.init()

FPS = 24

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("test")
clock = pygame.time.Clock()

screen.fill((0,0,255))
pygame.display.flip()

test_vid = medialib.video("/src/test/")

video_list = []
for i in range(15):
	video_list.append(medialib.video("/src/test/"))

print("Video loaded!")

prog_active = True
while prog_active:
	# input
	for event in pygame.event.get():
    	# closing the window
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			prog_active = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				test_vid.start()
			if event.key == pygame.K_2:
				test_vid.start(False)
	
	screen.fill((127,127,127))

	test_vid.draw(screen)

	pygame.display.flip()
	
	clock.tick(FPS)