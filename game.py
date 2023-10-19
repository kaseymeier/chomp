import pygame
import sys
import random

from Settings import *

pygame.init()

game_font = pygame.font.Font("assets/fonts/MASQUE__.ttf", 128)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chomp!')
screen.fill(WATER_COLOR)

pygame.draw.rect(screen, SAND_COLOR, (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
pygame.draw.rect(screen, (0, 200, 100), (0, 75, 74, 74))

sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
seagrass = pygame.image.load("assets/images/seagrass.png").convert()
sand_top.set_colorkey((0, 0, 0))
seagrass.set_colorkey((0, 0, 0))
# blit sand tiles across the bottom of the screen
for i in range(int(SCREEN_WIDTH / TILE_SIZE)):
    screen.blit(sand, (TILE_SIZE * i, SCREEN_WIDTH - TILE_SIZE))
    screen.blit(sand_top, (TILE_SIZE * i, SCREEN_HEIGHT - (2 * TILE_SIZE)))
for _ in range(4):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(SCREEN_HEIGHT - 2*TILE_SIZE, SCREEN_HEIGHT) - (0.5 * TILE_SIZE)
    screen.blit(seagrass, (x,y))
    #draw the title CHOMP!

text = game_font.render("CHOMP!", True, (255, 69, 0))
screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("thanks for playing")
            pygame.quit()
            sys.exit()
        pygame.display.flip()
