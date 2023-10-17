import pygame
from sys import exit

# initiate everything for pygame
pygame.init()
# display surface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('insert title')
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200))
test_surface.fill('red')

while True:
    # detect for any user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # draw all our elements
    screen.blit(test_surface, (200,100)) #blit: block image transfer i.e. put one surface on top of another

    # update everything
    pygame.display.update()
    clock.tick(60) #should not run faster than 60 times per second