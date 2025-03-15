import sys
import pygame

class AlienInvasion:
    """General class to manage the resources and the behaviour of the game"""

    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Initialize the main loop of the game"""
        while True:
            # Keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make visible the last drawn screen
            pygame.display.flip()

if __name__ == '__main__':
    # Make an instance of the game and execute it.
    ai = AlienInvasion()
    ai.run_game()
