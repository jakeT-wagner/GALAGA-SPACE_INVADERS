from .constants import WIDTH, HEIGHT, FIGHTER

class Piece:
    def __init__(self, image):
        self.image = image
        self.set_x_y()
        self.xVel = 0
        self.yVel = 0

    def set_x_y(self):
        if self.image == FIGHTER:
            self.x = WIDTH/ 2
            self.y = HEIGHT-self.image.get_height() - 5

    def draw(self, win): #pygame window
        win.blit(self.image, (self.x - self.image.get_width() // 2, self.y) )

    def move(self, xVel, yVel):
        self.xVel = xVel #in pixels
        self.yVel = yVel #in pixels

    def update(self):
        if self.image == FIGHTER:
            if 0 <= (self.x + self.xVel) <= WIDTH:
                self.x += self.xVel
        else:
            self.x += self.xVel
            self.y += self.yVel

class Enemy(Piece):
    oscillation_dist = 30
    oscillation_steps = 15
    def __init__(self, image, x, y):
        self.image = image
        self.x, self.initial_x = x, x
        self.y, self.initial_y = y, y
        self.set_next_x_y()
        self.set_xVel_yVel()

    def set_next_x_y(self):
        if self.x >= WIDTH // 2:
            self.next_x = self.x + self.oscillation_dist
            self.xVel = 1
        else:
            self.next_x = self.x - self.oscillation_dist
            self.xVel = -1
        self.next_y = self.y + self.oscillation_dist
        self.yVel = 1
    
    def set_xVel_yVel(self):
        self.yVel = self.yVel * (self.oscillation_dist// self.oscillation_steps)
        self.xVel = self.xVel * (self.oscillation_dist// self.oscillation_steps)
    
    def update(self):
        if self.x == self.next_x and self.y == self.next_y:
            self.initial_x, self.next_x, = self.next_x, self.initial_x
            self.initial_y, self.next_y = self.next_y, self.initial_y
            self.xVel = -1 * self.xVel
            self.yVel = -1 * self.yVel
        self.x += self.xVel
        self.y += self.yVel
        
    