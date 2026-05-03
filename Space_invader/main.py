import pygame
#initialise the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
player_image=pygame.image.load('spaceship.png')
player_x=360
player_y=480

def player():
    screen.blit(player_image,(player_x,player_y))

#game loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    screen.fill((0, 0, 0))

    player()
    pygame.display.update()