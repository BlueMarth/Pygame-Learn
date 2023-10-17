import pygame
from sys import exit

# initiate everything for pygame
pygame.init()
# display surface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Run')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png') # import an image on a new surface
ground_surface = pygame.image.load('graphics/Ground.png')
text_surface = test_font.render('Run', False, 'Black')
# test_surface = pygame.Surface((100,200))
# test_surface.fill('red')

while True:
    # detect for any user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # draw all our elements
    screen.blit(sky_surface, (0,0)) #blit: block image transfer i.e. put one surface on top of another
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (350, 50))

    # update everything
    pygame.display.update()
    clock.tick(60) #should not run faster than 60 times per second