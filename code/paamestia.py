"""
paamestia

"""

# imports
from globals import *
import ext_ui_methods_lib as ui

# pygame stuff
import pygame
import pygame.freetype
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.init()
pygame.freetype.init()
debug_font = pygame.freetype.Font(gen_path + "/src/fonts/CamingoCode-Regular.ttf", 30)

# DEL fill screen, can be deleted, when project done
screen.fill((127,127,127))
pygame.display.flip()

# objects creation


""" ### ### main loop ### ### """
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

	# run external methods according to prog_pos
	if prog_pos == 'i':					# intro
		ui.intro()

	elif prog_pos == 'm':				# main menu
		ui.main_menu()

	elif prog_pos[0] == 'f':			# free mixing
		if prog_pos[1] == 't':				# transition
			ui.free_transition()
		elif prog_pos[1] == 'c':			# mix cocktail
			ui.free_choose()
		elif prog_pos[1] == 'o':			# output
			ui.free_output()

	elif prog_pos[0] == 'r':			# recipe
		if prog_pos[1] == 't':				# transition
			ui.recipe_transition()
		elif prog_pos[1] == 'c':			# choose recipe / cocktail
			ui.recipe_choose()
		elif prog_pos[1] == 'o':			# output
			ui.recipe_output()

	elif prog_pos[0] == 's':			# settings
		ui.settings()

	else:
		text = ["ERROR", "invalid prog_pos: " + str(prog_pos), "reseting to 'm'"]
		screen.fill((0,0,0))
		h = 0
		for t in text:
			debug_font.render_to(screen, (0,h), t, (255,0,0))
			h += 32
		prog_pos = 'm'


	# debug
	if show_debug:
		fps = str(clock.get_fps())
		debug_main_loop = ["FPS: " + fps[0:6], "prog_pos: " + prog_pos]
		h = 3
		for t in debug_main_loop + debug_text:
			textsur, rect = debug_font.render(t, (0, 255, 0))
			pygame.draw.rect(screen, (0,0,0), (0,H - rect.height - h,rect.width,rect.height))
			screen.blit(textsur, (0,H - rect.height - h))
			h += rect.height + 3
		debug_text.clear()

	pygame.display.flip()	# refresh window and show content
	clock.tick(FPS)			# limit fps