""" test.py
PLACEHOLDER for testing
"""

import medialib, pygame
pygame.init()

test_vid = medialib.video("/lib/test/")

print(test_vid.frames)
print(test_vid.audio)
