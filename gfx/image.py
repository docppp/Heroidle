from dataclassy import dataclass

from wrapg.graphics import Graphics
from .detail import Detail


@dataclass(slots=True)
class Image(Detail):
    sprite: str
    _image: Graphics.Surface = None

    def __post_init__(self):
        self._image, size = Graphics.load_image(self.sprite)
        self._width, self._height = size

    def get_surface(self):
        return self._image