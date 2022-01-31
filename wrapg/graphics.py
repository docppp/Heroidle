from os import listdir
from os.path import join

import pygame as pg

from utils import get_png_dir_size
from utils import get_png_image_size
from utils import RGB


class Graphics:
    _master_path = 'assets'

    class Surface:
        __slots__ = '_pg_surface'

        def __init__(self, surface: pg.Surface):
            self._pg_surface = surface

        def get_size(self):
            return self._pg_surface.get_size()

    class Font:
        __slots__ = '_pg_font'

        def __init__(self, font: pg.font.Font):
            self._pg_font = font

    @staticmethod
    def load_image(file_name: str) -> tuple[Surface, tuple[int, int]]:
        path = join(Graphics._master_path, file_name)
        size = get_png_image_size(path)
        return Graphics.Surface(pg.image.load(path)), size

    @staticmethod
    def load_images(dir_name: str) -> tuple[list[Surface], tuple[int, int]]:
        path = join(Graphics._master_path, dir_name)
        images = []
        for file_name in listdir(path):
            try:
                sprite = Graphics.Surface(pg.image.load(join(path, file_name)))
                images.append(sprite)
            except Exception as e:
                print(f"Error {e} during loading {file_name}.")
        size = get_png_dir_size(path)
        return images, size

    @staticmethod
    def main_window(caption: str, size: tuple[int, int]) -> Surface:
        pg.display.set_caption(caption)
        return Graphics.Surface(pg.display.set_mode(size))

    @staticmethod
    def update_display() -> None:
        pg.display.update()

    @staticmethod
    def draw_on_surface(surface: Surface, image: Surface, position: tuple[int, int]):
        surface._pg_surface.blit(image._pg_surface, position)  # intentional use of protected member

    @staticmethod
    def create_sys_font(font_type: str, font_size: int) -> Font:
        return Graphics.Font(pg.font.SysFont(font_type, font_size))

    @staticmethod
    def render_text(font: Font, text: str, color: RGB):
        return Graphics.Surface(font._pg_font.render(text, True, color))  # intentional use of protected member
