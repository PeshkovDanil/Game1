import pygame
import json
from pprint import pprint

with open('Recoreds.json') as data_file:
    text = json.load(data_file)


class Records:
    hovered = False

    def __init__(self, text, pos):

        self.menu_font = pygame.font.Font(None, 100)
        self.screen = pygame.display.set_mode((1150, 955))
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()

    def draw(self):
        self.set_rend()
        self.screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = self.menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos
