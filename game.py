# import and initialize the pygame library
import pygame
pygame.init()

# set up drawing window
screen = pygame.display.set_mode([800, 600])

# run util user asks to quit
running = True
while running:
    
    # did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # flip the display       
    pygame.display.flip()

# done! time to quit
pygame.quit()