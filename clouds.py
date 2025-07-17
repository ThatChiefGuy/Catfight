import pygame
import snipets
import random


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(snipets.cloud_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-20, snipets.screen_width + 20)
        self.rect.bottom = 0
        snipets.cloud_group.add(self)

    def update(self):
        self.rect.y += snipets.cloud_speed
        if self.rect.top >= snipets.screen_height:
            self.kill()
