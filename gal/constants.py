import pygame

WIDTH, HEIGHT = 500,750

#rgb colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

COLORS = [GREEN, BLUE, WHITE, YELLOW]

BLACK = (0, 0, 0)

#Laser dimensions
LSRWIDTH = 4
LSRLENGTH = 20
LSRSPEED = 30

#images used from the following
#<div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#https://galaga.fandom.com/wiki/Goei
#https://commons.wikimedia.org/wiki/File:Explosion-155624_icon.svg
FIGHTER = pygame.transform.scale(pygame.image.load('assets/fighter.png'), (40,60))
REDBUG = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('assets/redbug.png'), (22,32)), 90.0)
EXPLOSION = pygame.transform.scale(pygame.image.load('assets/Explosion.svg'), (25,35))
