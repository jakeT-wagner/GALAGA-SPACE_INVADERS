from .constants import WIDTH, HEIGHT

class Piece:
    def __init__(self, image):
        self.image = image
        self.x = WIDTH / 2
        self.y = HEIGHT - self.image.get_height() - 5

    def draw(self, win): #pygame window
        win.blit(self.image, (self.x - self.image.get_width() // 2, self.y) )