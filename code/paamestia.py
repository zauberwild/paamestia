"""
paamestia

"""

# imports
import globals as gl
import ext_ui_methods_lib as ui
import io_lib

# pygame stuff
import pygame
import pygame.freetype
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.init()
pygame.freetype.init()
debug_font = pygame.freetype.Font(gl.gen_path + "/src/fonts/CamingoCode-Regular.ttf", 24)

# DEL fill screen, can be deleted, when project done
gl.screen.fill((0,0,127))
pygame.display.flip()

# objects creation


""" ### ### main loop ### ### """
while gl.prog_active:
	# keyboard input
	io_lib.keyboard_input()

	# run external methods according to prog_pos
	if gl.prog_pos == 'i':					# intro
		ui.intro()

	elif gl.prog_pos == 'm':				# main menu
		ui.main_menu()

	elif gl.prog_pos[0] == 'f':			# free mixing
		if gl.prog_pos[1] == 't':				# transition
			ui.free_transition()
		elif gl.prog_pos[1] == 'c':			# mix cocktail
			ui.free_choose()
		elif gl.prog_pos[1] == 'o':			# output
			ui.free_output()

	elif gl.prog_pos[0] == 'r':			# recipe
		if gl.prog_pos[1] == 't':				# transition
			ui.recipe_transition()
		elif gl.prog_pos[1] == 'c':			# choose recipe / cocktail
			ui.recipe_choose()
		elif gl.prog_pos[1] == 'o':			# output
			ui.recipe_output()

	elif gl.prog_pos[0] == 's':			# settings
		ui.settings()

	else:
		text = ["ERROR", "invalid prog_pos: " + str(gl.prog_pos), "resetting to 'm'"]
		gl.screen.fill((0,0,0))
		h = 0
		for t in text:
			print(t)
			debug_font.render_to(gl.screen, (0,h), t, (255,0,0))
			h += 32
		prog_pos = 'm'


	# debug
	if gl.show_debug:
		fps = str(gl.clock.get_fps())
		debug_main_loop = ["FPS: " + fps[0:6], "prog_pos: " + gl.prog_pos]
		h = 3
		for t in debug_main_loop + gl.debug_text:
			textsur, rect = debug_font.render(t, (0, 255, 0))
			pygame.draw.rect(gl.screen, (0,0,0), (0,gl.H - rect.height - h,rect.width,rect.height))
			gl.screen.blit(textsur, (0,gl.H - rect.height - h))
			h += rect.height + 3
		gl.debug_text.clear()

	pygame.display.flip()	# refresh window and show content
	gl.clock.tick(gl.FPS)			# limit fps

pygame.quit()