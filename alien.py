import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to depict just one alien in the Alien Fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and place it at its initial position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and configurate its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Initialize a new alien close to the top left part of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save the exact alien horizontal position
        self.x = float(self.rect.x)