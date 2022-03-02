import unittest
from unittest.mock import Mock

from pyclick.gfx.label import Label
from pyclick.gfx.text_manager import TextManager
from pyclick.utils import COLORS


class TestLabel(unittest.TestCase):

    @staticmethod
    def dynamic_txt():
        return "42"

    def setUp(self):
        TextManager().get_render = Mock(return_value=(None, (0, 0)))
        TextManager().get_default_render = Mock(return_value=(None, (0, 0)))

    def test_label_create_with_both_txt(self):
        with self.assertRaises(AttributeError):
            Label(0, 0, COLORS.BLACK, font_type="monospace", font_size=15, dynamic_txt=self.dynamic_txt, static_txt="a")

    def test_label_create_without_txt(self):
        with self.assertRaises(AttributeError):
            Label(0, 0, COLORS.BLACK, font_type="monospace", font_size=15)

    def test_static_label_render(self):
        label = Label(0, 0, COLORS.BLACK, font_type="monospace", font_size=15, static_txt="a")
        label.get_surface()
        TextManager().get_render.assert_called_once_with("a", COLORS.BLACK, "monospace", 15)
        self.assertEqual(TextManager().get_default_render.call_count, 0)

    def test_dynamic_label_render(self):
        label = Label(0, 0, COLORS.BLACK, font_type="monospace", font_size=15, dynamic_txt=self.dynamic_txt)
        label.get_surface()
        TextManager().get_render.assert_called_once_with(self.dynamic_txt(), COLORS.BLACK, "monospace", 15)
        self.assertEqual(TextManager().get_default_render.call_count, 1)


if __name__ == '__main__':
    unittest.main()
