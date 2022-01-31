from dataclassy import dataclass

from wrapg.graphics import Graphics
from .detail import Detail


@dataclass(slots=True)
class Animation(Detail):
    sprites_dir: str
    current_frame: int = 0
    _images: list[Graphics.Surface] = None

    def __post_init__(self):
        self._images, size = Graphics.load_images(self.sprites_dir)
        self._width, self._height = size

    def get_surface(self):
        self.current_frame = (self.current_frame + 1) % 24
        return self._images[self.current_frame]




