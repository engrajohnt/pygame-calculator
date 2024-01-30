#create a pygame-based calculator that performs addition, subtraction, multiplication, division, square root, and square of numbers the operators should be buttons on screen i.e. use windows calculator as a guide
#the best calculator will be used as a case study for the next topic

import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Font
font = pygame.font.Font(None, 36)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Calculator")

# Calculator state
expression = ""
result = ""

# Function to draw buttons
def draw_button(x, y, width, height, text, color, action=None):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(text_surface, text_rect)

    # Check for button click
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if x < mouse_pos[0] < x + width and y < mouse_pos[1] < y + height:
        if mouse_click[0] == 1 and action is not None:
            action()

# Function to handle button clicks
def button_click(value):
    global expression
    if value == "=":
        try:
            global result
            result = str(eval(expression))
            expression = result
        except:
            expression = "Error"
    elif value == "C":
        expression = ""
    elif value == "sqrt":
        try:
            expression = str(math.sqrt(float(expression)))
        except:
            expression = "Error"
    elif value == "x^2":
        try:
            expression = str(float(expression) ** 2)
        except:
            expression = "Error"
    else:
        expression += str(value)

# Main loop
while True:
    screen.fill(WHITE)

    # Draw expression and result
    expression_surface = font.render(expression, True, BLACK)
    expression_rect = expression_surface.get_rect(midtop=(WIDTH / 2, 50))
    screen.blit(expression_surface, expression_rect)

    result_surface = font.render(result, True, BLACK)
    result_rect = result_surface.get_rect(midtop=(WIDTH / 2, 100))
    screen.blit(result_surface, result_rect)

    # Draw calculator buttons
    buttons = [
        ("7", 50, 200), ("8", 150, 200), ("9", 250, 200), ("/", 350, 200),
        ("4", 50, 300), ("5", 150, 300), ("6", 250, 300), ("*", 350, 300),
        ("1", 50, 400), ("2", 150, 400), ("3", 250, 400), ("-", 350, 400),
        ("0", 50, 500), (".", 150, 500), ("=", 250, 500), ("+", 350, 500),
        ("C", 50, 100), ("sqrt", 150, 100), ("x^2", 250, 100)
    ]

    for button in buttons:
        draw_button(button[1], button[2], 80, 80, button[0], GRAY, lambda b=button[0]: button_click(b))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
