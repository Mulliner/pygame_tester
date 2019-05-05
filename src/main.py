import pygame
import sys
from pygame.locals import *
from environment import Background


winwidth = 640
winheight = 400
halfwinwidth = winwidth / 2
halfwinheight = winheight / 2

movespeed = 1

pygame.init()
pygame.display.set_icon(pygame.image.load('char.png'))
displaysurf = pygame.display.set_mode((winwidth, winheight), pygame.RESIZABLE)
pygame.display.set_caption('Pygame Tester')

background = Background('background_forest.png', [0,0])

# Setup Camera
camerax = 0
cameray = 0

moveleft = False
moveright = False
moveup = False
movedown = False

# Setup Player
player_img_l = pygame.image.load('char.png')
player_img_r = pygame.transform.flip(player_img_l, True, False)
player_obj = {
    'surface': pygame.transform.scale(player_img_l, (25, 25)),
    'facing': 'left',
    'size': 25,
    'x': halfwinwidth,
    'y': halfwinheight + 50,
}
facing_direction = 'right'

displaysurf.fill((255, 255, 255))

while True:
    displaysurf.blit(background.image, background.rect)
    player_center_x = player_obj['x'] + int(player_obj['size'] / 2)
    player_center_x = player_obj['y'] + int(player_obj['size'] / 2)

    player_obj['rect'] = pygame.Rect((player_obj['x'] - camerax, player_obj['y'] - cameray, player_obj['size'], player_obj['size']))
    displaysurf.blit(player_obj['surface'], player_obj['rect'])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_a]:
        player_obj['surface'] = pygame.transform.scale(player_img_l, (player_obj['size'], player_obj['size']))
        player_obj['x'] += movespeed
        facing_direction = 'right'

    if keys[pygame.K_LEFT] or keys[pygame.K_d]:
        player_obj['surface'] = pygame.transform.scale(player_img_r, (player_obj['size'], player_obj['size']))
        player_obj['x'] -= movespeed
        facing_direction = 'left'
    
    if keys[pygame.K_SPACE]:
        fire_img = pygame.image.load('fire.png')
        fire_obj = {
            'surface': pygame.transform.scale(fire_img, (50, 50)),
            'facing': 'left',
            'size': 50,
            'x': halfwinwidth,
            'y': halfwinheight,
        }
        if facing_direction == 'right':
            fire_obj['rect'] = pygame.Rect((player_obj['x'] + 20 - camerax, player_obj['y'] - 8 - cameray, fire_obj['size'], fire_obj['size']))
        
        if facing_direction == 'left':
            fire_img = pygame.transform.flip(fire_img, True, False)
            fire_obj['rect'] = pygame.Rect((player_obj['x'] - 45 - camerax, player_obj['y'] - 8 - cameray, fire_obj['size'], fire_obj['size']))
        displaysurf.blit(fire_obj['surface'], fire_obj['rect'])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # This comes last..
    pygame.display.update()
