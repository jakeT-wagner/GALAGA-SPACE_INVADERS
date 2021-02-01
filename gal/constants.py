import pygame

WIDTH, HEIGHT = 500,750

#rgb colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (0, 255, 255)

COLORS = [RED, GREEN, BLUE, WHITE, YELLOW]

BLACK = (0, 0, 0)

#images used from the following
#<div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#BLPAWN = pygame.transform.scale(pygame.image.load('assets/new_bl_pawn.png'), (42,58))
FIGHTER = pygame.transform.scale(pygame.image.load('assets/fighter.png'), (40,60))