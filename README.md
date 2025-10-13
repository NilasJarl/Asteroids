# Asteroids

Arcade-style Asteroids game for 1–2 players.  
Originally made a part of the guided project for Boot.dev.  
As part of the first personal project I decided to expand on the functionality of the game.  
I had already added score keeping and two player mode for fun on my own.  
But I challenged myself to add a menu system with various options which I've so far succeded with! :D  
I have added the following functionality to the original game:  
- Two player mode
- Score keeping
- Menu system
- Resolution selection (with increased spawn rate bassed on increasing resolution)
- Difficulty selection  
- Temporay buffs    
On my to do list is:
- Time based difficulty scaling

## Features
- Windowed arcade game
- 1–2 players
- Resolution selection
- Difficulty selection
- Temporay buffs  
- Score keeping
- End screen

## Controls
Mouse for menu navigation

In game:  
Player 1: Movement: WASD + Fire: Space  
Player 2: Movement: Arrow Keys + Fire: Left Ctrl  

## Resolution selection
Allows for switching between the following windowed resolutions:
- 1280*720
- 1920*1080
- 2560*1440  
_Note: Increasing resolution will also increase asteroids spawn rate to compensate for the bigger play area_

## Difficulty selection
Switch between following difficulties:
- Easy (0.9 factored asteroid spawn rate and asteroids speed)
- Normal (1.0 factored asteroid spawn rate and asteroids speed)
- Hard (1.1 factored asteroid spawn rate and asteroids speed)
- Insanity (1.5 factored asteroid spawn rate and asteroids speed)

## Temporay buffs
Three buff type, shot or fly into the coloroed Asteroids to get them:  
- Multishot, shot three shots per shot in a fan shape, given by Red Asteroids
- Machinegun, triple the rate of fire, given by Blue Asteroids
- Invulnerability, Unable to die, given by Green Asteroids  
_Note: Not points will be given for asteroids destroyed by hitting them with ship while invulnerable_

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
```
Using pip:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # or: pip install pygame
```

## Run
Using uv:
```bash
uv run python main.py 
```
  
Using Python:
```bash
python main.py
```


