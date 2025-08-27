import pygame
from constants import *
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #sets the screen width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    BLACK = (0, 0, 0) #color black for the screen
    
    #game loop
    while True:
        for event in pygame.event.get(): #Stops the loop if the windows is closed
            if event.type == pygame.QUIT:
                return
            
        screen.fill(BLACK) #turns screen black.
        pygame.display.flip()





if __name__ == "__main__":
    main()
