import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class for one only alien enemy"""
    def __init__(self, ai_game):
        """Initialize alien and establsh initial position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image y configure its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Initialize a new alien close to the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save the exact horizontal position of the alien
        self.x = float(self.rect.x)