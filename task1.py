import os

import pygame
import requests

size = ['450', '450']
spn = ['0.04', '0.04']
coor = ['37.530887', '55.703118']


def load_map():
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={','.join(coor)}&" \
                  f"spn={','.join(spn)}&size={','.join(size)}&l=map"
    response = requests.get(map_request)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

load_map()
pygame.init()
screen = pygame.display.set_mode((450, 450))
screen.blit(pygame.image.load('map.png'), (0, 0))
pygame.display.flip()
res = True

while res:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            res = False
            break
        if i.type == pygame.KEYUP:
            print('tyt', i.key)
            if i.key == pygame.K_UP and float(coor[1]) > -50:
                print(coor)
                coor[1] = str(float(coor[1]) + (float(size[1]) * float(spn[1]) * 0.002))
                print(coor)
                load_map()
                screen.blit(pygame.image.load('map.png'), (0, 0))
                pygame.display.flip()
            if i.key == pygame.K_DOWN:
                print(coor)
                coor[1] = str(float(coor[1]) - (float(size[1]) * float(spn[1]) * 0.002))
                print(coor)
                load_map()
                screen.blit(pygame.image.load('map.png'), (0, 0))
                pygame.display.flip()



pygame.quit()
os.remove('map.png')
