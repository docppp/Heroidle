import unittest

from gfx.image import Image
from wrapg import Graphics


class TestImage(unittest.TestCase):

    def test_surface(self):
        Graphics.load_image = lambda *args: (*args, (800, 600))
        image = Image(x="0", y="0", sprite="DummyImage")
        self.assertEqual(image.get_surface(), "DummyImage")


if __name__ == '__main__':
    unittest.main()
