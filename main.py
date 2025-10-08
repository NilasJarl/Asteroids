import pygame
from enum import Enum
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from uielement import UIElement


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    GAME = 1
    GAMETWO = 2
    END = 3


def title_screen(screen):
    op_btn = UIElement(
        center_position=(640, 300),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="One Player",
        action=GameState.GAME,
    )
    tp_btn = UIElement(
        center_position=(640, 400),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Two Player",
        action=GameState.GAMETWO,
    )
    quit_btn = UIElement(
        center_position=(640, 500),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
     #time keepking
    clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroidsfield = AsteroidField()
    buttons = [op_btn, tp_btn, quit_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
        dt = clock.tick(120) / 1000

def game_screen(screen, num_players):

    #time keepking
    clock = pygame.time.Clock()
    dt = 0

    font = pygame.font.SysFont("Arial", 24)

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)


    #Initiate the players in the middel of the screen
    score = 0
    score_two = 0
    player_alive = True
    player_two_alive = False
    player = Player(1, SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 + 50)
    if num_players >= 2:
        player_two_alive = True
        player_two = Player(2, SCREEN_WIDTH / 2 + 50, SCREEN_HEIGHT / 2 -50)

    asteroidsfield = AsteroidField()

    #game loop
    while True:
        for event in pygame.event.get(): #Stops the loop if the windows is closed
            if event.type == pygame.QUIT:
                return
            
        screen.fill(BLACK) #turns screen black.
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player):
                player_alive = False
                player.kill()
            if num_players >= 2:
                if asteroid.collision(player_two):
                    player_two_alive = False
                    player_two.kill()
            for shot in shots:
                if asteroid.collision(shot):
                    if shot.color == WHITE:
                        score += 100
                    elif shot.color == RED:
                        score_two += 100
                    shot.kill()
                    asteroid.split()
        if not player_alive and not player_two_alive:
            print("Game over!")
            print(f"Player score was: {score}")
            if num_players >= 2:
                print(f"Player two score was: {score_two}")
            return GameState.END, score, score_two
        player_score = font.render(f"{score}", True, WHITE)
        screen.blit(player_score, (5, 0))
        if num_players >= 2:
            player_two_score = font.render(f"{score_two}",True, RED)
            screen.blit(player_two_score, (5, 25))
            

        pygame.display.flip()
        dt = clock.tick(120) / 1000


def end_screen(screen, num_players, score, score_two):
    
    game_over = UIElement(
        center_position=(640, 200),
        font_size=80,
        bg_rgb=RED,
        text_rgb=WHITE,
        text="GAME OVER!",
        action=None,
    )
    player_score = UIElement(
        center_position=(640, 300),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text=f"Player One Score was: {score}",
        action=None,
    )
    quit_btn = UIElement(
        center_position=(640, 500),
        font_size=50,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    buttons = [game_over, player_score, quit_btn]
    if num_players >= 2:    
        player_two_score = UIElement(
            center_position=(640, 400),
            font_size=30,
            bg_rgb=BLACK,
            text_rgb=RED,
            text=f"Player Two score was: {score_two}",
            action=None,
        )
        buttons.append(player_two_score)
    

     #time keepking
    clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroidsfield = AsteroidField()


    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)
        updatable.update(dt)

        for draw in drawable:
            draw.draw(screen)
       
        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
        dt = clock.tick(120) / 1000


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #sets the screen width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = GameState.TITLE
    num_players = 1
    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.GAME:
            game_state, score, score_two = game_screen(screen, num_players)
        
        if game_state == GameState.GAMETWO:
            num_players = 2
            game_state, score, score_two = game_screen(screen, num_players)

        if game_state == GameState.END:
            game_state = end_screen(screen, num_players, score, score_two)

        if game_state == GameState.QUIT:
            pygame.quit()
            return





if __name__ == "__main__":
    main()