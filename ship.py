import pygame

class Ship:
    """Class to manage the spaceship"""

    def __init__(self, ai_game):
        """Initialize the spaceship and configurate its initial position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the spaceship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Place the ship at its initial position at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float value for the horizontal position of the ship
        self.x = float(self.rect.x)

        #Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship location depending on the Movement Flag"""
        # Update the value x of the ship, nor the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 8:
            self.x -= self.settings.ship_speed

        # Update the object rect of self x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
