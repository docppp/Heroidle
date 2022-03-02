from pyclick.gfx.detail import Detail
from pyclick.wrapg.graphics import Graphics


class Image(Detail):
    __slots__ = 'sprite', 'image'

    def __init__(self, x: int, y: int, sprite: str, **kwargs):
        self.sprite = sprite
        self.image, (width, height) = Graphics.load_image(sprite)
        super().__init__(x, y, width, height, **kwargs)

    def get_surface(self):
        return self.image
