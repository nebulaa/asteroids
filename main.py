import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    Shot.containers = (shots, updatable, drawable)

    AsteroidField()

    dt = 0
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)
            
        for obj in asteroids:
            if CircleShape.collide(obj, player):
                print("Game over")
                sys.exit()

        for obj in asteroids:
            for shot in shots:
                if CircleShape.collide(obj, shot):
                    obj.split()
                    shot.kill()
                    
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()