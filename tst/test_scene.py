import unittest
from copy import copy
from unittest.mock import call
from unittest.mock import Mock

from gfx.detail import Detail
from gfx.scene import Scene
from wrapg import Graphics


class TestScene(unittest.TestCase):
    #
    # |-D1----|   |-D2----|
    # |  T1|-D3----| T1   |
    # |----|  T2   |------|
    #      |-------|
    #
    def setUp(self):
        Graphics.load_image = lambda *args: (None, (800, 600))
        Graphics.draw_on_surface = Mock()
        Detail.get_surface = lambda this: id(this)

        self.details = {
            'D1': Detail(x=100, y=50, _width=20, _height=10, topness=2),
            'D2': Detail(x=130, y=50, _width=20, _height=10, topness=1),
            'D3': Detail(x=110, y=55, _width=30, _height=10, topness=3),
        }
        self.scene = Scene("")
        self.scene._details = list(self.details.values())

        self.overlay_details = copy(self.details)
        self.overlay_details.pop('D3')
        scene_overlay = Scene("")
        scene_overlay._details = list(self.overlay_details.values())

        self.multi_scene = copy(self.scene)
        self.multi_scene._overlays = [scene_overlay]

        self.test_params = [
            {'name': 'at_None', 'pos': (99, 56),  'single_focus': None,               'multi_focus': None},
            {'name': 'at_D1',   'pos': (101, 56), 'single_focus': self.details['D1'], 'multi_focus': self.overlay_details['D1']},
            {'name': 'at_D2',   'pos': (141, 56), 'single_focus': self.details['D2'], 'multi_focus': self.overlay_details['D2']},
            {'name': 'at_D3',   'pos': (121, 56), 'single_focus': self.details['D3'], 'multi_focus': self.details['D3']},
            {'name': 'at_D1D3', 'pos': (111, 56), 'single_focus': self.details['D3'], 'multi_focus': self.overlay_details['D1']},
            {'name': 'at_None', 'pos': (131, 56), 'single_focus': self.details['D3'], 'multi_focus': self.overlay_details['D2']},
        ]

    def test_single_layer_focus(self):
        for param in self.test_params:
            with self.subTest(param):
                self.assertEqual(self.scene.check_focus(param['pos']), param['single_focus'])

    def test_multi_layer_focus(self):
        for param in self.test_params:
            with self.subTest(param):
                self.assertEqual(self.multi_scene.check_focus(param['pos']), param['multi_focus'])

    def test_inactive_layer(self):
        self.scene.active = False
        for param in self.test_params:
            with self.subTest(param):
                self.assertEqual(self.scene.check_focus(param['pos']), None)

    @staticmethod
    def draw_args(det):
        return det.get_surface(), (det.x, det.y)

    def test_draw_all(self):
        win = Mock()
        self.scene.draw_all(win)

        calls = [
            call(win, None, (0, 0)),  # layer bg
            call(win, *self.draw_args(self.details['D2'])),
            call(win, *self.draw_args(self.details['D1'])),
            call(win, *self.draw_args(self.details['D3'])),
        ]
        Graphics.draw_on_surface.assert_has_calls(calls)
        self.assertEqual(Graphics.draw_on_surface.call_count, len(calls))

    def test_draw_only_active(self):
        win = Mock()
        self.scene._details[1].active = False  # disable D2
        self.scene.draw_all(win)

        calls = [
            call(win, None, (0, 0)),  # layer bg
            call(win, *self.draw_args(self.details['D1'])),
            call(win, *self.draw_args(self.details['D3'])),
        ]
        Graphics.draw_on_surface.assert_has_calls(calls)
        self.assertEqual(Graphics.draw_on_surface.call_count, len(calls))

    def test_draw_multi_layer(self):
        win = Mock()
        self.multi_scene.draw_all(win)

        calls = [
            call(win, None, (0, 0)),  # layer bg
            call(win, *self.draw_args(self.details['D2'])),
            call(win, *self.draw_args(self.details['D1'])),
            call(win, *self.draw_args(self.details['D3'])),
            call(win, None, (0, 0)),  # overlay bg
            call(win, *self.draw_args(self.overlay_details['D2'])),
            call(win, *self.draw_args(self.overlay_details['D1'])),
        ]
        Graphics.draw_on_surface.assert_has_calls(calls)
        self.assertEqual(Graphics.draw_on_surface.call_count, len(calls))




