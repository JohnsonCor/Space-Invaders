class Settings():
    """A class to store all setting for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Ship settings
        self.ship_speed_factor = 1.5
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (0, 0, 0)
        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 255, 0
        self.bullets_allowed = 4