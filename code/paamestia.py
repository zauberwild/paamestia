"""
paamestia

"""

# imports 
import media_lib
from globals import *

# pygame stuff
import pygame
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.init()
pygame.font.init()
debug_font = pygame.font.SysFont('Consolas', 30)

# setting the window up
screen = None
if os_is_linux:
	screen = pygame.display.set_mode((W,H), pygame.FULLSCREEN)
else:
	screen = pygame.display.set_mode((W,H))

pygame.display.set_caption("paamestia_main")
clock = pygame.time.Clock()

# objects creation


# ### ### main loop
show_debug = False
prog_active = True
while prog_active:
	# keyboard input
	for event in pygame.event.get():
		# closing window / exit program
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			prog_active = False
		if event.type == pygame.KEYDOWN:
			# debug information
			if event.key == pygame.K_d:
				show_debug = not show_debug

	
	# push button input


	# logic


	# draw
	screen.fill((127,127,127))


	# debug, flip and fps
	if show_debug:
		fps = str(clock.get_fps())
		textsur = debug_font.render(fps[0:6], False, (0,255,0))
		screen.blit(textsur, (0,H-30))

	pygame.display.flip()
	clock.tick(FPS)