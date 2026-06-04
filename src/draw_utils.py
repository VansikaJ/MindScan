import pygame
import math
from constants import *

def draw_star(screen, cx, cy, size=15):
    points = []
    for i in range(10):  # 10 points for a star
        angle = i * (2 * math.pi / 10) - math.pi / 2
        radius = size if i % 2 == 0 else size * 0.5
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        points.append((x, y))
    pygame.draw.polygon(screen, YELLOW, points)

def draw_board(screen):
    screen.fill(WHITE)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

    # Colored corners (home areas)
    corner_size = 6
    pygame.draw.rect(screen, RED, pygame.Rect(0, 0, corner_size * CELL_SIZE, corner_size * CELL_SIZE))
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 9 * CELL_SIZE, corner_size * CELL_SIZE, corner_size * CELL_SIZE))
    pygame.draw.rect(screen, GREEN, pygame.Rect(9 * CELL_SIZE, 0, corner_size * CELL_SIZE, corner_size * CELL_SIZE))
    pygame.draw.rect(screen, YELLOW, pygame.Rect(9 * CELL_SIZE, 9 * CELL_SIZE, corner_size * CELL_SIZE, corner_size * CELL_SIZE))

    # Draw safe zones and center
    pygame.draw.rect(screen, CENTER_COLOR, pygame.Rect(6 * CELL_SIZE, 6 * CELL_SIZE, 3 * CELL_SIZE, 3 * CELL_SIZE))

    for sx, sy in SAFE_ZONES:
        cx, cy = sx * CELL_SIZE + CELL_SIZE // 2, sy * CELL_SIZE + CELL_SIZE // 2
        draw_star(screen, cx, cy)

def draw_tokens(screen, tokens):
    font = pygame.font.SysFont("Arial", 20)  # Font for token numbers
    for player, positions in tokens.items():
        color = {"RED": RED, "BLUE": BLUE, "GREEN": GREEN, "YELLOW": YELLOW}[player]
        for i, position in enumerate(positions):
            if position == "Start":
                x, y = HOME_POSITIONS[player][i]
            elif isinstance(position, tuple):
                x, y = position
            else:
                continue
            cx, cy = x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(screen, BLACK, (cx, cy), 18)
            pygame.draw.circle(screen, color, (cx, cy), 15)
            
            # Draw token number on the token
            text = font.render(str(i + 1), True, BLACK)
            text_rect = text.get_rect(center=(cx, cy))
            screen.blit(text, text_rect)

def draw_dice(screen, dice_value):
    dice_size = 100
    dice_x = (SCREEN_WIDTH - dice_size) // 2
    dice_y = (SCREEN_HEIGHT - dice_size) // 2

    pygame.draw.rect(screen, WHITE, (dice_x, dice_y, dice_size, dice_size))
    pygame.draw.rect(screen, BLACK, (dice_x, dice_y, dice_size, dice_size), 2)

    dice_font = pygame.font.SysFont("Arial", 50)
    text = dice_font.render(str(dice_value), True, BLACK)
    text_x = dice_x + (dice_size - text.get_width()) // 2
    text_y = dice_y + (dice_size - text.get_height()) // 2
    screen.blit(text, (text_x, text_y))

def draw_turn_indicator(screen, current_player):
    turn_text = f"Turn: {current_player}"
    font = pygame.font.SysFont("Arial", 30)
    text_surface = font.render(turn_text, True, BLACK)
    screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT - 50))