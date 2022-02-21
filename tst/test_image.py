import unittest

from gfx.image import Image
from wrapg import Graphics


class TestImage(unittest.TestCase):

    def test_surface(self):
        Graphics.load_image = lambda *args: (*args, (800, 600))
        image = Image(x=0, y=0, sprite="DummyImage")
        self.assertEqual(image.get_surface(), "DummyImage")

    def test_extra_args(self):
        Graphics.load_image = lambda *args: (*args, (800, 600))
        image = Image(x=0, y=0, sprite="DummyImage", on_click=lambda: "42", topness=3, movable=True, active=False)
        self.assertEqual(image.topness, 3)
        self.assertEqual(image.movable, True)
        self.assertEqual(image.active, False)
        self.assertEqual(image.on_click(), "42")


if __name__ == '__main__':
    unittest.main()
