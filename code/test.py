""" test.py
PLACEHOLDER for testing
"""

import media_lib
import pygame
pygame.init()

FPS = 24

screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("test")
clock = pygame.time.Clock()

screen.fill((0,0,255))
pygame.display.flip()

test_anim = media_lib.Animation("/src/test/")

vid_files = ["/src/color.mov", "/dummy.mk4", "/src/jump.mov", "/src/movie.mp4n", "/dummy.mpg"]
vid_lengths = [1, 42, 2, 442, 69]
test_vid = media_lib.Video(vid_files, vid_lengths)

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
				test_anim.start(forwards=False)
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
				print("### VLC start")
			if event.key == pygame.K_8:
				test_vid.kill
				print("### VLC killed!")
	
	screen.fill((127,127,127))

	test_anim.draw(screen)

	pygame.display.flip()
	
	clock.tick(FPS)