import pygame

class Ship:
    """A class to manage the spaceship"""

    def __init__(self, ai_game):
        """Initialize the spaceship and configurate its initial position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image y get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Initial position of the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Save a decimal value for the horizontal position of the spaceship
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the spaceship position according to the movement flag"""
        # Update the x value of the spaceship, nor the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect object of self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the spaceship at its current position"""
        self.screen.blit(self.image, self.rect)