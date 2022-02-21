from gfx.detail import Detail
from wrapg.graphics import Graphics


class Image(Detail):
    __slots__ = 'sprite', '_image'

    def __init__(self, x, y, sprite, **kwargs):
        self.sprite = sprite
        self._image, (width, height) = Graphics.load_image(sprite)
        super().__init__(x, y, width, height, **kwargs)

    def get_surface(self):
        return self._image
