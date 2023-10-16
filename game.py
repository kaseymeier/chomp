import pygame
import time
import sys


print(f"the quit even is type {pygame.QUIT}")
pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Chomp!')
screen.fill((114,159,255))

pygame.draw.rect(screen, (100,25,0),(0,380,400,400))
pygame.draw.rect(screen, (0, 200, 100), (0, 75, 74, 74))

sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (200, 200, 64, 64))


while True:
   for event in pygame.event.get():

      if event.type == pygame.QUIT:
         print("thanks for playing")
         pygame.quit()
         sys.exit()

      pygame.display.flip()


