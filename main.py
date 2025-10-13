import pygame
from enum import Enum
from constants import *
from player import Player, Buff
from asteroid_and_buff import Asteroid, Buffoid
from asteroidfield_and_buff_field import AsteroidField
from shot import Shot
from uielement import UIElement

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    GAME = 1
    GAMETWO = 2
    END = 3
    MENU = 4



class Resolution(Enum):
    LOW = 720
    MED = 1080
    HIGH = 1440

class Difficulty(Enum):
    EASY = 0.9
    NORMAL = 1
    HARD = 1.1
    INSANE = 1.5 


def title_screen(screen, difficulty):
    op_btn = UIElement(
        center_position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="One Player",
        action=GameState.GAME,
    )
    tp_btn = UIElement(
        center_position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Two Player",
        action=GameState.GAMETWO,
    )
    menu_btn = UIElement(
        center_position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Settings",
        action=GameState.MENU,
    )
    quit_btn = UIElement(
        center_position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200),
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
    AsteroidField.containers = (updatable,)

    asteroidsfield = AsteroidField(SCREEN_WIDTH, SCREEN_HEIGHT, difficulty.value)
    buttons = [op_btn, tp_btn, menu_btn, quit_btn]

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
        dt = clock.tick(60) / 1000
def menu_screen(screen, difficulty):
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    res = UIElement(
        center_position=(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 200),
        font_size=40,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Select Resolution:",
        action=None,
    )
    low_res = UIElement(
        center_position=(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2 - 250),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="1280*720",
        action=Resolution.LOW,
    )
    med_res = UIElement(
        center_position=(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2 - 200),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="1920*1080",
        action=Resolution.MED,
    )
    high_res = UIElement(
        center_position=(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2  - 150),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="2560*1440",
        action=Resolution.HIGH,
    )
    dif = UIElement(
        center_position=(SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 ),
        font_size=40,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Select Difficulty:",
        action=None,
    )
    dif_easy = UIElement(
        center_position=(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2 - 75),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Easy",
        action=Difficulty.EASY,
    )
    dif_nor = UIElement(
        center_position=(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2 - 25),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Normal",
        action=Difficulty.NORMAL,
    )
    dif_hard = UIElement(
        center_position=(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2  + 25),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Hard",
        action=Difficulty.HARD,
    )
    dif_isn = UIElement(
        center_position=(SCREEN_WIDTH / 2 + 150, SCREEN_HEIGHT / 2  + 75),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Insanity",
        action=Difficulty.INSANE,
    )
    back_btn = UIElement(
        center_position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200),
        font_size=50,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Back",
        action=GameState.TITLE,
    )
     #time keepking
    clock = pygame.time.Clock()
    dt = 0
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    match SCREEN_HEIGHT:
        case 720:
            low_res.set_text_color(RED)
        case 1080:
            med_res.set_text_color(RED)
        case 1440:
            high_res.set_text_color(RED)

    match difficulty:
        case Difficulty.EASY:
            dif_easy.set_text_color(RED)
        case Difficulty.NORMAL:
            dif_nor.set_text_color(RED)
        case Difficulty.HARD:
            dif_hard.set_text_color(RED)
        case Difficulty.INSANE:
            dif_isn.set_text_color(RED)


    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroidsfield = AsteroidField(SCREEN_WIDTH, SCREEN_HEIGHT, difficulty.value)

    menu_buttons = [res, low_res, med_res, high_res,dif, dif_easy, dif_nor, dif_hard, dif_isn, back_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)
        for button in menu_buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                match ui_action:
                    case GameState.TITLE:
                       return ui_action, screen, difficulty 
                    case Resolution.LOW:
                        SCREEN_WIDTH = 1280
                        SCREEN_HEIGHT = 720
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    case Resolution.MED:
                        SCREEN_WIDTH = 1920
                        SCREEN_HEIGHT = 1080
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    case Resolution.HIGH:
                        SCREEN_WIDTH = 2560
                        SCREEN_HEIGHT = 1440
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    case Difficulty.EASY | Difficulty.NORMAL | Difficulty.HARD | Difficulty.INSANE:    
                        difficulty = ui_action
                return GameState.MENU, screen, difficulty        
            button.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def game_screen(screen, num_players, difficulty):

    #time keepking
    clock = pygame.time.Clock()
    dt = 0

    font = pygame.font.SysFont("Arial", 24)

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    buffs = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Buffoid.containers = (buffs, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)


    #Initiate the players in the middel of the screen
    score = 0
    score_two = 0
    player_alive = True
    player_two_alive = False
    if num_players == 1:
        player = Player(1, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    elif num_players >= 2:
        player = Player(1, SCREEN_WIDTH / 2 -25, SCREEN_HEIGHT / 2)
        player_two_alive = True
        player_two = Player(2, SCREEN_WIDTH / 2 + 25, SCREEN_HEIGHT / 2)

    asteroidsfield = AsteroidField(SCREEN_WIDTH, SCREEN_HEIGHT, difficulty.value, num_players)

    #game loop
    while True:
        for event in pygame.event.get(): #Stops the loop if the windows is closed
            if event.type == pygame.QUIT:
                return GameState.QUIT, score, score_two
            
        screen.fill(BLACK) #turns screen black.
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)
        for asteroid in asteroids:
            if player_alive and asteroid.collision(player):
                if player.buff == Buff.INVULNERABILITY:
                    asteroid.split()
                else:
                    player_alive = False
                    player.kill()
            if player_two_alive and asteroid.collision(player_two):
                if player_two.buff == Buff.INVULNERABILITY:
                    asteroid.split()
                else:
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
        for buff in buffs:
            if player_alive and buff.collision(player):
                player.buff_player(buff.hit())
                buff.kill()
            if player_two_alive and buff.collision(player_two):
                player_two.buff_player(buff.hit())
                buff.kill()
            for shot in shots:
                if buff.collision(shot):
                    if shot.color == WHITE:
                        player.buff_player(buff.hit())
                    elif shot.color == RED:
                        player_two.buff_player(buff.hit())
                    shot.kill()
                    buff.kill()
        if not player_alive and not player_two_alive:
            print("Game over!")
            print(f"Player score was: {score}")
            if num_players >= 2:
                print(f"Player two score was: {score_two}")
            return GameState.END, score, score_two
        player_score = f"{score}"
        if player.buff is not None and player_alive:
            player_score += f" {player.buff.value} {player.buff_timer:.0f}"
        screen.blit(font.render(player_score, True, WHITE), (5, 0))
        if num_players >= 2:
            player_two_score = f"{score_two}"
            if player_two.buff is not None and player_two_alive:
                player_two_score += f" {player.buff.value} {player.buff_timer:.0f}"
            screen.blit(font.render(player_two_score, True, RED), (5, 25))
            

        pygame.display.flip()
        dt = clock.tick(60) / 1000


def end_screen(screen, num_players, score, score_two, difficulty):
    
    game_over = UIElement(
        center_position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 300),
        font_size=80,
        bg_rgb=RED,
        text_rgb=WHITE,
        text="GAME OVER!",
        action=None,
    )
    player_score = UIElement(
        center_position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 200),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text=f"Player One Score was: {score}",
        action=None,
    )
    rty_btn = UIElement(
        center_position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
        font_size=50,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Retry",
        action=GameState.GAME,
    )
    back_btn = UIElement(
        center_position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100),
        font_size=50,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Back to Menu",
        action=GameState.TITLE,
    )
    quit_btn = UIElement(
        center_position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200),
        font_size=50,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )
    buttons = [game_over, player_score,rty_btn, back_btn, quit_btn]
    if num_players >= 2:    
        player_two_score = UIElement(
            center_position=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100),
            font_size=30,
            bg_rgb=BLACK,
            text_rgb=RED,
            text=f"Player Two score was: {score_two}",
            action=None,
        )
        rty_btn.action = GameState.GAMETWO
        buttons.append(player_two_score)
    

     #time keepking
    clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroidsfield = AsteroidField(SCREEN_WIDTH, SCREEN_HEIGHT, difficulty.value)


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
        dt = clock.tick(60) / 1000


def main():
    pygame.init()
    print("Starting Asteroids!")
    
    #sets the screen width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = GameState.TITLE
    difficulty = Difficulty.NORMAL
    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen, difficulty)

        if game_state == GameState.MENU:
            game_state, screen, difficulty = menu_screen(screen, difficulty)

        if game_state == GameState.GAME:
            num_players = 1
            game_state, score, score_two = game_screen(screen, num_players, difficulty)
        
        if game_state == GameState.GAMETWO:
            num_players = 2
            game_state, score, score_two = game_screen(screen, num_players, difficulty)

        if game_state == GameState.END:
            game_state = end_screen(screen, num_players, score, score_two, difficulty)

        if game_state == GameState.QUIT:
            pygame.quit()
            return





if __name__ == "__main__":
    main()