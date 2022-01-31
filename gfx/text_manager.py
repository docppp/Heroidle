from dataclassy import dataclass
from pympler import asizeof

from utils import COLORS
from utils import RGB
from utils import Singleton
from wrapg.graphics import Graphics


class TextManager(metaclass=Singleton):

    @dataclass(slots=True)
    class Element:
        text: str = ""
        color: RGB = COLORS.BLACK
        font_type: str = "monospace"
        font_size: int = 15

        def __hash__(self):
            return hash(str(self))

    def __init__(self, cache_size=10, unit='MB'):
        if unit not in ['B', 'KB', 'MB']:
            raise ValueError(f"{unit} not in available units ['B', 'KB', 'MB']")
        self.fonts: dict[tuple[str, int], Graphics.Font] = {}
        self.renders: dict[TextManager.Element, Graphics.Surface] = {}
        self.cache_size = cache_size if unit == 'B' \
            else (cache_size * 1000 if unit == 'KB'
                  else cache_size * 1000 * 1000)

    def get_render(self, text: str, color: RGB, font_type: str, font_size: int) -> tuple[Graphics.Surface, tuple[int, int]]:
        e = TextManager.Element(text, color, font_type, font_size)
        if e in self.renders:
            return self.renders[e], self.renders[e].get_size()

        if not (font_type, font_size) in self.fonts:
            f = Graphics.create_sys_font(font_type, font_size)
            self.fonts[(font_type, font_size)] = f
        else:
            f = self.fonts[(font_type, font_size)]
        render = Graphics.render_text(f, text, color)
        self.renders[e] = render
        total_size = asizeof.asizeof(self)
        if total_size > self.cache_size:
            try:
                self.renders.popitem()
                self.renders.popitem()
            except KeyError:
                pass
        return render, render.get_size()

    def get_default_render(self):
        e = TextManager.Element()
        return self.get_render(e.text, e.color, e.font_type, e.font_size)
