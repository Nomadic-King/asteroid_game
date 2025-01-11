import pygame
import random
import constants as c
from circleshape import CircleShape
from boomed import Boomed

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.size = self.get_size_from_radius(radius)

    def get_size_from_radius(self, radius):
        if radius > 50:
            return "Large"
        elif radius > 25:
            return "Medium"
        else:
            return "Small"

    def draw(self, surface):
        pygame.draw.circle(
                surface,
                "white",
                (self.position.x, self.position.y),
                self.radius,
                2
            )

    def split(self, asteroid_group, boom_group):
        self.kill()
        if self.radius <= c.ASTEROID_MIN_RADIUS:
            boom = Boomed(self.rect.center)
            boom_group.add(boom)
            return

        random_angle = random.uniform(20, 50)
        new_radius = self.radius - c.ASTEROID_MIN_RADIUS
        
        velocity_1 = self.velocity.rotate(random_angle) * 1.2
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = velocity_1

        velocity_2 = self.velocity.rotate(-random_angle) * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = velocity_2

        asteroid_group.add(asteroid_1, asteroid_2)

    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)
