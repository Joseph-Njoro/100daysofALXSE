import pygame
import random

pygame.init()

# Set up the game window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

# Load background image
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 15
BALL_SIZE = 10
BALL_SPEED_X = 8
BALL_SPEED_Y = 8

# Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += PADDLE_SPEED

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.speed_x = random.choice((BALL_SPEED_X, -BALL_SPEED_X))
        self.speed_y = random.choice((BALL_SPEED_Y, -BALL_SPEED_Y))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Check collision with walls
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed_y = -self.speed_y
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.reset()

# Create sprites
all_sprites = pygame.sprite.Group()
paddle1 = Paddle(20, WINDOW_HEIGHT // 2)
paddle2 = Paddle(WINDOW_WIDTH - 20, WINDOW_HEIGHT // 2)

# AI-controlled paddle
ai_paddle = Paddle(WINDOW_WIDTH - 20, WINDOW_HEIGHT // 2)
all_sprites.add(ai_paddle)

ball = Ball()
all_sprites.add(paddle1, paddle2, ball)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # AI movement
    if ball.speed_x > 0:
        if ball.rect.centery < ai_paddle.rect.centery:
            ai_paddle.rect.y -= PADDLE_SPEED
        elif ball.rect.centery > ai_paddle.rect.centery:
            ai_paddle.rect.y += PADDLE_SPEED

    # Update game state
    all_sprites.update()

    # Check collision with paddles
    if pygame.sprite.collide_rect(ball, paddle1) or pygame.sprite.collide_rect(ball, paddle2):
        ball.speed_x = -ball.speed_x

    # Draw everything
    window.blit(background_image, (0, 0))  # Draw background image
    pygame.draw.line(window, WHITE, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT), 2)
    all_sprites.draw(window)

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()