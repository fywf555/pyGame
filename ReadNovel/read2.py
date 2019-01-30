import pygame
from pygame.locals import *
from sys import exit


with open("..\ReadNovel\#1.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()

num = -1
def readTxt():
    global num
    num += 1
    return lines[num]



pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background_image = 'timg.jpg'
background = pygame.image.load(background_image).convert()

# 以下两种方法都可以，第一种需要把字体文件复制到代码文件目录下
# font = pygame.font.Font("simhei.ttf", 40)
font = pygame.font.SysFont("simsunnsimsun", 40)

text_surface = font.render("你好", True, (0, 0, 255))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                text_surface = font.render(readTxt(), True, (0, 0, 255))
    screen.blit(background, (0, 0))
    x = 0
    y = (480 - text_surface.get_height()) / 2
    screen.blit(text_surface, (x, y))
    pygame.display.update()
