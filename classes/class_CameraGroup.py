import pygame as pg
from pygame.sprite import Group
from pygame.image import load
from pygame.display import get_surface
from pygame.math import Vector2

from functions.function_load_sources import load_sources


class CameraGroup(Group):
    def __init__(
        self,
        game=None
        ):
        super().__init__(self)

        self.game = game
        self.change_screen_size()
        self.camera_rect = pg.Rect(10, 10, 10, 10)
        self.old_screen_size = self.game.screen.window.get_size()
        self.set_backgroung()

    def set_backgroung(self):
        self.source = load_sources(
            dir_path='config/sources/backgrounds',
            level=1,
            current_level=1
        )
        self.background_surface = load(self.source).convert_alpha()
        self.background_rect = self.background_surface.get_rect()

    def change_screen_size(self):
        self.display_surface = get_surface()
        self.offset = Vector2()
        self.half = (
            self.display_surface.get_size()[0] // 2,
            self.display_surface.get_size()[1] // 2
        )

    def check_screen_size(self):
        if self.old_screen_size != self.game.screen.window.get_size():
            self.change_screen_size()
        self.old_screen_size = self.game.screen.window.get_size()

    def camera_center(self, target):
        self.offset.x = target.rect.centerx - self.half[0]
        self.offset.y = target.rect.centery - self.half[1]

    def custom_draw(self, player):
        self.camera_center(player)
        self.background_offset = self.background_rect.topleft - self.offset
        self.display_surface.blit(self.background_surface, self.background_offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.center):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(self.image_rotation, offset_position)

    def update(self):
        self.check_screen_size()
        super().update()
        self.custom_draw(self.game.player)
