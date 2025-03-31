# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    my_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
   
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)
    
    player = Player(x, y)
    asteroidField_obj = AsteroidField()
    

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        screen.fill("red")
        
        for p in drawable:
            p.draw(screen)

        updatable.update(dt)
        
        for p in asteroids:
            if p.collisions(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()
        
        dt = my_clock.tick(60)  / 1000
        
if __name__ == "__main__":
    main()
