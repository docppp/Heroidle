from typing import Any

from dataclassy import dataclass

from utils import RGB
from wrapg.graphics import Graphics
from .detail import Detail
from .text_manager import TextManager


@dataclass(slots=True)
class Label(Detail):
    color: RGB
    font_type: str
    font_size: int
    text: 'Any' = lambda: ""
    _render: Graphics.Surface = None

    def __post_init__(self):
        self._render, size = TextManager().get_default_render()
        self._width, self._height = size

    def get_surface(self):
        self._render, size = TextManager().get_render(self.text(), self.color, self.font_type, self.font_size)
        self._width, self._height = size
        return self._render
