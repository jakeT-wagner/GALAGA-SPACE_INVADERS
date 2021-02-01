import pygame
import random
from .constants import WIDTH, HEIGHT, COLORS, BLACK, FIGHTER
from .piece import Piece

class Background:
    def __init__(self, win):
        self.win = win
        self.space = []
        self.pieces = []
        self.initial_backg()
        self.display_backg()

    def initial_backg(self):
        for row in range(WIDTH):
            self.space.append([])
            for col in range(HEIGHT):
                rand = random.uniform(0, 1)
                if (rand > 0.98):
                    color = random.choice(COLORS)
                    self.space[row].append(color)
                else:
                    self.space[row].append(0)
        self.add_piece(FIGHTER)
    
    def add_piece(self, image):
        self.pieces.append(Piece(image))

    def display_backg(self):
        self.win.fill(BLACK)
        for row in range(WIDTH):
            for col in range(HEIGHT):
                if self.space[row][col] != 0:
                    rand = random.uniform(0,1)
                    if (rand > 0.2):
                        pygame.draw.rect(self.win, self.space[row][col], (row, col, 1, 1) )
        for piece in self.pieces:
            piece.draw(self.win)

    def update_backg(self):
        translation = 1 #control the speed of movement of background
        for row in range(WIDTH): #goal is to create the effect of space moving upward
            for col in range(HEIGHT-translation): #so give the previous row the next rows "star", 
                self.space[row][col] = self.space[row][col + translation]

        for row in range(WIDTH): #number of rows added at bottom
            for col in range(translation): #generate random values for all locations on a row
                rand = random.uniform(0,1)
                if rand > 0.98:
                    color = random.choice(COLORS)
                    self.space[row][HEIGHT - translation] = color
                else:
                    self.space[row][HEIGHT - translation] = 0


    def update(self):
        self.update_backg()
        self.display_backg()
        pygame.display.update()
