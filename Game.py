import pygame
import os
from random import randint


# цвета и статус

def ugli(matrix, pos1, pos2, p):
    for el in range(0, p):
        if matrix[pos1][pos2-el] == matrix[pos1-1][pos2-el]:
            if matrix[pos1][pos2-el] == matrix[pos1 - 2][pos2-el]:
                matrix = change_color2(matrix, pos1-1, pos2-el, 2)
                matrix = change_color1(matrix, pos1, pos2, 3)
                print('sd')
        if pos1<8:
            if matrix[pos1][pos2-el] == matrix[pos1+1][pos2-el]:
                if matrix[pos1][pos2-el] == matrix[pos1 + 2][pos2-el]:
                    matrix = change_color1(matrix, pos1, pos2, 3)
                    matrix = change_color2(matrix, pos1+2, pos2-el, 2)
    return matrix


def change_color1(matrix, pos1, pos2, p):
    normalpos = pos2
    if pos1 != 0:
        for i in range(0, p):
            matrix[pos1][normalpos] = matrix[pos1 - 1][normalpos]
            normalpos -= 1
        change_color1(matrix, pos1 - 1, pos2, p)
    else:
        matrix = random_color1(matrix, pos2, p)
    return matrix


def random_color1(matrix, pos, p):
    for i in range(0, p):
        if pos > 0:
            matrix[0][pos] = randint(0, 4)
            pos -= 1
    return matrix


def change_color2(matrix, pos1, pos2, p):
    normalpos = pos1
    for i in range(0, normalpos + 1):
        if normalpos >= p - 1:
            matrix[normalpos][pos2] = matrix[normalpos - p][pos2]
            normalpos -= 1
        else:
            matrix[normalpos][pos2] = randint(0, 4)
            normalpos -= 1
    return matrix


def update(self, score):
    n = -1
    for el in self:
        n = n + 1
        for a in range(2, 9 + 1):
            if el[a] == el[a - 1]:
                if el[a] == el[a - 2]:
                    if a < 9 and el[a] == el[a + 1]:
                        if (a < 8) and (el[a] == el[a + 2]):
                            self = change_color1(self, n, a + 2, 5)
                            score += 500
                        else:
                            self = change_color1(self, n, a + 1, 4)
                            score += 400
                    else:
                        new_matrix = ugli(self, n, a, 3)
                        if new_matrix == self:
                            self = change_color1(self, n, a, 3)
                            score += 300
                        else:
                            self = new_matrix
                    n = 0
    for b in range(0, 10):
        for c in range(2, 9 + 1):
            if self[c][b] == self[c - 1][b]:
                if self[c][b] == self[c - 2][b]:
                    if c < 9 and self[c][b] == self[c + 1][b]:
                        if c < 8 and self[c][b] == self[c + 2][b]:
                            self = change_color2(self, c + 2, b, 5)
                            score += 500
                        else:
                            self = change_color2(self, c + 1, b, 4)
                            score += 400
                    else:
                        self = change_color2(self, c, b, 3)
                        score += 300
    return self, score


def new_check(self):
    matrix2 = self
    n = -1
    for el in self:
        n += 1
        for a in range(2, 9 + 1):
            if el[a] == el[a - 1]:
                if el[a] == el[a - 2]:
                    return 1
    for b in range(0, 10):
        for c in range(2, 9 + 1):
            if self[c][b] == self[c - 1][b]:
                if self[c][b] == self[c - 2][b]:
                    return 1
    return 0


class Game():
    def __init__(self):
        self.matrix = [[2, 3, 1, 3, 1, 2, 4, 2, 3, 2],
                       [3, 1, 2, 4, 2, 1, 3, 4, 1, 3],
                       [3, 2, 1, 2, 3, 4, 3, 1, 3, 4],
                       [4, 2, 1, 3, 2, 1, 0, 1, 3, 0],
                       [0, 0, 2, 4, 0, 1, 3, 2, 1, 0],
                       [1, 2, 0, 0, 3, 1, 0, 3, 2, 1],
                       [2, 1, 2, 1, 0, 2, 0, 4, 3, 1],
                       [1, 4, 3, 2, 0, 2, 4, 2, 3, 2],
                       [3, 1, 3, 0, 1, 2, 2, 3, 1, 0],
                       [4, 0, 1, 4, 1, 3, 4, 1, 3, 2]]
        for el in range(0, 10):
            for i in range(0, 10):
                self.matrix[el][i] = randint(0, 4)
        self.width = 90
        self.height = 90
        self.margin = 5
        self.window_size = [1150, 955]
        self.status = 1
        self.blue = (0, 0, 255)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.pink = (255, 130, 219)
        self.score = 0
        self.screen = None
        self.pos1 = 0
        self.pos2 = 0

    def run(self):
        i = 3000
        pygame.init()
        self.screen = pygame.display.set_mode(self.window_size)
        self.blue = pygame.image.load("PLANETA.jpg").convert()
        self.white = pygame.image.load("MET.jpg").convert()
        self.green = pygame.image.load("OBL.jpeg").convert()
        self.red = pygame.image.load("Zvezda.jpg").convert()
        self.pink = pygame.image.load("MP.jpeg").convert()
        background_image = pygame.image.load("BG.jpg").convert()
        done = False
        clock = pygame.time.Clock()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    for el in range(0, 10):
                        for i in range(0, 10):
                            self.matrix[el][i] = randint(0, 4)
                    print(self.score)
                    a = self.score
                    self.score = 0
                    return (a)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.status == 1:
                        POS1 = pygame.mouse.get_pos()
                        self.status = 2
                    elif self.status == 2:
                        POS2 = pygame.mouse.get_pos()
                        column = POS1[0] // (self.width + self.margin)
                        row = POS1[1] // (self.height + self.margin)
                        a = self.matrix[row][column]
                        column1 = POS2[0] // (self.width + self.margin)
                        row1 = POS2[1] // (self.height + self.margin)
                        if (column == column1 and (row - row1 == 1 or row - row1 == -1)) or (
                                        row == row1 and (column - column1 == 1 or column - column1 == -1)):
                            self.matrix[row][column] = self.matrix[row1][column1]
                            self.matrix[row1][column1] = a
                            self.status = 1
                            self.screen.blit(pygame.image.load("fg02.png").convert(), [990, 60])
                            c = new_check(self.matrix)
                            if c == 0:
                                a = self.matrix[row][column]
                                self.matrix[row][column] = self.matrix[row1][column1]
                                self.matrix[row1][column1] = a
                            else:
                                i = 3000
                        else:
                            print('wrong')
                            self.status = 1

            (self.matrix, self.score) = update(self.matrix, self.score)
            self.screen.blit(background_image, [0, 0])
            for row in range(10):
                for column in range(10):
                    color = self.white
                    if self.matrix[row][column] == 1:
                        color = self.blue
                    if self.matrix[row][column] == 2:
                        color = self.green
                    if self.matrix[row][column] == 3:
                        color = self.pink
                    if self.matrix[row][column] == 4:
                        color = self.red
                    self.screen.blit(color,
                                     [(self.margin + self.width) * column + self.margin,
                                      (self.margin + self.height) * row + self.margin])
            font = pygame.font.Font(None, 50)
            self.screen.blit(font.render(str(self.score), True, [255, 255, 255]), [980, 850])
            for b in range(0, i // 600 + 1):
                self.screen.blit(pygame.image.load("fg02.png").convert(), [990, 50 + b * 60])
                i -= 1
            if i == 0:
                done = True
                for el in range(0, 10):
                    for i in range(0, 10):
                        self.matrix[el][i] = randint(0, 4)
                a = self.score
                self.score = 0
                return (a)
            clock.tick(10)
            pygame.display.flip()
