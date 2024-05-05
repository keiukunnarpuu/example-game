class Settings:
    """Class for game settings"""
    
    
    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (153, 170, 181)
        self.caption = '''Vanda's Paradise'''
        
        self.bubble_min_r = 10
        self.bubble_max_r = 50
        
        self.bonus_score = 1000
        
        self.speed_min = 1
        self.speed_max = 5
        self.speed_level = 1
