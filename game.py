# import and initialize the pygame library
import pygame
from settings import Settings

def run_game():
    pygame.init()
    gm_settings = Settings()
    # set up drawing window
    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)
    # run util user asks to quit
    running = True
    while running:
        screen.fill(gm_settings.bg_color)
        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # flip the display
            pygame.display.flip()
        # done! time to quit
        pygame.quit()
        
run_game()