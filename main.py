import pygame
import time
from gal.constants import WIDTH, HEIGHT
from gal.background import Background
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Galaga')

#def get_row_col_from_mouse(pos):
#    x,y = pos
#    row = y // SQUARE_SIZE
#    col = x // SQUARE_SIZE
#    return row, col

def main():
    backg = Background(WIN)
    running = True
    clock = pygame.time.Clock()
    
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                #row,col = get_row_col_from_mouse(pos)
                #game.select(row,col)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    backg.shoot()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            backg.move_(-12)
        elif pressed[pygame.K_RIGHT]:
            backg.move_(12)
        else: 
            backg.move_(0)
        backg.update()

    pygame.quit()
main()
