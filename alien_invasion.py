import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
    """General class to manage the resources and the behaviour of the game"""

    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

        # Background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Initialize the main loop of the game"""
        while True:
            # Keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Updates the screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Makes visible the last drawn screen
            pygame.display.flip()

if __name__ == '__main__':
    # Makes an instance of the game and executes it.
    ai = AlienInvasion()
    ai.run_game()
