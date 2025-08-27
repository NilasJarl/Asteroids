import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #sets the screen width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #time keepking
    clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    #Initiate the player in the middel of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()
