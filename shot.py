import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = None

    def draw(self, surface):
        pygame.draw.circle(
                surface,
                "white",
                (self.position.x, self.position.y),
                self.radius,
                2
            )

    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)
