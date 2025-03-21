import pygame
import sys
import constants
import player
from asteroid import Asteroid
import asteroidfield
import circleshape
import shot
pygame.init()
from constants import *
def main():
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        dt = 0
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        updatable = pygame.sprite.Group()
        drawables = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        player.Player.containers = (updatable, drawables)
        Asteroid.containers = (asteroids, updatable, drawables)
        asteroidfield.AsteroidField.containers = (updatable)
        shot.Shot.containers = (shots, updatable, drawables)
        player_ship = player.Player(x,y)
        asteroid_field = asteroidfield.AsteroidField()
        
        running = True
        while running:
            dt = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("black")
            for drawable in drawables:
                drawable.draw(screen)
            updatable.update(dt)
                        # After updating all game objects
            for asteroid in asteroids:
                if player_ship.collides_with(asteroid):
                    # Create and render the game over text
                    font = pygame.font.Font(None, 74)
                    text = font.render("Game over!", True, (255, 0, 0))
        
                    # Position the text in the center of the screen
                    text_rect = text.get_rect(center=(screen.get_width()//2, screen.get_height()//2))
        
                    # Draw the text on the screen
                    screen.blit(text, text_rect)
        
                    # Update the display to show the text
                    pygame.display.flip()
        
                    # Wait for 2 seconds so player can see the message
                    pygame.time.wait(2000)
        
                    # Exit the game
                    sys.exit()

            pygame.display.flip()
if __name__ == "__main__":
    print ("Starting Asteroids!")
    print ("Screen width: 1280")
    print ("Screen height: 720")
    main()