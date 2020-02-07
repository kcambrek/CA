import CA
import pygame

width = 800
height = 600

cellSize = 5
generationTimestep = 500 # In ms!
x = CA.ddCA((int(width/cellSize), int(height/cellSize)), 0.15)



pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CA")
clock = pygame.time.Clock()

session = True

while session:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            session = False

    for i in range(len(x.population)):
        for j in range(len(x.population[0])):
            if x.population[i][j] > 0:
                pygame.draw.rect(screen, (255, 255, 255), (i*cellSize, j*cellSize, cellSize, cellSize))

    x.generate()
    #pygame.display.update([0, cellSize * x.generation, width, height])
#    clock.tick(1000 / generationTimestep)
    clock.tick(10)
    pygame.display.flip()
