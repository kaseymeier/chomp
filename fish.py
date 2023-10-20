import pygame
from Settings import *

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = fish_graphic = pygame.image.load("assets/images/fish.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.x = x
        self.y = y
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        print("I am a brand new fish ;)")

    def move_left(self):
        self.x -= 5
        print("swimming to the left")
    def move_right(self):
        self.x += 5
        print('swimming to the right')
    def move_up(self):
        self.y += 5
    def move_down(self):
        self.y -= 5
    def update(self):
        if self.moving_left:
            self.x -= 5
        elif self.moving_right:
            self.x += 5
        if self.moving_up:
            self.y -= 5
        elif self.moving_down:
            self.y += 5
        #make sure fish is within bounds
        if self.x <0:
            self.x = 0
        if self.y <0:
            self.y = 0
        if self.x >= SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - TILE_SIZE
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
