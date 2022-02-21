from gfx.detail import Detail
from gfx.text_manager import TextManager


class Label(Detail):
    __slots__ = 'color', 'font_type', 'font_size', 'static_txt', 'dynamic_txt', '_render'

    def __init__(self, x, y, color, font_type, font_size,  **kwargs):
        if 'static_txt' in kwargs and 'dynamic_txt' in kwargs:
            raise AttributeError("Cannot create label without static nor dynamic txt")
        if 'static_txt' not in kwargs and 'dynamic_txt' not in kwargs:
            raise AttributeError("Cannot create label with both static and dynamic txt")
        self.color = color
        self.font_type = font_type
        self.font_size = font_size
        if 'static_txt' in kwargs:
            self.static_txt = kwargs['static_txt']
            self.dynamic_txt = None
            self._render, (width, height) = TextManager().get_render(self.static_txt, self.color, self.font_type, self.font_size)
            kwargs.pop('static_txt')
        if 'dynamic_txt' in kwargs:
            self.static_txt = None
            self.dynamic_txt = kwargs['dynamic_txt']
            self._render, (width, height) = TextManager().get_default_render()
            kwargs.pop('dynamic_txt')
        super().__init__(x, y, width, height, **kwargs)

    def get_surface(self):
        if self.static_txt is not None:
            return self._render
        else:
            self._render, (self.width, self.height) = TextManager().get_render(self.dynamic_txt(), self.color, self.font_type, self.font_size)
            return self._render
