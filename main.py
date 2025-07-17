import pygame
import Enemy
import clouds
import player
import snipets
import sprite_sheet


def load_images():
    snipets.cloud_images = [snipets.main_sprite_sheet.get_sprite(0, 96, 100, 70, 2, (0, 0, 0)),
                            snipets.main_sprite_sheet.get_sprite(101, 99, 98, 62, 2, (0, 0, 0)),
                            snipets.main_sprite_sheet.get_sprite(200, 96, 37, 32, 2, (0, 0, 0)),
                            snipets.main_sprite_sheet.get_sprite(0, 168, 51, 35, 2, (0, 0, 0)),
                            snipets.main_sprite_sheet.get_sprite(74, 169, 62, 47, 2, (0, 0, 0)),
                            snipets.main_sprite_sheet.get_sprite(160, 160, 97, 61, 2, (0, 0, 0)),
                            snipets.main_sprite_sheet.get_sprite(7, 217, 115, 61, 2, (0, 0, 0))]


class Game:
    def __init__(self, window_height, window_width):
        self.screen = pygame.display.set_mode((window_height, window_width))
        self.main_clock = pygame.time.Clock()
        main_sprite_sheet_image = pygame.image.load("Assets/sprites.png")
        snipets.main_sprite_sheet = sprite_sheet.SpriteSheet(main_sprite_sheet_image)
        load_images()
        self.player = player.Player()
        Enemy.Enemy(self.player.rect.center)

    def draw(self):
        self.screen.fill((0, 200, 250))
        snipets.cloud_group.draw(self.screen)
        snipets.gas_group.draw(self.screen)
        for bullet in snipets.bullet_group:
            self.screen.blit(bullet.image, bullet.rect.center)
        snipets.enemy_group.draw(self.screen)
        snipets.player_group.draw(self.screen)
        self.screen.blit(self.player.propeller_image,
                         (self.player.rect.center[0] - self.player.propeller_image.get_size()[0] / 2,
                          self.player.rect.top - self.player.propeller_image.get_size()[1] / 2))
        pygame.display.update()

    def main(self):
        run = True
        while run:
            self.main_clock.tick(snipets.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            snipets.cloud_timer += 1
            if snipets.cloud_timer >= snipets.cloud_time:
                clouds.Cloud()
                snipets.cloud_timer = 0

            snipets.player_group.update(pygame.key.get_pressed(),
                                        (snipets.screen_width, snipets.screen_height))
            snipets.gas_group.update()
            snipets.bullet_group.update()
            snipets.cloud_group.update()
            snipets.enemy_group.update(self.player.rect.center)
            self.draw()


if __name__ == "__main__":
    game = Game(snipets.screen_width, snipets.screen_height)
    game.main()
