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
