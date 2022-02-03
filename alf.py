import pygame

alf = [113,
       119, 101, 114, 116, 121, 117, 105, 111,
       112, 91, 93,
       97, 115, 100, 102, 103, 104, 106, 107, 108, 59, 39, 122, 120,
       99, 118, 98, 110, 109, 44, 46, 32, 49, 50, 51, 52, 53, 54, 55, 56, 57, 48]
alf1 = 'йцукенгшщзхъфывапролджэячсмитьбю 1234567890'


def func(screen, words, ch):
    if ch in alf:
        words += alf1[alf.index(ch)]
        if len(words.split('\n')[-1]) > 28:
            words += '\n'
    font = pygame.font.Font(None, 30)
    text_coord = 475

    for i in words.split('\n'):
        string_rendered = font.render(str(i), 1,
                                      pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
        text_coord += 20

    pygame.display.flip()
    return words
