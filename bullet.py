import math

import pygame
import snipets

class Bullet(pygame.sprite.Sprite):
    def __init__(self, starting_position, shoot_by, player_position):
        super().__init__()
        self.image = snipets.main_sprite_sheet.get_sprite(2, 65, 2, 12, 2, (12, 12 ,21))
        self.rect = self.image.get_rect()
        self.rect.center = starting_position
        self.shoot_by = shoot_by
        self.player_position = player_position
        self.dx = 0
        self.dy = 0
        self.distance = 0
        self.kill_timer = 0
        snipets.bullet_group.add(self)
        x_distance = self.player_position[0] - self.rect.x
        y_distance = -(self.player_position[1] - self.rect.y)
        angle = math.degrees(math.atan2(-x_distance, y_distance))
        if shoot_by == "enemy":
            self.image = pygame.transform.rotate(self.image, angle)

    def update(self):
        self.kill_timer += 1
        if self.shoot_by == "player":
            self.rect.y -= snipets.bullet_speed

        if self.shoot_by == "enemy":
            radians = math.atan2(self.player_position[1] - self.rect.y, self.player_position[0] - self.rect.x)
            self.distance = int(math.hypot(self.player_position[0] - self.rect.x,
                                           self.player_position[1] - self.rect.y))
            self.dx = math.cos(radians)
            self.dy = math.sin(radians)
