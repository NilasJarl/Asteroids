import pygame
from circleshape import CircleShape
from enum import Enum
from shot import Shot
from constants import *

class Buff(Enum):
    MACHINEGUN = "Machinegun"
    MULTISHOT = "Multishot"
    INVULNERABILITY = "Invulnerability"

class Player(CircleShape):
    def __init__(self, player_num, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.player_num = player_num #plaer one or two
        #player one is white player two is red.
        if self.player_num == 1:
            self.color = WHITE 
        elif self.player_num == 2:
            self.color = RED 
        self.buff = None
        self.buff_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        #draw the player on the screen in their color, in the trinagle shape witha  line width of 2
            pygame.draw.polygon(screen, self.color, self.triangle(), 2) 
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        #if the player has a buff reduce the timer on the buff if time is out remove the buff from the player.
        if self.buff is not None:
            self.buff_timer -= dt
            if self.buff_timer <= 0:
                self.buff = None
                self.buff_timer = None
        keys = pygame.key.get_pressed()
        #player one controls
        if self.player_num == 1:
            if keys[pygame.K_a]:
                self.rotate(-dt)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_w]:
                self.move(dt)
            if keys[pygame.K_s]:
                self.move(-dt)
            if keys[pygame.K_SPACE]:
                self.shoot()
        #player two controls.
        elif self.player_num == 2:
            if keys[pygame.K_LEFT]:
                self.rotate(-dt)
            if keys[pygame.K_RIGHT]:
                self.rotate(dt)
            if keys[pygame.K_UP]:
                self.move(dt)
            if keys[pygame.K_DOWN]:
                self.move(-dt)
            if keys[pygame.K_RCTRL]:
                self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    #add buff to the player and set the timer to the constand from constants.py
    def buff_player(self, buff):
        self.buff = buff
        self.buff_timer = BUFF_DURATION


    def shoot(self):
        #only when the shot cooldown is 0 can you shoot.
        if not self.timer > 0:
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.color)
            new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            #multishot spawns two extra show 10 degress to either side
            if self.buff == Buff.MULTISHOT:
                new_shot2 = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.color)
                new_shot2.velocity = pygame.Vector2(0, 1).rotate(self.rotation - 10) * PLAYER_SHOOT_SPEED
                new_shot3 = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.color)
                new_shot3.velocity = pygame.Vector2(0, 1).rotate(self.rotation + 10) * PLAYER_SHOOT_SPEED
            #reset the shot cooldown, with teh machinegun buff it is on third of the CD from constants.py
            if self.buff == Buff.MACHINEGUN:
                self.timer = PLAYER_SHOOT_COOLDOWN / 3
            else:
                self.timer = PLAYER_SHOOT_COOLDOWN
