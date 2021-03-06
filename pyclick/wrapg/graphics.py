import imghdr
import struct
from os import listdir
from os import sep
from os.path import join
from random import choice
from typing import Union

import pygame as pg
import pygame.draw

from showcase import settings
from pyclick.utils.color_constants import RGB, COLOR_LIST


class Graphics:

    class Surface:
        __slots__ = '_pg_surface'

        def __init__(self, surface: pg.Surface):
            self._pg_surface = surface

        def get_size(self):
            return self._pg_surface.get_size()

    class Rect:
        __slots__ = '_pg_rect', 'color'

        def __init__(self, rect: pg.Rect):
            self._pg_rect = rect
            self.color = choice(COLOR_LIST)

    class Font:
        __slots__ = '_pg_font'

        def __init__(self, font: pg.font.Font):
            self._pg_font = font

    @staticmethod
    def create_rect(x, y, width, height):
        return Graphics.Rect(pg.Rect(x, y, width, height))

    @staticmethod
    def load_image(file_name: str) -> tuple[Surface, tuple[int, int]]:
        path = join(settings.ASSETS_PATH, file_name)
        size = Graphics._get_png_image_size(path)
        return Graphics.Surface(pg.image.load(path)), size

    @staticmethod
    def load_images(dir_name: str) -> tuple[list[Surface], tuple[int, int]]:
        path = join(settings.ASSETS_PATH, dir_name)
        images = []
        for file_name in listdir(path):
            try:
                sprite = Graphics.Surface(pg.image.load(join(path, file_name)))
                images.append(sprite)
            except Exception as e:
                print(f"Error {e} during loading {file_name}.")
        size = Graphics._get_png_dir_size(path)
        return images, size

    @staticmethod
    def main_window(caption: str, size: tuple[int, int]) -> Surface:
        pg.display.set_caption(caption)
        return Graphics.Surface(pg.display.set_mode(size))

    @staticmethod
    def update_display() -> None:
        pg.display.update()

    @staticmethod
    def draw_on_surface(surface: Surface, image: Union[Surface, Rect], position: tuple[int, int]):
        if isinstance(image, Graphics.Surface):
            surface._pg_surface.blit(image._pg_surface, position)  # intentional use of protected member
        elif isinstance(image, Graphics.Rect):
            pygame.draw.rect(surface._pg_surface, image.color, image._pg_rect)
        else:
            raise ValueError(f"Cannot draw {image}, type {type(image)}")

    @staticmethod
    def create_sys_font(font_type: str, font_size: int) -> Font:
        return Graphics.Font(pg.font.SysFont(font_type, font_size))

    @staticmethod
    def render_text(font: Font, text: str, color: RGB):
        return Graphics.Surface(font._pg_font.render(text, True, color))  # intentional use of protected member

    @staticmethod
    def _get_png_image_size(file_name: str) -> tuple[int, int]:
        with open(file_name, 'rb') as file_handle:
            head = file_handle.read(24)
            if len(head) != 24:
                raise ValueError(f"{file_name} is not png image")
            if imghdr.what(file_name) == 'png':
                check = struct.unpack('>i', head[4:8])[0]
                if check != 0x0d0a1a0a:
                    raise ValueError(f"{file_name} is not png image")
                width, height = struct.unpack('>ii', head[16:24])
                return width, height
            raise ValueError(f"{file_name} is not png image")

    @staticmethod
    def _get_png_dir_size(dir_path: str, ignore_size_mismatch=False) -> tuple[int, int]:
        x, y = Graphics._get_png_image_size(dir_path + sep + listdir(dir_path)[0])
        for file_name in listdir(dir_path):
            width, height = Graphics._get_png_image_size(dir_path + sep + file_name)
            if (x, y) != (width, height) and not ignore_size_mismatch:
                raise ValueError(f"Png at {dir_path} do not match in size."
                                 f"{(x, y)} != {(width, height)}")
        return x, y
