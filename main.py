# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_ship = player.Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("Black")
        player.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
