""" test.py
PLACEHOLDER for testing
"""

import video_class, pygame
pygame.init()

test_vid = video_class.video("/lib/test/")

print(test_vid.frames)
print(test_vid.audio)
