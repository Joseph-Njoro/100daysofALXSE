import pygame
import sys

# Initialize Pygame
pygame.init();

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")


running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    window.fill((0, 0, 0))  

    pygame.display,flip()  # Update the display

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()