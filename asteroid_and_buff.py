import pygame
import random
from circleshape import CircleShape
from constants import WHITE, RED, BLUE, GREEN, ASTEROID_MIN_RADIUS
from player import Buff

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity *dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2

#buff roids are similar to asteroids but far less complex when hit it simply returns what type of buff it is. the buffs are an enum defines in player.py
class Buffoid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        buff_types = list(Buff)
        self.buff = random.choice(buff_types)

    def draw(self, screen):
        match self.buff:
            case Buff.MULTISHOT:
                color = RED
            case Buff.MACHINEGUN:
                color = BLUE
            case Buff.INVULNERABILITY:
                color = GREEN
        pygame.draw.circle(screen, color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity *dt

    def hit(self):
        return self.buff
        
