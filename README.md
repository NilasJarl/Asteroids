# Asteroids

Arcade-style Asteroids game for 1–2 players.
Originally made a part of the guided project for Boot.Dev
As part of the first personal project I decided to expand on the scope of the.
I had already added score keeping and two player mode for fun one my own.
But I challenged myself to add a menu system with various options which I've so far succeded with! :D
On my to do list is:
- permanent and/or temporay buffs/enhancements
- time based difficulty scaling

## Features
- 1–2 players
- Resolution selection
- Difficulty selection
- Score keeping
- End screen

## Controls
Mouse for menu navigation

In game:
Player 1: WASD + Space
Player 2: Arrow Keys + Left Ctrl

## Resolutions selection
Allows for switching between the following windowed resolutions:
- 1280*720
- 1920*1080
- 2556*1440
_Note: Increasing resolution will also increase asteroids spawn rate to compensate for the bigger play area_

## Defficulty selection
Switch between following difficulties:
- Easy (0.9 factored spawn rate and asteroids speed)
- Normal (1.0 factored spawn rate and asteroids speed)
- Hard (1.1 factored spawn rate and asteroids speed)
- Insanity (1.5 factored spawn rate and asteroids speed)

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
```

## Run
```bash
Using uv:

uv run python main.py 

Using Python:

python main.py

