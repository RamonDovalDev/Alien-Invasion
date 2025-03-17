class Settings:
    """A class to store all Alien Invasion configuration"""

    def __init__(self):
        """Starts game configuration"""
        # Screen configuration
        self.screen_width = 1020
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        #Bullets configuration
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)