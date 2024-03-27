import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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

# Define game functions
def move_ball():
    global ball_speed_x, ball_speed_y
    
    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball collision with top/bottom walls
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y *= -1
    
    # Ball collision with paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed_x *= -1

def draw_objects():
    # Clear the screen
    window.fill(BLACK)
    
    # Draw paddles and ball
    pygame.draw.rect(window, WHITE, player1_paddle)
    pygame.draw.rect(window, WHITE, player2_paddle)
    pygame.draw.ellipse(window, WHITE, ball)

    # Draw center line
    pygame.draw.aaline(window, WHITE, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT))

    # Update the display
    pygame.display.flip()

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
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
    move_ball()

    # Draw game objects
    draw_objects()

    # Control the frame rate
    clock.tick(60)

# Clean up
pygame.quit()