import curses
import time
import math

# Constants
PADDLE_HEIGHT = 5
PADDLE_WIDTH = 1
BALL_RADIUS = 2
PADDLE_CHAR = '|'
MAX_SCORE = 5
INITIAL_DELAY = 0.05
SPEED_INCREASE_FACTOR = 0.95


def main_game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)

    height, width = stdscr.getmaxyx()

    # Initial positions
    paddle1_x, paddle1_y = 2, height // 2 - PADDLE_HEIGHT // 2
    paddle2_x, paddle2_y = width - 3, height // 2 - PADDLE_HEIGHT // 2
    ball_x, ball_y = width // 2, height // 2
    ball_dx, ball_dy = 1, 1
    score1, score2 = 0, 0
    speed_delay = INITIAL_DELAY
def instructions_screen(stdscr, message, timeout=5):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    for idx, line in enumerate(message):
        stdscr.addstr(height // 2 - len(message) // 2 + idx, width // 2 - len(line) // 2, line)
    stdscr.refresh()
    time.sleep(timeout)

def show_instructions(stdscr):
    title_message = ["PaddleSphere Showdown"]
    instructions_screen(stdscr, title_message, timeout=3)

    aim_message = [
        "Welcome to 3D Sphere Soccer!",
        "Goal: Score by hitting the ball past your opponent's paddle.",
        "The first player to reach 5 points wins!"
    ]
    instructions_screen(stdscr, aim_message, timeout=4)

    controls_message = [
        "Controls:",
        "- Player 1: Use 'W' to move up and 'S' to move down",
        "- Player 2: Use 'Arrow Up' and 'Arrow Down' to move",
    ]
    instructions_screen(stdscr, controls_message, timeout=4)

def choose_mode(stdscr):
    choice_message = [
        "Choose Game Mode:",
        "1 - Play against AI",
        "2 - Play against another player"
    ]
    instructions_screen(stdscr, choice_message, timeout=0)
    while True:
        choice = stdscr.getch()
        if choice == ord('1'):
            return 'AI'
        elif choice == ord('2'):
          return'Human'
        
def draw_paddle(stdscr, x, y):
    for i in range(PADDLE_HEIGHT):
        stdscr.addch(y + i, x, PADDLE_CHAR)

def draw_sphere(stdscr, x, y, radius):
    for angle in range(0, 360, 10):
        radians = math.radians(angle)
        sphere_x = int(radius * math.cos(radians)) + x
        sphere_y = int(radius * math.sin(radians) / 2) + y
        if 0 <= sphere_x < curses.COLS and 0 <= sphere_y < curses.LINES:
            stdscr.addch(sphere_y, sphere_x, 'o')

def draw_score(stdscr, score1, score2, width):
    score_display = f"{score1} - {score2}"
    stdscr.addstr(1, width // 2 - len(score_display) // 2, score_display)