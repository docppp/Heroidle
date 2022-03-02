import unittest
from copy import copy
from unittest.mock import ANY
from unittest.mock import call
from unittest.mock import Mock

from pyclick.gfx.detail import Detail
from pyclick.gfx.complex_scene import ComplexScene
from pyclick.gfx.simple_scene import SimpleScene
from pyclick.wrapg import Graphics


class TestScene(unittest.TestCase):
    #
    # |-D1----|   |-D2----|
    # |  T1|-D3----| T1   |
    # |----|  T2   |------|
    #      |-------|
    # D1 and D2 are copied to overlay
    def setUp(self):
        Graphics.load_image = lambda *args: (None, (800, 600))
        Graphics.draw_on_surface = Mock()
        Detail.get_surface = lambda this: id(this)

        self.details = {
            'D1': Detail(x=100, y=50, width=20, height=10, topness=2),
            'D2': Detail(x=130, y=50, width=20, height=10, topness=1),
            'D3': Detail(x=110, y=55, width=30, height=10, topness=3),
        }
        self.scene = SimpleScene(bg='bg', x=0, y=0, details=list(self.details.values()))

        self.overlay_details = copy(self.details)
        self.overlay_details.pop('D3')
        self.scene_overlay = SimpleScene(bg='bg', x=0, y=0, details=list(self.overlay_details.values()))

        self.multi_scene = ComplexScene([self.scene, self.scene_overlay])

        self.test_params = [
            {'name': 'at_None', 'pos': (99, 56),  'focus': None},
            {'name': 'at_D1',   'pos': (101, 56), 'focus': self.overlay_details['D1']},
            {'name': 'at_D2',   'pos': (141, 56), 'focus': self.overlay_details['D2']},
            {'name': 'at_D3',   'pos': (121, 56), 'focus': self.details['D3']},
            {'name': 'at_D1D3', 'pos': (111, 56), 'focus': self.overlay_details['D1']},
        ]

    def test_layer_focus(self):
        for param in self.test_params:
            with self.subTest(param):
                self.assertEqual(self.multi_scene.check_focus(param['pos']), param['focus'])

    @staticmethod
    def draw_args(det):
        return det.get_surface(), (det.x, det.y)

    def test_draw_multi_layer(self):
        win = Mock()
        self.multi_scene.draw_all(win)

        calls = [
            call(win, None, (0, 0)),  # layer bg
            call(ANY, *self.draw_args(self.details['D2'])),
            call(ANY, *self.draw_args(self.details['D1'])),
            call(ANY, *self.draw_args(self.details['D3'])),
            call(win, ANY, (0, 0)),  # subsurface with details to window
            call(win, None, (0, 0)),  # overlay bg
            call(ANY, *self.draw_args(self.overlay_details['D2'])),
            call(ANY, *self.draw_args(self.overlay_details['D1'])),
            call(win, ANY, (0, 0)),  # overlay subsurface with details to window
        ]
        Graphics.draw_on_surface.assert_has_calls(calls)
        self.assertEqual(Graphics.draw_on_surface.call_count, len(calls))

        # TODO:
        # test moving details
        # test focus sub-scenes



