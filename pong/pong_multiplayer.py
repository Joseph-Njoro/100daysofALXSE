import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1000
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load background image
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Define game variables
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20
PADDLE_SPEED = 12
BALL_SPEED_X = 7
BALL_SPEED_Y = 7

# Create paddles
player1_paddle = pygame.Rect(50, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(WINDOW_WIDTH - 50 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create ball
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_SIZE // 2, WINDOW_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

# Define font for countdown text
font = pygame.font.Font(None, 200)

# Define game functions
def move_ball():
    global ball_speed_x, ball_speed_y
    
    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball collision with top/bottom walls
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y *= -1
    
    # Ball collision with left/right walls (miss)
    if ball.left <= 0 or ball.right >= WINDOW_WIDTH:
        return True
    
    # Ball collision with paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed_x *= -1

def draw_objects(countdown):
    # Draw background image
    window.blit(background_image, (0, 0))
    
    # Draw paddles and ball
    pygame.draw.rect(window, WHITE, player1_paddle)
    pygame.draw.rect(window, WHITE, player2_paddle)
    pygame.draw.ellipse(window, WHITE, ball)

    # Draw center line
    pygame.draw.aaline(window, WHITE, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT))

    # Draw countdown text
    countdown_text = font.render(str(countdown), True, RED)
    countdown_rect = countdown_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    window.blit(countdown_text, countdown_rect)

    # Update the display
    pygame.display.flip()

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    countdown = 3
    # Countdown before every game starts
    while countdown > 0:
        for event in pygame.event.get():  # Handle events to prevent video system error
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_objects(countdown)
        pygame.time.wait(1000)  # Wait 1 second
        countdown -= 1
    
    # Reset game state
    ball.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
    ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
    player1_paddle.y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
    player2_paddle.y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Move player paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_paddle.top > 0:
            player1_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and player1_paddle.bottom < WINDOW_HEIGHT:
            player1_paddle.y += PADDLE_SPEED
        if keys[pygame.K_UP] and player2_paddle.top > 0:
            player2_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player2_paddle.bottom < WINDOW_HEIGHT:
            player2_paddle.y += PADDLE_SPEED
        
        # Move ball
        if move_ball():
            if ball.left <= 0:
                print("ANGEL scores!")
            elif ball.right >= WINDOW_WIDTH:
                print("RAMOZ scores!")
            ball.x = WINDOW_WIDTH // 2 - BALL_SIZE // 2
            ball.y = WINDOW_HEIGHT // 2 - BALL_SIZE // 2
            ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
            ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
        
        # Draw game objects
        draw_objects(countdown)

        # Control the frame rate
        clock.tick(60)

# Clean up
pygame.quit()