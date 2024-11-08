import curses
import time
import math
import random

# Constants
PADDLE_HEIGHT = 5
PADDLE_WIDTH = 1
BALL_RADIUS = 2
PADDLE_CHAR = '|'
MAX_SCORE = 5
INITIAL_DELAY = 0.05  # Initial speed delay for the ball

# CPU behavior constants
CPU_ERROR_INTERVAL = 20  # seconds before CPU starts to occasionally miss the ball
CPU_ERROR_PROBABILITY = 0.2  # 20% chance CPU will "miss" after 20 seconds

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

def show_title_screen(stdscr):
    title_message = [
        "Welcome to 3D Sphere Soccer!",
        "",
        "Get ready to compete and score some goals!"
    ]
    instructions_screen(stdscr, title_message, timeout=3)

def show_instructions_screen(stdscr):
    instructions_message = [
        "Instructions:",
        "",
        "Goal: Score by hitting the ball past your opponent's paddle.",
        "The first player to reach 5 points wins!",
        "",
        "Controls:",
        " - Player 1: Use 'W' to move up and 'S' to move down",
        " - Player 2: Use 'Arrow Up' to move up and 'Arrow Down' to move down",
    ]
    instructions_screen(stdscr, instructions_message, timeout=5)

def loading_screen(stdscr):
    height, width = stdscr.getmaxyx()
    loading_message = "Get Ready for 3D Sphere Soccer!"
    stdscr.addstr(height // 2 - 2, width // 2 - len(loading_message) // 2, loading_message)
    stdscr.refresh()
    time.sleep(1)

    for i in range(3, 0, -1):
        stdscr.clear()
        countdown_message = f"{i}"
        stdscr.addstr(height // 2, width // 2, countdown_message)
        stdscr.refresh()
        time.sleep(1)

    stdscr.clear()
    stdscr.refresh()

def instructions_screen(stdscr, message, timeout):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    for idx, line in enumerate(message):
        stdscr.addstr(height // 2 - len(message) // 2 + idx, width // 2 - len(line) // 2, line)

    stdscr.refresh()
    time.sleep(timeout)

def pause_screen(stdscr):
    height, width = stdscr.getmaxyx()
    pause_message = "Game Paused. Press any key to continue."
    stdscr.addstr(height // 2, width // 2 - len(pause_message) // 2, pause_message)
    stdscr.refresh()
    stdscr.getch()

def select_mode(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(5, 5, "Select Mode:")
        stdscr.addstr(7, 5, "1 - Play against CPU")
        stdscr.addstr(8, 5, "2 - Play against Human")
        stdscr.addstr(10, 5, "Press 1 or 2: ")
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('1'):
            return "cpu"
        elif key == ord('2'):
            return "human"

def main_game(stdscr, mode):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)

    height, width = stdscr.getmaxyx()

    show_title_screen(stdscr)
    show_instructions_screen(stdscr)
    loading_screen(stdscr)

    paddle1_x, paddle1_y = 2, height // 2 - PADDLE_HEIGHT // 2
    paddle2_x, paddle2_y = width - 3, height // 2 - PADDLE_HEIGHT // 2
    ball_x, ball_y = width // 2, height // 2
    ball_dx, ball_dy = 1, 1
    score1, score2 = 0, 0

    speed_delay = INITIAL_DELAY
    speed_increase_factor = 0.95
    start_time = time.time()
    cpu_error_active = False

    while True:
        stdscr.clear()
        draw_paddle(stdscr, paddle1_x, paddle1_y)
        draw_paddle(stdscr, paddle2_x, paddle2_y)
        draw_sphere(stdscr, ball_x, ball_y, BALL_RADIUS)
        score_display = f"{score1} - {score2}"
        stdscr.addstr(1, width // 2 - len(score_display) // 2, score_display)

        key = stdscr.getch()
        if key == 27:  # ESC key to pause
            pause_screen(stdscr)

        if key == ord('w') and paddle1_y > 0:
            paddle1_y -= 1
        if key == ord('s') and paddle1_y + PADDLE_HEIGHT < height:
            paddle1_y += 1

        if time.time() - start_time > CPU_ERROR_INTERVAL:
            cpu_error_active = True

        if mode == 'cpu':
            if cpu_error_active and random.random() < CPU_ERROR_PROBABILITY:
                pass
            else:
                if paddle2_y + PADDLE_HEIGHT // 2 < ball_y and paddle2_y + PADDLE_HEIGHT < height:
                    paddle2_y += 1
                elif paddle2_y + PADDLE_HEIGHT // 2 > ball_y and paddle2_y > 0:
                    paddle2_y -= 1
        else:
            if key == curses.KEY_UP and paddle2_y > 0:
                paddle2_y -= 1
            if key == curses.KEY_DOWN and paddle2_y + PADDLE_HEIGHT < height:
                paddle2_y += 1

        ball_x += ball_dx
        ball_y += ball_dy

        if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= height:
            ball_dy *= -1

        if (paddle1_x + PADDLE_WIDTH >= ball_x - BALL_RADIUS and
                paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT):
            ball_dx *= -1
            speed_delay *= speed_increase_factor

        if (paddle2_x - PADDLE_WIDTH <= ball_x + BALL_RADIUS and
                paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT):
            ball_dx *= -1
            speed_delay *= speed_increase_factor

        if ball_x - BALL_RADIUS < 0:
            score2 += 1
            ball_x, ball_y = width // 2, height // 2
            speed_delay = INITIAL_DELAY
        elif ball_x + BALL_RADIUS >= width:
            score1 += 1
            ball_x, ball_y = width // 2, height // 2

        if score1 == MAX_SCORE or score2 == MAX_SCORE:
            winner = "Player 1" if score1 == MAX_SCORE else "Player 2"
            stdscr.clear()
            win_message = f"{winner} Wins!"
            stdscr.addstr(height // 2, width // 2 - len(win_message) // 2, win_message)
            stdscr.refresh()
            time.sleep(3)
            break

        stdscr.refresh()
        time.sleep(speed_delay)

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    mode = select_mode(stdscr)
    main_game(stdscr, mode)

curses.wrapper(main)
