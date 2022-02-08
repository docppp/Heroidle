from dataclassy import dataclass

from detail import Detail
from wrapg.graphics import Graphics


@dataclass(slots=True)
class Image(Detail):
    sprite: str
    _image: Graphics.Surface = None

    def __post_init__(self):
        self._image, size = Graphics.load_image(self.sprite)
        self._width, self._height = size

    def get_surface(self):
        return self._image
