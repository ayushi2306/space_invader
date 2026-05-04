import pygame
import random
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
player_x_change=0

#enemy
enemy_image=pygame.image.load('ghost.png')
enemy_x=random.randint(0,736)
enemy_y=random.randint(50,150)
enemy_x_change=0

def player(x,y):
    screen.blit(player_image,(x,y))

def enemy(x,y):
    screen.blit(enemy_image,(x,y))

#game loop 
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    # if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_x_change = -0.1
        if event.key == pygame.K_RIGHT:
            player_x_change = 0.1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player_x_change = 0      
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 764:
        player_x = 764
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pygame.display.update()