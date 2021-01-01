import pygame
from Settings import *
from Bird import *
from Pipe import *
from  random import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pipes = []
passed_pipes = []
pipe = Pipe(sc, GREEN, WIDTH, Vx, ALLOWED_HEIGHT, PIPE_WIDTH, randint(ALLOWED_HEIGHT + 150, HEIGHT - GROUND_HEIGHT -150), False)
pipes.append(pipe)

bird = Bird(sc, x_0, y_0, 0, YELLOW, RADIUS, DASH_V, pipes, passed_pipes)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill(BLUE)

    bird.movement()
    bird.draw()

    for pipe in pipes:
        if pipe.existing() == False:
             pipes.remove(pipe)
        else:
            pipe.movement()
            pipe.draw()



    if pipes[-1].x <= WIDTH - PIPES_DIST - PIPE_WIDTH:
        pipes.append(Pipe(sc, GREEN, WIDTH, Vx, ALLOWED_HEIGHT, PIPE_WIDTH, randint(ALLOWED_HEIGHT + 150, HEIGHT - GROUND_HEIGHT -150), False))

    # ground
    pygame.draw.rect(sc, OLIVE, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))
    if bird.y >= HEIGHT - GROUND_HEIGHT - RADIUS:
        file = open('Highscores.txt', 'a')
        file.write(str(bird.score()) + '\n')
        file.close()
        exit()
    if bird.check():
        file = open('Highscores.txt', 'a')
        file.write(str(bird.score()) + '\n')
        file.close()
        exit()


    f1 = pygame.font.SysFont('arial', 70)
    score1 = f1.render(str(bird.score()), True, RED)
    sc.blit(score1, (int(WIDTH * 0.8), int(HEIGHT * 0.1 )))



    pygame.display.flip()
    clock.tick(FPS)
