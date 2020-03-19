import pygame
pygame.init()
size = width, height = 600, 800
screen = pygame.display.set_mode(size)
running = True
screen.fill((0, 0, 0))


class Board:
    def __init__(self, width, height, rect, pos):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.rect = rect
        self.pos = pos

    def set_view(self, rect):
        self.rect = rect

    def can(self, x, y):
        if x < 0 or y < 0 or x + 1 > self.width or y + 1 > self.height:
            return False
        try:
            m = self.board[y][x]
            return True
        except:
            return False

    def render(self, screen):
        screen.fill((0, 0, 0))
        count = 0
        for i in range(0, self.width * self.rect[0], self.rect[0]):
            count_1 = 0
            for j in range(0, self.height * self.rect[1], self.rect[1]):
                if self.board[count_1][count] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (i + self.pos[0], j + self.pos[1],
                                                                self.rect[0],
                                                                self.rect[1]), 1)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (i + self.pos[0], j + self.pos[1],
                                                               self.rect[0],
                                                               self.rect[1]))
                count_1 += 1
            count += 1

    def revrs(self, num):
        if num == 0:
            return 1
        return 0

    def mouse_click(self, ev):
        if self.can((ev.pos[0] - self.pos[0]) // self.rect[0], (ev.pos[1] - self.pos[1]) // self.rect[1]):
            for i in range(self.width):
                self.board[(ev.pos[1] - self.pos[1]) // self.rect[1]][i] = self.revrs(self.board[(ev.pos[1] - self.pos[1]) // self.rect[1]][i])
            for i in range(self.height):
                self.board[i][(ev.pos[0] - self.pos[0]) // self.rect[0]] = self.revrs(self.board[i][(ev.pos[0] - self.pos[0]) // self.rect[0]])
            self.board[(ev.pos[1] - self.pos[1]) // self.rect[1]][(ev.pos[0] - self.pos[0]) // self.rect[0]] = self.revrs(self.board[(ev.pos[1] - self.pos[1]) // self.rect[1]][(ev.pos[0] - self.pos[0]) // self.rect[0]])


boarder = Board(5, 5, (50, 50), (70, 40))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == 6:
            boarder.mouse_click(event)
    boarder.render(screen)
    pygame.display.flip()