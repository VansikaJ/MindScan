import pygame
import random
from constants import *
from draw_utils import draw_board, draw_tokens, draw_dice, draw_turn_indicator
from game_logic import roll_dice_with_animation, move_token_with_animation, ai_choose_token, move_ai_token_with_animation
from question_handler import load_questions, load_answers, ask_question
import csv
import tkinter as tk
from tkinter import messagebox

def choose_player_colors():
    available_colors = ["Red", "Blue", "Green", "Yellow"]
    print("Available colors:", ", ".join(available_colors))
    human_color = input("Choose your color: ").capitalize()
    while human_color not in available_colors:
        print("Invalid choice. Please choose from:", ", ".join(available_colors))
        human_color = input("Choose your color: ").capitalize()
    available_colors.remove(human_color)
    ai_color = random.choice(available_colors)
    return human_color, ai_color

def choose_player_colors_gui(screen):
    """
    Display a centered box with available colors and let the user select one.
    Returns the selected color for the human player and a random color for the AI.
    """
    available_colors = ["RED", "BLUE", "GREEN", "YELLOW"]
    font = pygame.font.SysFont("Arial", 25)
    small_font = pygame.font.SysFont("Arial", 16)
    box_width = 400
    box_height = 300
    box_x = (SCREEN_WIDTH - box_width) // 2
    box_y = (SCREEN_HEIGHT - box_height) // 2
    color_rects = []  # Stores the rectangles for each color option

    # Create rectangles for each color option
    for i, color in enumerate(available_colors):
        rect = pygame.Rect(box_x + 50, box_y + 55 + i * 60, 300, 50)
        color_rects.append((rect, color))

    selected_color = None
    while selected_color is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the user clicked on a color
                mouse_pos = pygame.mouse.get_pos()
                for rect, color in color_rects:
                    if rect.collidepoint(mouse_pos):
                        selected_color = color
                        break

        # Draw the background
        screen.fill(WHITE)
        draw_board(screen)  # Draw the Ludo board in the background

        # Draw the selection box
        pygame.draw.rect(screen, CENTER_COLOR, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, BLACK, (box_x, box_y, box_width, box_height), 2)

        # Draw the title
        title_text = font.render("Choose Your Color", True, BLACK)
        screen.blit(title_text, (box_x + (box_width - title_text.get_width()) // 2, box_y + 15))

        # Draw the color options
        for rect, color in color_rects:
            pygame.draw.rect(screen, eval(color), rect)  # Use eval to convert color name to its value
            text = small_font.render(color, True, BLACK)
            screen.blit(text, (rect.x + 10, rect.y + 15))

        pygame.display.flip()

    # Remove the selected color from available colors for the AI
    available_colors.remove(selected_color)
    ai_color = random.choice(available_colors)

    return selected_color, ai_color

def choose_disorder_type(screen):
    """
    Display a dialog box to choose between Learning Disorder Detection and Mental Health Disorder Detection.
    Returns "Learning" or "Mental Health".
    """
    font = pygame.font.SysFont("Arial", 25)
    small_font = pygame.font.SysFont("Arial", 17)
    box_width = 500
    box_height = 300
    box_x = (SCREEN_WIDTH - box_width) // 2
    box_y = (SCREEN_HEIGHT - box_height) // 2
    options = ["Learning Disorder Detection", "Mental Health Disorder Detection"]
    option_rects = []  # Stores the rectangles for each option

    # Create rectangles for each option
    for i, option in enumerate(options):
        rect = pygame.Rect(box_x + 50, box_y + 80 + i * 80, 400, 50)
        option_rects.append((rect, option))

    selected_option = None
    while selected_option is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the user clicked on an option
                mouse_pos = pygame.mouse.get_pos()
                for rect, option in option_rects:
                    if rect.collidepoint(mouse_pos):
                        selected_option = option
                        break

        # Draw the background
        screen.fill(WHITE)
        draw_board(screen)  # Draw the Ludo board in the background

        # Draw the selection box
        pygame.draw.rect(screen, CENTER_COLOR, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, BLACK, (box_x, box_y, box_width, box_height), 2)

        # Draw the title
        title_text = font.render("Choose Disorder Detection Type", True, BLACK)
        screen.blit(title_text, (box_x + (box_width - title_text.get_width()) // 2, box_y + 20))

        # Draw the options
        for rect, option in option_rects:
            pygame.draw.rect(screen, BLACK, rect, 2)
            text = small_font.render(option, True, BLACK)
            screen.blit(text, (rect.x + 10, rect.y + 15))

        pygame.display.flip()

    return "Learning" if selected_option == "Learning Disorder Detection" else "Mental Health"

def map_responses_to_disorders(user_responses_file, questions_file, disorders_file, disorder_type):
    """
    Map user responses to disorders and find disorders where:
    - All questions have 'Often' or 'Always' responses.
    - Some questions have 'Sometimes', 'Often', or 'Always' responses (excluding those already in the first list).
    """
    # Load questions and group them by disorder
    questions_by_disorder = {}
    with open(questions_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            question_id, question_text, disorder_id = row
            disorder_id = int(disorder_id.strip('"'))
            question_id = int(question_id.strip('"'))
            if disorder_id not in questions_by_disorder:
                questions_by_disorder[disorder_id] = []
            questions_by_disorder[disorder_id].append(question_id)

    # Load disorders
    disorders = {}
    with open(disorders_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            disorder_id, disorder_name = row
            disorders[int(disorder_id.strip('"'))] = disorder_name.strip('"')

    # Load user responses
    user_responses = {}
    with open(user_responses_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            question_id, answer_text, score = row
            question_id = int(question_id.strip('"'))
            answer_text = answer_text.strip('"')
            user_responses[question_id] = answer_text

    # Filter disorders based on the selected type
    if disorder_type == "Learning":
        disorder_ids = range(1, 17)  # Learning Disorders (1-16)
    else:
        disorder_ids = range(17, 26)  # Mental Health Disorders (17-25)

    # Find disorders where all questions have 'Often' or 'Always' responses
    disorders_with_all_high_responses = []
    for disorder_id in disorder_ids:
        question_ids = questions_by_disorder.get(disorder_id, [])
        if not question_ids:
            continue
        all_high_responses = all(
            user_responses.get(question_id) in ["Often", "Always"]
            for question_id in question_ids
        )
        if all_high_responses:
            disorders_with_all_high_responses.append(disorders[disorder_id])

    # Find disorders where some questions have 'Sometimes', 'Often', or 'Always' responses
    disorders_with_some_high_responses = []
    for disorder_id in disorder_ids:
        # Skip disorders that are already in the "all high responses" list
        if disorders[disorder_id] in disorders_with_all_high_responses:
            continue

        question_ids = questions_by_disorder.get(disorder_id, [])
        if not question_ids:
            continue
        some_high_responses = any(
            user_responses.get(question_id) in ["Sometimes", "Often", "Always"]
            for question_id in question_ids
        )
        if some_high_responses:
            disorders_with_some_high_responses.append(disorders[disorder_id])

    return disorders_with_all_high_responses, disorders_with_some_high_responses

def show_results_dialog(disorders_with_all_high_responses, disorders_with_some_high_responses):
    """
    Display the results in a tkinter dialog box.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prepare the message
    
    if disorders_with_all_high_responses:
        message = "Higher possibility of having the following disorders:\n"
        for disorder in disorders_with_all_high_responses:
            message += f"- {disorder}\n"
    #else:
        #message += "No disorders meet the criteria.\n"

    
    if disorders_with_some_high_responses:
        message += "\nLower possibility of having the following disorders:\n"
        for disorder in disorders_with_some_high_responses:
            message += f"- {disorder}\n"
    #else:
        #message += "No disorders meet the criteria.\n"

    # Show the message box
    messagebox.showinfo("Results", message)

    root.destroy()

def main():
    # Initialize Pygame
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ludo Game with AI and Questions")
    clock = pygame.time.Clock()

    # Play background music
    bg_music = pygame.mixer.Sound('../assets/puzzle-game-bright-casual-video-game-music-249202.mp3')
    bg_music.play(loops=-1)

    # Choose colors for human and AI players using the GUI
    human_color, ai_color = choose_player_colors_gui(screen)
    print(f"Human player: {human_color}, AI player: {ai_color}")

    # Choose disorder type (Learning or Mental Health)
    disorder_type = choose_disorder_type(screen)
    print(f"Selected disorder type: {disorder_type}")

    # Load questions and answers
    questions = load_questions("../data/questions_output.txt")
    answers = load_answers("../data/answers_output.txt")

    # Filter questions based on the selected disorder type
    if disorder_type == "Learning":
        questions = [q for q in questions if 1 <= q["id"] <= 27]  # Learning Disorders (1-27)
    else:
        questions = [q for q in questions if 28 <= q["id"] <= 47]  # Mental Health Disorders (28-47)

    question_index = 0  # Track which question to ask next

    # Initialize game state
    running = True
    tokens = {human_color: ["Start"] * 4, ai_color: ["Start"] * 4}
    current_player = human_color
    dice_value = 1

    # Open a file to save user responses
    with open("user_responses.txt", mode='w') as response_file:
        response_file.write("Question ID,Answer Text,Score\n")  # Header for the file

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break  # Exit the game loop
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and current_player == human_color:
                    dice_value = roll_dice_with_animation(screen, current_player, tokens)
                    moved = move_token_with_animation(screen, current_player, tokens, dice_value)

                    # Ask a question only if the dice value is not 6 (i.e., turn is shifting to AI)
                    if dice_value != 6 and question_index < len(questions):
                        question = questions[question_index]
                        response = ask_question(screen, question, answers)
                        if response:
                            # Save the response to the file
                            response_file.write(f"{response['question_id']},{response['answer_text']},{response['score']}\n")
                            question_index += 1  # Move to the next question

                    # Switch to AI if the user didn't roll a 6 or couldn't move
                    if not moved or dice_value != 6:
                        current_player = ai_color

            if current_player == ai_color and running:
                pygame.time.delay(1000)  # Simulate thinking time
                dice_value = roll_dice_with_animation(screen, current_player, tokens)
                moved = move_ai_token_with_animation(screen, ai_color, tokens, dice_value)

                # Switch back to the human player if the AI didn't roll a 6 or couldn't move
                if not moved or dice_value != 6:
                    current_player = human_color

            # Draw game elements
            draw_board(screen)
            draw_turn_indicator(screen, current_player)
            draw_tokens(screen, tokens)
            draw_dice(screen, dice_value)
            pygame.display.flip()
            clock.tick(30)

    pygame.quit()

    # Map responses to disorders and display results
    disorders_with_all_high_responses, disorders_with_some_high_responses = map_responses_to_disorders(
        "user_responses.txt",
        "../data/questions_output.txt",
        "../data/disorders_output.txt",
        disorder_type
    )

    # Show the results in a tkinter dialog box
    show_results_dialog(disorders_with_all_high_responses, disorders_with_some_high_responses)

if __name__ == "__main__":
    main()