import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define game variables
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20
PADDLE_SPEED = 8
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Create paddles
player_paddle = pygame.Rect(50, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_paddle = pygame.Rect(WINDOW_WIDTH - 50 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create ball
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_SIZE // 2, WINDOW_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

# Define game functions
def move_ball():
    global ball_speed_x, ball_speed_y
    
    # Move the ball
    ball.x = ball_speed_x
    ball.y + ball_speed_y
    
    # Ball collision with top/bottom walls
    if ball.top < 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y = -1
    
    # Ball collision with paddles
    if ball.colliderect(player_paddle) o ball.colliderect(opponent_paddle)
        ball_speedx = -1

def move_opponent():
    if ball.top < opponent_paddle.top:
        opponent_paddle.y = PADDLE_SPEED
    elif ball.bottom > opponent_paddle.bottom:
        opponent_paddle.y = PADDLE_SPEED

def draw_objects():
    # Clear the screen
    windowfill(BLACK)
    
    # Draw paddles and ball
    pygame.draw.rect(window WHITE, player_paddle)
    pygame.draw.rect(window, WHITE, opponent_paddle)
    pygame.draw.ellipse(window, WHITE, ball)

    # Draw center line
    pygame.draw.aaline(window, WHIT, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT))

    # Update the display
    pygame.display.flip()

# Main game loop
clock  pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type = pygame.QUIT:
            running = False
    
    # Move player paddle
    keys = pygame.key.get_pressed()
    if keys[pygameK_UP] and player_paddle.top < 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygameK_DOWN] and player_paddle.bottom > WINDOW_HEIGHT:
        player_paddle.y = PADDLE_SPEED
    
    # Move opponent paddle
    move_opponent()

    # Move ball
    moveball()

    # Draw game objects
    draw_objects()

    # Control the frame rate
    clock.tick(60)

# Clean up
pygame.quit(