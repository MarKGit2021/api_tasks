import os
import sys

import pygame
import requests

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    pygame.display.flip()
    clock = pygame.time.Clock()
    run = True

    api_server = "http://static-maps.yandex.ru/1.x/"
    lon = "37.530887"
    lat = "55.703118"
    delta = "0.1"
    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEUP:
                    print('up')
                    if 0.05 >= float(delta) >= 0.01:
                        delta = str(round(float(delta) + 0.02, 2))
                        response = requests.get(api_server, params=params)
                    elif 0.1 >= float(delta) >= 0.05:
                        delta = str(round(float(delta) + 0.03, 2))
                        response = requests.get(api_server, params=params)
                    elif 0.5 >= float(delta) >= 0.1:
                        delta = str(round(float(delta) + 0.07, 2))
                        response = requests.get(api_server, params=params)
                    elif 1 >= float(delta) >= 0.5:
                        delta = str(round(float(delta) + 0.1, 2))
                        response = requests.get(api_server, params=params)
                    else:
                        delta = str(round(float(delta) + 0.5, 2))
                        response = requests.get(api_server, params=params)
                elif event.key == pygame.K_PAGEDOWN:
                    print('down')
                    if float(delta) - 0.01 > 0:
                        if 0.05 >= float(delta) >= 0.01:
                            delta = str(round(float(delta) - 0.02, 2))
                            response = requests.get(api_server, params=params)
                        elif 0.1 >= float(delta) >= 0.05:
                            delta = str(round(float(delta) - 0.03, 2))
                            response = requests.get(api_server, params=params)
                        elif 0.5 >= float(delta) >= 0.1:
                            delta = str(round(float(delta) - 0.07, 2))
                            response = requests.get(api_server, params=params)
                        elif 1 >= float(delta) >= 0.5:
                            delta = str(round(float(delta) - 0.1, 2))
                            response = requests.get(api_server, params=params)
                        else:
                            delta = str(round(float(delta) - 0.5, 2))
                            response = requests.get(api_server, params=params)


        params = {
            "ll": ",".join([lon, lat]),
            "spn": ",".join([delta, delta]),
            "l": "map"
        }
        map_file = "map.png"
        response = requests.get(api_server, params=params)
        with open(map_file, "wb") as file:
            file.write(response.content)

        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
        clock.tick(60)
        os.remove(map_file)
