import pygame
import sys

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SAND_HEIGHT = 20
TILE_SIZE = 64  # tiles are square height==width

# COLORS

WATER_COLOR = (114, 159, 232)
SAND_COLOR = (100, 25, 0)

print(f"the quit even is type {pygame.QUIT}")
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chomp!')
screen.fill(WATER_COLOR)

pygame.draw.rect(screen, SAND_COLOR, (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
pygame.draw.rect(screen, (0, 200, 100), (0, 75, 74, 74))

sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (SCREEN_WIDTH / 2 - TILE_SIZE / 2, SCREEN_HEIGHT / 2 - TILE_SIZE / 2))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("thanks for playing")
            pygame.quit()
            sys.exit()

        pygame.display.flip()
