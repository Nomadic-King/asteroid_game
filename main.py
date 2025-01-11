import pygame
import pygame.font
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    print(f"Starting asteroids!")

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000

        for sprite in updatable:
            sprite.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if player.collisions(asteroid):
                game_over_font = pygame.font.Font(None, 74)
                game_over_text = game_over_font.render('Game Over!', True, (255, 0, 0))
                game_over_rect = game_over_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
                prompt_font = pygame.font.Font(None, 36)
                prompt_text = prompt_font.render('(click or press any key to exit)', True, (200, 200, 200))  
                prompt_rect = prompt_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 50))
                screen.blit(game_over_text, game_over_rect)
                screen.blit(prompt_text, prompt_rect)
                pygame.display.flip()

                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                            waiting = False
                            sys.exit()
                        if event.type == pygame.QUIT:
                            waiting = False
                            sys.exit()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
