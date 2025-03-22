import circleshape
import main
import pygame
import random
from constants import *

class Asteroid(circleshape.CircleShape):
        def __init__(self, x, y, radius):
            super().__init__(x, y, radius)
            
        def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
        def update(self, dt):
            self.position += self.velocity * dt
        
        def split(self):
            self.kill()

            if self.radius <= ASTEROID_MIN_RADIUS:
                return
            
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = new_velocity1 * 1.2
            asteroid2.velocity = new_velocity2 * 1.2
            