import CA
import pygame
import sys
import sys

rule = int(sys.argv[1])
print(rule)
width = 800
height = 600

cellSize = 4
generationTimestep = 2 # In ms!
x = CA.dCA(rule, int(width/cellSize), [int(width/cellSize*0.5)])



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

    if x.generation * cellSize > height:
        del x.population[0]

    for g, pop in enumerate(x.population):
        for i, cell in enumerate(pop):
            if cell == 1:
                pygame.draw.rect(screen, (255, 255, 255), [i*cellSize, cellSize*g, cellSize, cellSize])


    #pygame.display.update([0, cellSize * x.generation, width, height])
    clock.tick(1000 / generationTimestep)
    x.generate()
    pygame.display.flip()
