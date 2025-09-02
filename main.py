import pygame
from constants import *
from player import *



def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Gameloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        player1.update(dt)
        player1.draw(screen)
        pygame.display.flip()
        fpsClock.tick(60)
        dt = fpsClock.get_time() / 1000

if __name__ == "__main__":
    main()
