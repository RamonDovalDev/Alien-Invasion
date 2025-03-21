import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and configurate its initial position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Place initially each ship at the center bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Keep a decimal value for horizontal position of the ship
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship position according to the movement flags"""
        # Update the x value of the ship, nor the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update the rect object of self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its initial location"""
        self.screen.blit(self.image, self.rect)