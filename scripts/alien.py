import pygame
from pygame.sprite import Sprite
from os.path import join
import sys

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carga la imagen del alien
        self.image = pygame.image.load(join("..","assets",'alien_ship.bmp'))
        self.image = pygame.transform.scale(self.image, (58, 26))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.alien_direction)
        self.rect.x = self.x
