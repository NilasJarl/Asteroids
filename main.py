import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #sets the screen width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Initiate the player in the middel of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    BLACK = (0, 0, 0) #color black for the screen
    
    #game loop
    while True:
        for event in pygame.event.get(): #Stops the loop if the windows is closed
            if event.type == pygame.QUIT:
                return
            
        screen.fill(BLACK) #turns screen black.
        player.update(dt)
        player.draw(screen) #draw the player
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
