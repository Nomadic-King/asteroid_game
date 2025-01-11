import pygame

class Boomed(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        font = pygame.font.Font(None, 36)
        self.image = font.render("BOOM", True, (255, 0, 0))
        self.image.set_alpha(255)
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect(center=position)
        self.fade_timer = 30

    def update(self):
        self.fade_timer -= 1
        current_alpha = self.image.get_alpha()
        new_alpha = max(0, current_alpha - 8)
        self.image.set_alpha(new_alpha)

        if self.fade_timer <= 0:
            self.kill()
