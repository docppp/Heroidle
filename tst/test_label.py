import unittest
from unittest.mock import Mock, call

from gfx.label import Label
from gfx.text_manager import TextManager
from utils import COLORS


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
        calls = [
            call("a", COLORS.BLACK, "monospace", 15)
        ]
        TextManager().get_render.assert_has_calls(calls)
        self.assertEqual(TextManager().get_render.call_count, len(calls))
        self.assertEqual(TextManager().get_default_render.call_count, 0)

    def test_dynamic_label_render(self):
        label = Label(0, 0, COLORS.BLACK, font_type="monospace", font_size=15, dynamic_txt=self.dynamic_txt)
        label.get_surface()
        calls = [
            call(self.dynamic_txt(), COLORS.BLACK, "monospace", 15)
        ]
        TextManager().get_render.assert_has_calls(calls)
        self.assertEqual(TextManager().get_render.call_count, len(calls))
        self.assertEqual(TextManager().get_default_render.call_count, 1)


if __name__ == '__main__':
    unittest.main()
