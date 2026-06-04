import pygame
import random
from constants import *
from draw_utils import draw_board, draw_tokens, draw_dice, draw_turn_indicator

def roll_dice_with_animation(screen, current_player, tokens):
    dice_roll_sound = pygame.mixer.Sound('../assets/dice-142528.mp3')
    dice_roll_sound.play()  # Play dice rolling sound

    for _ in range(10):  # Show 10 frames of random dice values
        dice_value = random.randint(1, 6)
        draw_board(screen)
        draw_turn_indicator(screen, current_player)
        draw_tokens(screen, tokens)
        draw_dice(screen, dice_value)
        pygame.display.flip()
        pygame.time.delay(50)  # Short delay to create animation effect

    return random.randint(1, 6)  # Final roll value

def move_token_with_animation(screen, player, tokens, dice_value):
    # Identify tokens eligible for movement
    movable_tokens = []
    for i, position in enumerate(tokens[player]):
        if position == "Start" and dice_value == 6:
            movable_tokens.append(i)  # Tokens in "Start" can only move on a 6
        elif position != "Start" and position != FINISH:
            path = PATHS[player]
            idx = path.index(position) if position in path else -1
            if 0 <= idx + dice_value < len(path):
                movable_tokens.append(i)

    # If no tokens can be moved, return False
    if not movable_tokens:
        return False

    # Let the player choose a token if multiple are eligible
    chosen_token = prompt_token_selection(screen, player, tokens, movable_tokens, dice_value)

    # Move the chosen token
    if chosen_token is not None:
        token_idx = chosen_token
        path = PATHS[player]
        current_position = tokens[player][token_idx]

        if current_position == "Start":
            tokens[player][token_idx] = path[0]
        else:
            idx = path.index(current_position)
            for step in range(1, dice_value + 1):
                tokens[player][token_idx] = path[idx + step]
                draw_board(screen)
                draw_turn_indicator(screen, player)
                draw_tokens(screen, tokens)
                draw_dice(screen, dice_value)
                pygame.display.flip()
                pygame.time.delay(150)  # Smooth movement delay

        capture_token(tokens, player)
        return True

    return False  # If no valid choice was made

def prompt_token_selection(screen, player, tokens, movable_tokens, dice_value):
    """
    Display a prompt for the player to choose which token to move.
    If the player selects a token that is not allowed to move, show "Wrong move".
    The dice value remains visible during the selection.
    """
    running = True
    font = pygame.font.SysFont("Arial", 30)
    error_message = None  # To store the error message

    while running:
        screen.fill(WHITE)
        draw_board(screen)
        draw_tokens(screen, tokens)
        draw_dice(screen, dice_value)  # Redraw the dice to keep it visible

        # Display prompt
        text_surface = font.render(f"{player}'s Turn: Press a number to select a token", True, BLACK)
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 50))

        # Display error message if any
        if error_message:
            error_surface = font.render(error_message, True, BLACK)
            screen.blit(error_surface, (SCREEN_WIDTH // 2 - error_surface.get_width() // 2, 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in range(pygame.K_1, pygame.K_1 + len(movable_tokens)):
                    return movable_tokens[event.key - pygame.K_1]  # Return the selected token index
                else:
                    # Show "Wrong move" if the selected token is not allowed
                    error_message = "Wrong move! Choose a valid token."

    return None

def capture_token(tokens, player):
    # Dynamically determine the opponent's color
    opponents = [color for color in tokens.keys() if color != player]
    for opponent in opponents:
        for i, player_token in enumerate(tokens[player]):
            if player_token == "Start" or player_token == FINISH:
                continue  # Skip tokens that are still in home or have finished

            for j, opponent_token in enumerate(tokens[opponent]):
                if player_token == opponent_token and player_token not in SAFE_ZONES:
                    tokens[opponent][j] = "Start"  # Send opponent's token back to home
                    return True  # A capture happened
    return False  # No capture occurred

def ai_choose_token(tokens, player, dice_value):
    """
    AI logic to choose which token to move.
    """
    movable_tokens = []
    for i, position in enumerate(tokens[player]):
        if position == "Start" and dice_value == 6:
            return i  # Always move out of start if possible
        elif position != "Start" and position != FINISH:
            path = PATHS[player]
            idx = path.index(position) if position in path else -1
            if 0 <= idx + dice_value < len(path):
                movable_tokens.append(i)
    
    if movable_tokens:
        return random.choice(movable_tokens)  # Randomly choose among movable tokens
    return None  # No valid move

def move_ai_token_with_animation(screen, player, tokens, dice_value):
    """
    Move the AI's token along the path with animation.
    """
    token_idx = ai_choose_token(tokens, player, dice_value)
    if token_idx is None:
        return False  # No valid move

    path = PATHS[player]
    current_position = tokens[player][token_idx]

    if current_position == "Start":
        tokens[player][token_idx] = path[0]  # Move to the first position on the path
    else:
        idx = path.index(current_position)
        for step in range(1, dice_value + 1):
            tokens[player][token_idx] = path[idx + step]
            draw_board(screen)
            draw_turn_indicator(screen, player)
            draw_tokens(screen, tokens)
            draw_dice(screen, dice_value)
            pygame.display.flip()
            pygame.time.delay(150)  # Smooth movement delay

    capture_token(tokens, player)
    return True