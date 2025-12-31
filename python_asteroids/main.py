import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_SHOOT_SPEED
from logger import log_state, log_event
from sys import exit
def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for sprite in asteroids:
            if sprite.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                exit()
            for shot in shots:
                if sprite.collides_with(shot):
                    log_event("asteroid_shot")
                    sprite.split()
                    shot.kill()
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
