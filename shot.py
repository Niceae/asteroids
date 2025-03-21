import circleshape
import main
import pygame
from constants import *

class Shot(circleshape.CircleShape):
    containers = None # Will be set later in main.py

    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)  # Call parent constructor with 3 args (+ self)
        self.velocity = velocity  # Store velocity as a separate property
        # Add self to containers if they exist
        if Shot.containers:
            for container in Shot.containers:
                container.add(self)

    def update(self, dt):
        # Update position based on velocity and time
        self.position += self.velocity * dt
        
    def draw(self, screen):
        # Draw the shot on the screen
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)