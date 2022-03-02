from showcase import settings
from pyclick.gfx.detail import Detail
from pyclick.wrapg.graphics import Graphics


class Animation(Detail):
    __slots__ = 'sprites_dir', 'images', 'current_frame'

    def __init__(self, x: int, y: int, sprites_dir: str, **kwargs):
        self.sprites_dir = sprites_dir
        self.images, (width, height) = Graphics.load_images(self.sprites_dir)
        self.current_frame = 0
        super().__init__(x, y, width, height, **kwargs)

    def get_surface(self):
        self.current_frame = (self.current_frame + 1) % settings.FPS
        return self.images[self.current_frame]




