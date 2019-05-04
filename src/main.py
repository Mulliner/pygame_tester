import pygame
import sys
from pygame.locals import *


winwidth = 640
winheight = 400
halfwinwidth = winwidth / 2
halfwinheight = winheight /2


pygame.init()
pygame.display.set_icon(pygame.image.load('char.png'))
displaysurf = pygame.display.set_mode((winwidth, winheight))
pygame.display.set_caption('Pygame Tester')

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
    'surface': pygame.transform.scale(player_img_l, (40, 40)),
    'facing': 'left',
    'size': 25,
    'x': halfwinwidth,
    'y': halfwinheight,
}


while True:

    player_center_x = player_obj['x'] + int(player_obj['size'] / 2)
    player_center_x = player_obj['y'] + int(player_obj['size'] / 2)

    displaysurf.fill((255, 255, 255))

    player_obj['rect'] = pygame.Rect((player_obj['x'] - camerax, player_obj['y'] - cameray, 40, 40))
    displaysurf.blit(player_obj['surface'], player_obj['rect'])

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_obj['surface'] = pygame.transform.scale(player_img_l, (player_obj['size'], player_obj['size']))
        player_obj['x'] += .05

    if keys[pygame.K_LEFT]:
        player_obj['surface'] = pygame.transform.scale(player_img_r, (player_obj['size'], player_obj['size']))
        player_obj['x'] -= .05

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == KEYDOWN:
        #     if event.key in (K_RIGHT, K_d):
        #         print('Right')
        #         player_obj['surface'] = pygame.transform.scale(player_img_l, (player_obj['size'], player_obj['size']))
        #         moveleft = False
        #         moveright = True
        #         player_obj['x'] += 10
        #     if event.key in (K_LEFT, K_a):
        #         print('Left')
        #         player_obj['surface'] = pygame.transform.scale(player_img_r, (player_obj['size'], player_obj['size']))
        #         moveleft = True
        #         moveright = False
        #         player_obj['x'] -= 10

    # This comes last..
    pygame.display.update()