# Sphere Soccer Duel

## Overview
**Sphere Soccer Duel** is a 2D Pong-style game played in the terminal where players control paddles to hit a ball back and forth. The goal is to score by passing the ball past your opponent's paddle. The first player to reach 5 points wins. The game offers two modes: one to play against another human player or against an AI opponent.

## Features
- Play against another player or AI.
- Dynamic ball speed increase after each paddle collision.
- Simple, text-based interface with terminal graphics.
- Option to pause the game using the ESC key.

## Controls
- **Player 1**: Use `W` to move up and `S` to move down.
- **Player 2**: Use the `Arrow Up` and `Arrow Down` keys to move up and down.
- **Pause**: Press `ESC` to pause the game. Press any key to resume.

## Installation
To run **Sphere Soccer Duel**, ensure you have Python 3.x and the `curses` library installed.

1. Clone the repository or download the game files.
2. Open a terminal and navigate to the folder containing `main.py`.
3. Run the game with the following command:
   ```bash
   python3 main.py

## How to Play
1. Upon starting the game, choose a game mode:
   - **1**: Play against the AI.
   - **2**: Play against another human player.
2. Use the appropriate controls to move your paddle and try to hit the ball past your opponent.
3. The first player to score 5 points wins.

### Game Mechanics
- **Paddles**: Move up or down to prevent the ball from passing you. Player 1 uses the 'W' and 'S' keys, while Player 2 uses the Arrow Up and Arrow Down keys.
- **Ball Movement**: The ball bounces off the top and bottom walls and changes direction when it collides with a paddle. After each collision, the ball’s speed gradually increases.
- **Scoring**: A point is scored when the ball passes the opponent's paddle. The first player to reach 5 points wins the match.
- **Pause**: Press the `ESC` key at any time to pause the game. Press any key to resume playing.

### Modes of Play
- **AI Mode**: In this mode, you will play against a computer-controlled opponent. The AI moves its paddle automatically, trying to block the ball from passing its side.
- **Human Mode**: In this mode, two players can play on the same machine, taking turns to control the paddles.
