import pygame
import sys
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    Shot_Group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids_group, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (Shot_Group, updatable, drawable)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    #Gameloop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        for asteroid in asteroids_group:
            if asteroid.collision_check(player1):
                sys.exit("Game over!")
            for shot in Shot_Group:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()
        fpsClock.tick(60)
        dt = fpsClock.get_time() / 1000

if __name__ == "__main__":
    main()
