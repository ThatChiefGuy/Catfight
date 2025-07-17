import pygame

import bullet
import snipets


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player_position):
        super().__init__()
        self.image = snipets.main_sprite_sheet.get_sprite(188, 310, 68, 57, 2, (0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = 500, 100
        self.shoot_timer = 0
        snipets.enemy_group.add(self)
        self.shooting(player_position)

    def update(self, player_position):
        self.movement()

    def movement(self):
        self.rect.y += snipets.enemy_speed

    def shooting(self, player_position):
        self.shoot_timer += 1
        if self.shoot_timer >= snipets.enemy_shoot_time:
            bullet.Bullet(self.rect.center, "enemy", player_position)
            self.shoot_timer = 0


