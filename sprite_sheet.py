import pygame


class SpriteSheet:
    def __init__(self, sheet):
        self.sheet = sheet

    def get_sprite(self, position_x, position_y, size_x, size_y, scale, color_key):
        image = pygame.Surface((size_x, size_y)).convert_alpha()
        image.blit(self.sheet, (0, 0), (position_x, position_y, size_x, size_y))
        image = pygame.transform.scale(image, (size_x * scale, size_y * scale))
        image.set_colorkey(color_key)
        return image
