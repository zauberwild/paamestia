""" test.py
PLACEHOLDER for testing
"""

import drinks_lib as drinks
import pygame
import pygame.freetype
import globals as gl

drinks.spot[5].drink = "Alter Janx-Geist"
drinks.spot[4].drink = "arkturanischer Mega-Gin"
drinks.spot[6].drink = "fallianisches Sumpfgas"
drinks.spot[2].drink = "qualaktinischen Hyperminz-Extrakt"
drinks.spot[1].drink = "Zamphuor"
drinks.spot[3].drink = "KiBa"

pangal = drinks.Recipe(gl.gen_path + "/src/recipes/Pangalaktischer_Donnergurgler")