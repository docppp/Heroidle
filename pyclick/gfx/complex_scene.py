from __future__ import annotations
from typing import TYPE_CHECKING

from pyclick.gfx.abstract_scene import AbstractScene
from pyclick.gfx.scrollable import Scrollable
from pyclick.wrapg.graphics import Graphics

if TYPE_CHECKING:
    from pyclick.gfx.detail import Detail


class ComplexScene(AbstractScene):

    def __init__(self, layers: list[AbstractScene]):
        self.layers = layers

    def check_focus(self, mouse_pos: tuple[int, int]):
        # reverse order, so those on top is checked first
        for layer in reversed(self.layers):
            focused = layer.check_focus(mouse_pos)
            if focused is not None:
                return focused
        return None

    def check_focus_overlay(self, mouse_pos: tuple[int, int]):
        # reverse order, so those on top is checked first
        for layer in reversed(self.layers):
            if layer.check_focus_overlay(mouse_pos):
                return layer
        return None

    def draw_all(self, window: Graphics.Surface):
        for layer in self.layers:
            layer.draw_all(window)

    def move_detail_by(self, detail: Detail, delta_pos: tuple[int, int], mouse_pos: tuple[int, int]):
        # reverse order, so those on top is checked first
        for layer in reversed(self.layers):
            layer.move_detail_by(detail, delta_pos, mouse_pos)

    def scroll_by(self, mouse_pos: tuple[int, int], dy: int):
        layer = self.check_focus_overlay(mouse_pos)
        if isinstance(layer, Scrollable):
            layer.scroll_by(mouse_pos, dy)
