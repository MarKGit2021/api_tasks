import os

import pygame
import requests


def find(text):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    toponym_to_find = text
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    return toponym_longitude, toponym_lattitude


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
    map = "map"
    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": map,
        "pt": "0"
    }
    text = ''
    font = pygame.font.SysFont('arial', 20)
    font2 = pygame.font.SysFont('arial', 14)
    pt = False
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEUP:
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
                elif event.key == pygame.K_UP:
                    if float(lat) < 84:
                        if float(delta) < 3:
                            lat = str(float(lat) + 0.01)
                            response = requests.get(api_server, params=params)
                        elif 3 <= float(delta) < 10:
                            lat = str(float(lat) + 0.1)
                            response = requests.get(api_server, params=params)
                        else:
                            lat = str(float(lat) + 0.5)
                            response = requests.get(api_server, params=params)
                elif event.key == pygame.K_DOWN:
                    if float(lat) > -84:
                        if float(delta) < 3:
                            lat = str(float(lat) - 0.01)
                            response = requests.get(api_server, params=params)
                        elif 3 <= float(delta) < 10:
                            lat = str(float(lat) - 0.1)
                            response = requests.get(api_server, params=params)
                        else:
                            lat = str(float(lat) - 0.5)
                            response = requests.get(api_server, params=params)
                elif event.key == pygame.K_LEFT:
                    if float(delta) < 3:
                        lon = str(float(lon) - 0.01)
                        response = requests.get(api_server, params=params)
                    elif 3 <= float(delta) < 10:
                        lon = str(float(lon) - 0.1)
                        response = requests.get(api_server, params=params)
                    else:
                        lon = str(float(lon) - 0.5)
                        response = requests.get(api_server, params=params)
                elif event.key == pygame.K_RIGHT:
                    if float(delta) < 3:
                        lon = str(float(lon) + 0.01)
                        response = requests.get(api_server, params=params)
                    elif 3 <= float(delta) < 10:
                        lon = str(float(lon) + 0.1)
                        response = requests.get(api_server, params=params)
                    else:
                        lon = str(float(lon) + 0.5)
                        response = requests.get(api_server, params=params)
                elif event.key != pygame.K_RETURN:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif event.key != pygame.K_SPACE:
                        text += event.unicode
                    elif event.key == pygame.K_SPACE:
                        text += ' '
                elif event.key == pygame.K_RETURN:
                    lon, lat = find(text)
                    delta = '0.005'
                    pt = True
                    ptlon = lon
                    ptlat = lat
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print(400 < x < 460, )
                if 400 < x < 460 and 5 < y < 30:
                    map = 'map'
                elif 465 < x < 525 and 5 < y < 30:
                    map = 'sat'
                elif 530 < x < 590 and 5 < y < 30:
                    map = 'sat,skl'

        if pt:
            params = {
                "ll": ",".join([lon, lat]),
                "spn": ",".join([delta, delta]),
                "l": map,
                "pt": f"{ptlon},{ptlat},pm2rdl1"
            }

        else:
            params = {
                "ll": ",".join([lon, lat]),
                "spn": ",".join([delta, delta]),
                "l": map,
            }
        # карта
        map_file = "map.png"
        response = requests.get(api_server, params=params)
        with open(map_file, "wb") as file:
            file.write(response.content)
        screen.blit(pygame.image.load(map_file), (0, 0))
        # Текствое поле
        pygame.draw.rect(screen, (0, 0, 0), (10, 10, 200, 30), width=2)
        text_surf = font.render(text, True, (0, 0, 0))
        screen.blit(text_surf, (13, 13))
        # Кнопки
        pygame.draw.rect(screen, (0, 0, 0), (400, 5, 60, 25), width=2)
        pygame.draw.rect(screen, (0, 0, 0), (465, 5, 60, 25), width=2)
        pygame.draw.rect(screen, (0, 0, 0), (530, 5, 60, 25), width=2)
        text_surf1 = font2.render('Схема', True, (0, 0, 0))
        screen.blit(text_surf1, (410, 7))
        text_surf2 = font2.render('Спутник', True, (0, 0, 0))
        screen.blit(text_surf2, (470, 7))
        text_surf3 = font2.render('Гибрид', True, (0, 0, 0))
        screen.blit(text_surf3, (535, 7))

        pygame.display.flip()
        clock.tick(60)
        os.remove(map_file)
