import pygame
import snipets
import random

class Gas(pygame.sprite.Sprite):
    def __init__(self, starting_position):
        super().__init__()
        self.image_list = [snipets.main_sprite_sheet.get_sprite(103, 72, 9, 8, 2, (0, 0, 0)),
                           snipets.main_sprite_sheet.get_sprite(101, 88, 10, 10, 2, (0, 0, 0)),
                           snipets.main_sprite_sheet.get_sprite(84, 81, 14, 11, 1.5, (0, 0, 0)),
                           snipets.main_sprite_sheet.get_sprite(92, 72, 4, 4, 3, (0, 0, 0))]
        self.image = random.choice(self.image_list)
        self.rect = self.image.get_rect()
        self.rect.center = starting_position
        self.disappear_timer = 0
        self.disappear_time = 50
        snipets.gas_group.add(self)

    def update(self):
        size_x, size_y = self.image.get_size()
        self.disappear_timer += 1
        self.rect.y += snipets.gas_speed
        if self.rect.top == snipets.screen_height:
            self.kill()
        if self.disappear_timer >= self.disappear_time and not size_x < 0 and not size_y < 0:
            self.image = pygame.transform.scale(self.image, (size_x / 1.1, size_y / 1.1)).convert_alpha()
