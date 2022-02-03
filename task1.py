import os

import pygame
import requests

map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&" \
              "spn=0.04,0.04&size=450,450&l=map"
response = requests.get(map_request)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((450, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)
