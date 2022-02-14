import unittest

import settings
from gfx.animation import Animation
from wrapg import Graphics


class TestAnimation(unittest.TestCase):

    def setUp(self):
        Graphics.load_images = lambda *args: (range(settings.FPS), (800, 600))
        self.animation = Animation(x="0", y="0", sprites_dir="DummyImages")

    def test_surfaces(self):
        for i in range(settings.FPS - 1):
            self.assertEqual(self.animation.get_surface(), i + 1)

    def test_surface_flip(self):
        self.animation.current_frame = settings.FPS - 1
        self.animation.get_surface()
        self.assertEqual(self.animation.current_frame, 0)


if __name__ == '__main__':
    unittest.main()
