class Settings: 
    """A class to keep all Alien Invasion configuration"""

    def __init__(self):
        """Initialize the game configurtation"""
        # Screen configuration
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship configuration
        self.ship_speed = 1.5

        # Bullets configuration
        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien configuration
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 1 represents to the right; -1, to the left
        self.fleet_direction = 1