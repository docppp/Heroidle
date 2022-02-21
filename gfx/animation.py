import settings
from gfx.detail import Detail
from wrapg.graphics import Graphics


class Animation(Detail):
    __slots__ = 'sprites_dir', '_images', 'current_frame'

    def __init__(self, x, y, sprites_dir, **kwargs):
        self.sprites_dir = sprites_dir
        self._images, (width, height) = Graphics.load_images(self.sprites_dir)
        self.current_frame = 0
        super().__init__(x, y, width, height, **kwargs)

    def get_surface(self):
        self.current_frame = (self.current_frame + 1) % settings.FPS
        return self._images[self.current_frame]




