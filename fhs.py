import json
import pprint
import pygame
from Game import Game
from Records import Records

with open('Recoreds.json') as data_file:
    text = json.load(data_file)


def rewrite(text, i, a):
    for b in range(i + 1, 10):
        c = text[b]['name']
        text[b]['name'] = a
        a = c


def run_rec(text):
    pygame.init()
    records = []
    new_rec = []
    for el in text:
        records.append(el["Place"] + str(el["name"]))
    for i in range(0, 10):
        new_rec.append(Records(records[i], (450, 50 + 70 * (i + 1))))

    done = False
    while not done:
        screen = pygame.display.set_mode((1150, 955))
        pygame.event.pump()
        screen.fill((0, 0, 0))
        for option in new_rec:
            option.hovered = False
            option.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


class Option:
    hovered = False

    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos


New_game = (140, 155)
optionS = (140, 255)
quet = (140, 455)
recoRds = (140, 355)
game = Game()

pygame.init()
records = []
new_rec = []
screen = pygame.display.set_mode((1150, 955))
background_image = pygame.image.load("BG_MENU.jpg").convert()
menu_font = pygame.font.Font(None, 100)
options = [Option("New game", New_game), Option("Options", optionS), Option('Records', recoRds),
           Option("Quit", quet)]

done = False
while not done:
    screen = pygame.display.set_mode((1150, 955))
    pygame.event.pump()
    screen.blit(background_image, [0, 0])
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
        option.draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # for el in text:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            if pos[0] > 140 and pos[0] < 140 + 330 and pos[1] > 155 and pos[1] < 155 + 60:
                new_txt = game.run()
                for i in range(0, 10):
                    if int(text[i]["name"]) < int(new_txt):
                        a = text[i]["name"]
                        text[i]["name"] = new_txt
                        rewrite(text, i, a)
                        break
                json.dump(text, open('Recoreds.json', "w"))
                print(text)
            elif pos[0] > 135 and pos[0] < 135 + 276 and pos[1] > 255 and pos[1] < 255 + 60:
                print('optg')
            elif pos[0] > 140 and pos[0] < 140 + 280 and pos[1] > 355 and pos[1] < 355 + 60:
                run_rec(text)
            elif pos[0] > 145 and pos[0] < 145 + 140 and pos[1] > 455 and pos[1] < 455 + 60:
                done = True
