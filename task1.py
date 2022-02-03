import os

import pygame
import requests
from alf import func

size = ['450', '450']
spn = ['0.04', '0.04']
coor = ['37.530887', '55.703118']


def search(address, pt=False):
    global coor
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": address,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    coor = toponym_coodrinates.split(" ")
    load_map(pt=True)


def load_map(pt=False):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={','.join(coor)}&" \
                  f"spn={','.join(spn)}&size={','.join(size)}&l=map"
    if pt:
        map_request += f"&pt={','.join(coor)},pm2rdl1"
    response = requests.get(map_request)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


load_map()
pygame.init()
screen = pygame.display.set_mode((450, 575))
screen.fill((0, 0, 0))
screen.blit(pygame.image.load('map.png'), (0, 0))
pygame.display.flip()
res = True
word = ''
while res:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            res = False
            break
        if i.type == pygame.KEYUP:
            print(i.key)
            if i.key == pygame.K_UP and float(coor[1]) > -50:
                coor[1] = str(float(coor[1]) + float(spn[1]))
                load_map()
                screen.blit(pygame.image.load('map.png'), (0, 0))
                pygame.display.flip()
            if i.key == pygame.K_DOWN:
                coor[1] = str(float(coor[1]) - float(spn[1]))
                load_map()
                screen.blit(pygame.image.load('map.png'), (0, 0))
                pygame.display.flip()
            if i.key == pygame.K_LEFT:
                coor[0] = str(float(coor[0]) + float(spn[0]))
                load_map()
                screen.blit(pygame.image.load('map.png'), (0, 0))
                pygame.display.flip()
            if i.key == pygame.K_RIGHT:
                coor[0] = str(float(coor[0]) - float(spn[0]))
                load_map()
                screen.blit(pygame.image.load('map.png'), (0, 0))
                pygame.display.flip()
            if i.key == pygame.K_KP_ENTER or i.key == pygame.K_RETURN:
                search(word, pt=True)
                screen.blit(pygame.image.load('map.png'), (0, 0))
                pygame.display.flip()
            word = func(screen, word, i.key)

pygame.quit()
os.remove('map.png')
