import pygame

import Bullet
import snipets
import Player_gas


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.normal_image = snipets.main_sprite_sheet.get_sprite(0, 0, 68, 55, 2, (0, 0, 0))
        self.image_left = snipets.main_sprite_sheet.get_sprite(74, 0, 68, 55, 2, (0, 0, 0))
        self.image_right = snipets.main_sprite_sheet.get_sprite(148, 0, 68, 55, 2, (0, 0, 0))
        self.image = self.normal_image
        self.rect = self.image.get_rect()
        self.rect.center = snipets.player_starting_position
        self.animation_state = "forward"
        snipets.player_group.add(self)
        self.gas_time = 0
        self.gas_spawn_time = snipets.gas_spawn_time

    def update(self, keys_pressed, window_size):
        self.movement(keys_pressed)
        self.collisions(window_size[0], window_size[1])
        self.shooting(keys_pressed)
        self.animation()

    def movement(self, keys_pressed):
        if keys_pressed[ord("s")]:
            self.rect.y += snipets.player_speed

        if keys_pressed[ord("w")]:
            self.rect.y -= snipets.player_speed

        if keys_pressed[ord("a")]:
            self.rect.x -= snipets.player_speed
            self.animation_state = "left"

        if keys_pressed[ord("d")]:
            self.rect.x += snipets.player_speed
            self.animation_state = "right"

    def collisions(self, window_width, window_height):
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > window_height:
            self.rect.bottom = window_height

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > window_width:
            self.rect.right = window_width

    def animation(self):
        if self.animation_state == "forward":
            self.image = self.normal_image

        if self.animation_state == "left":
            self.image = self.image_left

        if self.animation_state == "right":
            self.image = self.image_right

        self.animation_state = "forward"

        self.gas_time += 1

        if self.gas_time >= self.gas_spawn_time:
            self.gas_time = 0
            Player_gas.Gas(self.rect.center)

    def shooting(self, keys_pressed):
        snipets.bullet_cooldown_timer += 1
        if keys_pressed[ord(" ")] and snipets.bullet_cooldown_timer >= snipets.bullet_cooldown:
            Bullet.Bullet(self.rect.center)
            snipets.bullet_cooldown_timer = 0





