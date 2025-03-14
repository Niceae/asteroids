import pygame
import constants
pygame.init()
from constants import *
def main():
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("black")
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
if __name__ == "__main__":
    print ("Starting Asteroids!")
    print ("Screen width: 1280")
    print ("Screen height: 720")
    main()