import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, difficulty):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.spawn_timer = 0.0
        self.dif_factor = difficulty
        self.edges = [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * self.SCREEN_HEIGHT),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    self.SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * self.SCREEN_HEIGHT
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(x * self.SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    x * self.SCREEN_WIDTH, self.SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
                ),
            ],
        ]
    
    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > (ASTEROID_SPAWN_RATE / self.dif_factor):
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(60, 140) * self.dif_factor
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)