#!/usr/bin/env python3

#pygame documentation https://www.pygame.org/docs/ref/pygame.html

import pygame
import constants

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black", rect=None, special_flags=0)
        pygame.display.flip()

if __name__ == "__main__":
    main()
