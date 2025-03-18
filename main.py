import pygame
import constants
import player
pygame.init()
from constants import *
def main():
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        dt = 0
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        player_ship = player.Player(x,y)
        running = True
        while running:
            dt = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("black")
            player_ship.draw(screen)
            player_ship.update(dt)
            pygame.display.flip()
if __name__ == "__main__":
    print ("Starting Asteroids!")
    print ("Screen width: 1280")
    print ("Screen height: 720")
    main()