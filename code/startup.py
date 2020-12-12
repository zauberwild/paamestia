"""
startup.py

this script allows to stop the normal startup routine, so you can use
the normal desktop
"""

"""ISSUE REPLACEABLE? / WORKAROUND? """

import pygame
pygame.init()

print("paamestia is starting...")

normal_startup = True

# TODO startup routine; ask if normal startup should be continued or cancelled

if normal_startup:
	#python ./paamestia.py
	#exec(open("./paamestia.py").read())
