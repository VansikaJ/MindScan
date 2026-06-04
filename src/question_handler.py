import csv
import pygame
from constants import *
from draw_utils import draw_board


def load_questions(filename):
    """
    Load questions from a CSV file into a list of dictionaries.
    """
    questions = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            question_id, question_text, disorder_id = row
            questions.append({
                "id": int(question_id.strip('"')),
                "text": question_text.strip('"'),
                "disorder_id": int(disorder_id.strip('"'))
            })
    return questions

def load_answers(filename):
    """
    Load answers from a CSV file into a list of dictionaries.
    """
    answers = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            answer_id, question_id, answer_text, score = row
            answers.append({
                "id": int(answer_id.strip('"')),
                "question_id": int(question_id.strip('"')),
                "text": answer_text.strip('"'),
                "score": int(score.strip('"'))
            })
    return answers

def wrap_text(text, font, max_width):
    """
    Wrap text into multiple lines if it exceeds the max_width.
    """
    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        # Check if adding the next word exceeds the max width
        test_line = current_line + ' ' + word if current_line else word
        test_width, _ = font.size(test_line)
        if test_width <= max_width:
            current_line = test_line
        else:
            # If the line exceeds the width, start a new line
            lines.append(current_line)
            current_line = word

    # Add the last line
    if current_line:
        lines.append(current_line)

    return lines

def ask_question(screen, question, answers):
    """
    Display a question in a dialog box with radio buttons for the user to select their response.
    Returns the selected response as a dictionary.
    """
    font = pygame.font.SysFont("Arial", 17)
    small_font = pygame.font.SysFont("Arial", 17)
    responses = ["Never", "Rarely", "Sometimes", "Often", "Always"]
    selected_response = None
    running = True

    # Dialog box dimensions
    box_width = 600
    box_height = 300  # Increased height to accommodate multi-line questions
    box_x = (SCREEN_WIDTH - box_width) // 2
    box_y = (SCREEN_HEIGHT - box_height) // 2

    # Wrap the question text into multiple lines
    wrapped_question = wrap_text(question["text"], font, box_width - 40)  # 40px padding

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the user clicked on a response
                mouse_pos = pygame.mouse.get_pos()
                for i, response in enumerate(responses):
                    response_rect = pygame.Rect(box_x + 50, box_y + 90 + i * 40, 200, 30)  # Adjusted Y position
                    if response_rect.collidepoint(mouse_pos):
                        selected_response = {
                            "question_id": question["id"],
                            "answer_text": response,
                            "score": next(a["score"] for a in answers if a["question_id"] == question["id"] and a["text"] == response)
                        }
                        running = False

        # Draw the background
        screen.fill(WHITE)
        draw_board(screen)  # Draw the Ludo board in the background

        # Draw the dialog box
        pygame.draw.rect(screen, CENTER_COLOR, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, BLACK, (box_x, box_y, box_width, box_height), 2)

        # Draw the question text (multi-line)
        y_offset = box_y + 20
        for line in wrapped_question:
            question_text = font.render(line, True, BLACK)
            screen.blit(question_text, (box_x + 20, y_offset))
            y_offset += 30  # Move down for the next line

        # Draw the response options
        for i, response in enumerate(responses):
            response_rect = pygame.Rect(box_x + 50, box_y + 90 + i * 40, 200, 30)
            pygame.draw.rect(screen, BLACK, response_rect, 2)
            response_text = small_font.render(response, True, BLACK)
            screen.blit(response_text, (response_rect.x + 10, response_rect.y + 5))

        pygame.display.flip()

    return selected_response