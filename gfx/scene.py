from dataclassy import dataclass

from wrapg.graphics import Graphics
from .detail import Detail


@dataclass(slots=True)
class Scene:
    background: str
    x: int = 0
    y: int = 0
    active: bool = True
    _width: int = None
    _height: int = None
    _image: Graphics.Surface = None
    _details: list[Detail] = None
    _overlays: list = None

    def __post_init__(self):
        self._image, size = Graphics.load_image(self.background)
        self._width, self._height = size
        self._details = []
        self._overlays = []

    def check_focus(self, mouse_x, mouse_y):
        # reverse order, so those on top is checked first
        for layer in reversed(self._overlays):
            focused = layer.check_focus(mouse_x, mouse_y)
            if focused is not None:
                return focused
        if self.active:
            under_mouse = [det for det in self._details if det.is_focused(mouse_x, mouse_y)]
            if under_mouse:
                return max(under_mouse, key=lambda item: item.topness)
        return None

    def draw_all(self, window: Graphics.Surface):
        if self.active:
            Graphics.draw_on_surface(window, self._image, (self.x, self.y))
            self._details.sort(key=lambda item: item.topness)
            for det in self._details:
                if det.active:
                    Graphics.draw_on_surface(window, det.get_surface(), (det.x, det.y))
        # put on the surface in order of the appearance
        for layer in self._overlays:
            layer.draw_all(window)

