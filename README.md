# Asteroids

Arcade-style Asteroids game for 1–2 players.

## Features
- 1–2 players
- Difficulty selection
- Score keeping
- End screen

## Requirements
- Python 3.10+
- pygame
- Optional: uv (package manager)

## Install

Using uv:
```bash
uv venv
uv pip install -e .
# or ensure pygame is installed:
uv pip install pygame

Using pip:

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # or: pip install pygame

Run
Using uv:

uv run python main.py 

Using Python:

python main.py

Controls:

Player 1: WASD + Space
Player 2: Arrow Keys + Left Ctrl