import pygame
import random

class Bubble(pygame.sprite.Sprite):
    """Class for bubble object"""
    
    
    def __init__(self, screen, game_settings):
        """Initialize bubble"""
        super(Bubble, self).__init__()
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.bubble_radius = random.randint(game_settings.bubble_min_r, game_settings.bubble_max_r)
        
        self.bubble = pygame.Surface((self.bubble_radius * 2, self.bubble_radius * 2), pygame.SRCALPHA)
        
        self.bubble.set_colorkey(game_settings.bg_color)
        
        self.bubble.set_alpha(128)
        
        self.rect = pygame.draw.circle(
            self.bubble,
            (255, 255, 255),
            (self.bubble_radius, self.bubble_radius),
            self.bubble_radius,
            2)
        
        self.rect = self.bubble.get_rect(
                center=(
                    random.randint(game_settings.screen_height + 20, game_settings.screen_width + 100),
                    random.randint(0, game_settings.screen_height),
                )
            )
        self.speed = random.randint(game_settings.speed_min * game_settings.speed_level, game_settings.speed_max * game_settings.speed_level)
        
    def blit_me(self):
        self.screen.blit(self.bubble, self.rect)
    
    def update(self):
        """Update the position of the bubble."""
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
