import pygame

FPS = 60
main_sprite_sheet = None
screen_width = 1700
screen_height = 900

player_group = pygame.sprite.Group()
player_starting_position = (1700 / 2, 700)
player_speed = 6

gas_group = pygame.sprite.Group()
gas_spawn_time = 10

bullet_speed = 5
player_shoot_time = 10
bullet_group = pygame.sprite.Group()
bullet_kill_time = 80

cloud_group = pygame.sprite.Group()
cloud_images = []
cloud_speed = 8
cloud_time = 14
cloud_timer = 0

enemy_group = pygame.sprite.Group()
enemy_speed = 1
enemy_shoot_time = 10
