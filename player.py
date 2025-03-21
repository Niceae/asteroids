import circleshape
import constants 
from constants import *
import pygame
import main
import shot
class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cool_down = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shot_cool_down <= 0:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            position = self.position + forward * self.radius
        # Just create the shot, it will automatically add itself to the containers
            shot.Shot(position.x, position.y, SHOT_RADIUS, forward * PLAYER_SHOOT_SPEED)
            self.shot_cool_down = .3

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cool_down = max(self.shot_cool_down - dt, 0)

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