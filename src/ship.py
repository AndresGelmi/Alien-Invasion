import pygame
from pygame.sprite import Sprite
from os.path import join
import sys

class Ship(Sprite):
    def __init__(self, ai_game, size=(75, 75)):  # Añade un parámetro de tamaño con un valor predeterminado
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings  # Asume que Settings ya es parte de ai_game

        # Carga la imagen de la nave
        self.image = pygame.image.load(join("..","assets", "ship.bmp"))
        self.image = pygame.transform.scale(self.image, size)  # Usa el parámetro de tamaño aquí

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)  # Asegura que x sea un float para movimientos precisos

        # Banderas de movimiento
        self.moving_right = False
        self.moving_left = False



    def blitme(self):
        """Dibuja la nave en su ubicación actual."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Actualiza la posición de la nave basada en las banderas de movimiento."""
        # Actualiza el valor del centro de la nave, no el rectángulo.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.speed

        # Actualiza el objeto rect de self.x.
        self.rect.x = self.x

    def center_ship(self):
        """Centra la nave en la pantalla."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
