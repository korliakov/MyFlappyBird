from Settings import *
import pygame



class Bird:
    def __init__(self, sc, x, y, Vy, color, radius, dash_v, pipes, passed_pipes):
        self.y = y
        self.x = x
        self.Vy = Vy
        self.color = color
        self.radius = radius
        self.sc = sc
        self.dash_v = dash_v
        self.pipes = pipes
        self.passed_pipes = passed_pipes


    def movement(self):
        self.y += self.Vy
        self.Vy += g
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.Vy = -self.dash_v

    def draw(self):
        pygame.draw.circle(self.sc, self.color, (self.x, self.y), self.radius)

    def check(self):
        for pipe in self.pipes:
            if (pipe.x <= self.x <= pipe.x + PIPE_WIDTH) and (self.y >= pipe.y - self.radius or self.y <= pipe.y - ALLOWED_HEIGHT + self.radius):
                return True
            elif (self.y >= pipe.y - self.radius or self.y <= pipe.y - ALLOWED_HEIGHT + self.radius) and pipe.x + PIPE_WIDTH + self.radius >= self.x >= pipe.x - self.radius:
                return True
            elif ((self.x - pipe.x)**2 + (self.y - pipe.y)**2) <= self.radius**2 or ((self.x - pipe.x)**2 + (self.y - (pipe.y - ALLOWED_HEIGHT))**2) <= self.radius**2:
                return True
            elif ((self.x - (pipe.x + PIPE_WIDTH))**2 + (self.y - pipe.y)**2) <= self.radius**2 or ((self.x - (pipe.x+PIPE_WIDTH))**2 + (self.y - (pipe.y - ALLOWED_HEIGHT))**2) <= self.radius**2:
                return True

    def score(self):
        for pipe in self.pipes:
            if self.x > pipe.x + PIPE_WIDTH + self.radius and not(pipe.passed):
                pipe.passed = True
                self.passed_pipes.append(pipe)
        return len(self.passed_pipes)


