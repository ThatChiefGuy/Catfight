import pygame
import random
import bullet
import snipets
import player_gas


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.normal_image = snipets.main_sprite_sheet.get_sprite(0, 0, 68, 55, 2, (0, 0, 0))
        self.image_left = snipets.main_sprite_sheet.get_sprite(74, 0, 68, 55, 2, (0, 0, 0))
        self.image_right = snipets.main_sprite_sheet.get_sprite(148, 0, 68, 55, 2, (0, 0, 0))
        self.animation_state = "forward"
        self.engine_state = "on"
        self.image = self.normal_image

        self.propeller_image1 = snipets.main_sprite_sheet.get_sprite(123, 62, 27, 10, 2, (0, 0, 0))
        self.propeller_image2 = snipets.main_sprite_sheet.get_sprite(150, 62, 27, 10, 2, (0, 0, 0))
        self.propeller_image3 = snipets.main_sprite_sheet.get_sprite(177, 62, 27, 10, 2, (0, 0, 0))
        self.propeller_image = self.propeller_image1
        self.propeller_timer = 0
        self.propeller_time = 2
        self.propeller_state = 1

        self.rect = self.image.get_rect()
        self.rect.center = snipets.player_starting_position
        self.player_shoot_timer = 0

        self.gas_time = 0
        self.gas_spawn_time = snipets.gas_spawn_time

        snipets.player_group.add(self)

    def update(self, keys_pressed, window_size):
        self.movement(keys_pressed)
        self.collisions(window_size[0], window_size[1])
        self.shooting(keys_pressed)
        self.animation()

    def movement(self, keys_pressed):
        if self.engine_state == "on":
            if keys_pressed[ord("s")] or keys_pressed[pygame.K_DOWN]:
                self.engine_state = "off"

            if keys_pressed[ord("w")] or keys_pressed[pygame.K_UP]:
                self.rect.y -= snipets.player_speed

            if keys_pressed[ord("a")] or keys_pressed[pygame.K_LEFT]:
                self.rect.x -= snipets.player_speed
                self.animation_state = "left"

            if keys_pressed[ord("d")] or keys_pressed[pygame.K_RIGHT]:
                self.rect.x += snipets.player_speed
                self.animation_state = "right"

        if self.engine_state == "off":
            self.rect.y += snipets.player_speed

        if self.rect.bottom >= snipets.screen_height:
            self.engine_state = "on"

        if self.animation_state == "right" and keys_pressed[ord("a")] \
                or self.animation_state == "right" and keys_pressed[pygame.K_LEFT]:
            self.animation_state = "forward"

    def collisions(self, window_width, window_height):
        if self.rect.top < self.propeller_image.get_size()[1]:
            self.rect.top = self.propeller_image.get_size()[1]

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
        self.propeller_timer += 1

        if self.gas_time >= self.gas_spawn_time:
            self.gas_time = 0
            player_gas.Gas((self.rect.center[0] + random.randint(-10, 10), self.rect.bottom))

        if self.propeller_timer >= self.propeller_time:
            self.propeller_state += 1
            self.propeller_timer = 0

        if self.propeller_state > 3:
            self.propeller_state = 1

        if self.propeller_state == 1:
            self.propeller_image = self.propeller_image1

        if self.propeller_state == 2:
            self.propeller_image = self.propeller_image2

        if self.propeller_state == 3:
            self.propeller_image = self.propeller_image3

    def shooting(self, keys_pressed):
        self.player_shoot_timer += 1
        if keys_pressed[ord(" ")] and self.player_shoot_timer >= snipets.player_shoot_time:
            bullet.Bullet((self.rect.x + self.rect.width / 2 + random.randint(-20, 20), self.rect.top), "player", self.rect.center)
            self.player_shoot_timer = 0
