import pygame
import random
#initialise the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load('5532919.jpg')

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
enemy_x_change=0.1
enemy_y_change=40

#bullet
bullet_image=pygame.image.load('bullet.png')
bullet_x=0
bullet_y=480
bullet_x_change=0
bullet_y_change=0.5
#bullet_state="ready" # ready - you can't see the bullet on the screen, fire - the bullet is currently moving
bullet_state="ready"


def player(x,y):
    screen.blit(player_image,(x,y))

def enemy(x,y):
    screen.blit(enemy_image,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image,(x+16,y+10))

#game loop 
running = True
while running:

    screen.fill((50, 0, 70)) # RGB for black
    #background image 
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get the current x coordinate of the spaceship
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # checking for boundaries of spaceship so it doesn't go out of bounds   
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 764:
        player_x = 764
    
    # enemy movement
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 0.1
        enemy_y += enemy_y_change
    elif enemy_x >= 764:   
        enemy_x_change = -0.1
        enemy_y += enemy_y_change

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    

    # bullet function is being called so it can move
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y-=bullet_y_change

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)


    pygame.display.update()