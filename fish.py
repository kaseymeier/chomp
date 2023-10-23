import pygame
from Settings import *


class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        self.right_image = pygame.image.load("assets/images/fish.png").convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.image = self.right_image
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        print("I am a brand new fish ;)")
    def update(self):
        if self.moving_left:
            self.rect.x -= 5
        elif self.moving_right:
            print(f"moving right! {self.rect.x}")
            self.rect.x += 5
            if self.rect.x>512:
                print("here!")
        if self.moving_up:
            self.rect.y -= 5
        elif self.moving_down:
            self.rect.y += 5
        # make sure fish is within bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > SCREEN_WIDTH:
            print("stoppe!")
            self.rect.right = SCREEN_WIDTH
        if self.rect.left > SCREEN_HEIGHT:
            self.rect.left = SCREEN_HEIGHT
        if self.rect.bottom > SCREEN_HEIGHT - 2 * TILE_SIZE:
            self.rect.bottom = SCREEN_HEIGHT - 2 * TILE_SIZE


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
