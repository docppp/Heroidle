from typing import Any, Optional

from dataclassy import dataclass

from gfx.detail import Detail
from gfx.text_manager import TextManager
from utils import RGB
from wrapg.graphics import Graphics


@dataclass(slots=True)
class Label(Detail):
    color: RGB
    font_type: str
    font_size: int
    static_txt: Optional[str] = None
    dynamic_txt: 'Any' = None
    _render: Graphics.Surface = None

    def __post_init__(self):
        if self.static_txt is None and self.dynamic_txt is None:
            raise AttributeError("Cannot create label without static nor dynamic txt")
        if self.static_txt is not None and self.dynamic_txt is not None:
            raise AttributeError("Cannot create label with both static and dynamic txt")

        if self.static_txt is not None:
            self._render, size = TextManager().get_render(self.static_txt, self.color, self.font_type, self.font_size)
            self._width, self._height = size
        else:
            self._render, size = TextManager().get_default_render()
            self._width, self._height = size

    def get_surface(self):
        if self.static_txt is not None:
            return self._render
        else:
            self._render, size = TextManager().get_render(self.dynamic_txt(), self.color, self.font_type, self.font_size)
            self._width, self._height = size
            return self._render
