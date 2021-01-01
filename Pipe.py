from Settings import *
import pygame



class Pipe:
    def __init__(self, sc, color, x, Vx, allowed_height, pipe_width, y, passed):
        self.sc = sc
        self.color = color
        self.x = x
        self.Vx = Vx
        self.allowed_height = allowed_height
        self.pipe_width = pipe_width
        self.y = y
        self.passed = passed

    def movement(self):
        self.x -= self.Vx

    def draw(self):

        pygame.draw.rect(self.sc, self.color, (self.x, self.y, self.pipe_width, HEIGHT - self.y))
        pygame.draw.rect(self.sc, self.color, (self.x, 0, self.pipe_width, self.y - self.allowed_height))

    def existing(self):
        if self.x <= -self.pipe_width:
            return False


