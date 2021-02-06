import pygame
import random
import time
from .constants import WIDTH, HEIGHT, COLORS, BLACK, FIGHTER, REDBUG, EXPLOSION, LSRWIDTH, LSRLENGTH, LSRSPEED, RED
from .piece import Piece, Enemy

random.seed(1)

class Background:
    def __init__(self, win):
        self.win = win
        self.space = []
        self.pieces = []
        self.lasers = []
        self.curr_fighter = 0
        self.initial_backg()
        self.display_backg()

    def initial_backg(self):
        for row in range(WIDTH):
            self.space.append([])
            for col in range(HEIGHT):
                rand = random.random()
                if (rand > 0.98):
                    color = random.choice(COLORS)
                    self.space[row].append(color)
                else:
                    self.space[row].append(0)
        self.add_fighter(FIGHTER)
        for i in range(100, 500, 100):
            for j in range(200, 400, 40):
                self.add_enemy(REDBUG, i, j)
    
    def add_fighter(self, image):
        piece = Piece(image)
        self.pieces.append(piece)
        if self.curr_fighter == 0:
            self.curr_fighter = piece

    def add_enemy(self, image, x ,y ):
        piece = Enemy(image, x, y)
        self.pieces.append(piece)
        
    def display_backg(self):
        self.win.fill(BLACK)
        for row in range(WIDTH):
            for col in range(HEIGHT):
                if self.space[row][col] != 0:
                    rand = random.random()
                    if (rand > 0.2):
                        pygame.draw.rect(self.win, self.space[row][col], (row, col, 1, 1) )
        for piece in self.pieces:
            piece.draw(self.win)
        for laser in self.lasers: #these will be 2 pixels wide and 10 long
            pygame.draw.rect(self.win, RED, (laser[0], laser[1], LSRWIDTH, LSRLENGTH) )
            

    def update_backg(self):
        translation = 1 #control the speed of movement of background
        for row in range(WIDTH): #goal is to create the effect of space moving upward
            for col in range(HEIGHT-translation): #so give the previous row the next rows "star", 
                self.space[row][col] = self.space[row][col + translation]

        for row in range(WIDTH): #number of rows added at bottom
            for col in range(translation): #generate random values for all locations on a row
                rand = random.random()
                if rand > 0.98:
                    color = random.choice(COLORS)
                    self.space[row][HEIGHT - translation] = color
                else:
                    self.space[row][HEIGHT - translation] = 0

    def update(self):
        hits = 0
        for piece in self.pieces:
            if piece.image == EXPLOSION:
                self.pieces.remove(piece)
            else:
                piece.update()
            piece.update()
        for laser in self.lasers: #x,y
            laser[1] -= laser[2]
            if laser[1] <= 0:
                self.lasers.remove(laser)
            #check if it hits a bug
            for piece in self.pieces:
                if piece.image != REDBUG:
                    pass
                else:
                    if laser == 0:
                        break
                    else:
                        if laser[1] + LSRLENGTH <= piece.y + piece.image.get_width() and piece != self.curr_fighter: #use width bc the image is rotated
                            if (laser[0] < (piece.x + piece.image.get_height() // 2) ) and (laser[0] + LSRWIDTH > (piece.x - piece.image.get_height() // 2)):
                                hits += 1
                                self.add_enemy(EXPLOSION, piece.x, piece.y)
                                self.pieces.remove(piece)
                                self.lasers.remove(laser)
                                laser = 0 
                                break
                                #issue with remove() fixed ~usually~
                    #lhs_laser < rhs_piece and rhs_laser > lhs_piece
        self.update_backg()
        self.display_backg()
        pygame.display.update()

    def move_(self, xVel):
        if isinstance(self.curr_fighter, Piece):
            self.curr_fighter.move(xVel, 0)
        else:
            print("Wrong type for movement")

    def shoot(self):
        if len(self.lasers) <= 5:
            laser_loc = [self.curr_fighter.x, self.curr_fighter.y -LSRLENGTH, LSRSPEED]
            self.lasers.append(laser_loc)