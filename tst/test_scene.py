from copy import copy
from unittest.mock import Mock, call

import pytest

from gfx.detail import Detail
from gfx.scene import Scene
from wrapg import Graphics


class TestScene:
    #
    # |-D1----|   |-D2----|
    # |  T1|-D3----| T1   |
    # |----|  T2   |------|
    #      |-------|
    #

    details = {
        'D1': Detail(x=100, y=50, _width=20, _height=10, topness=1),
        'D2': Detail(x=130, y=50, _width=20, _height=10, topness=1),
        'D3': Detail(x=110, y=55, _width=30, _height=10, topness=2),
    }

    overlay_details = copy(details)
    overlay_details.pop('D3')

    mouse_pos = {
        'at_None': (99, 56),
        'at_D1': (101, 56),
        'at_D2': (141, 56),
        'at_D3': (121, 56),
        'at_D1D3': (111, 56),
        'at_D2D3': (131, 56),
    }

    @pytest.fixture
    def scene(self):
        Graphics.load_image = lambda *args: (None, (800, 600))
        scene = Scene("")
        scene._details = list(TestScene.details.values())
        return scene

    @pytest.fixture
    def multi_scene(self):
        Graphics.load_image = lambda *args: (None, (800, 600))
        multi_scene = Scene("")
        multi_scene._details = list(TestScene.details.values())
        scene_overlay = Scene("")
        scene_overlay._details = list(self.overlay_details.values())
        multi_scene._overlays = [scene_overlay]
        return multi_scene

    def test_single_layer_focus(self, scene):
        assert scene.check_focus(self.mouse_pos['at_None']) is None
        assert scene.check_focus(self.mouse_pos['at_D1']) == self.details['D1']
        assert scene.check_focus(self.mouse_pos['at_D2']) == self.details['D2']
        assert scene.check_focus(self.mouse_pos['at_D3']) == self.details['D3']
        assert scene.check_focus(self.mouse_pos['at_D1D3']) == self.details['D3']
        assert scene.check_focus(self.mouse_pos['at_D2D3']) == self.details['D3']

    def test_multi_layer_focus(self, multi_scene):
        assert multi_scene.check_focus(self.mouse_pos['at_None']) is None
        assert multi_scene.check_focus(self.mouse_pos['at_D1']) == self.overlay_details['D1']
        assert multi_scene.check_focus(self.mouse_pos['at_D2']) == self.overlay_details['D2']
        assert multi_scene.check_focus(self.mouse_pos['at_D3']) == self.details['D3']
        assert multi_scene.check_focus(self.mouse_pos['at_D1D3']) == self.overlay_details['D1']
        assert multi_scene.check_focus(self.mouse_pos['at_D2D3']) == self.overlay_details['D2']

    def test_inactive_layer(self, scene):
        scene.active = False
        for pos in self.mouse_pos.values():
            assert scene.check_focus(pos) is None

    @staticmethod
    def draw_setup():
        Graphics.draw_on_surface = Mock()
        Detail.get_surface = lambda this: id(this)

    @staticmethod
    def draw_args(det):
        return id(det), (det.x, det.y)

    def test_draw_all(self, scene):
        self.draw_setup()
        win = Mock()
        scene.draw_all(win)

        calls = [
            call(win, None, (0, 0)),  # layer bg
            call(win, *self.draw_args(self.details['D1'])),
            call(win, *self.draw_args(self.details['D2'])),
            call(win, *self.draw_args(self.details['D3'])),
        ]
        Graphics.draw_on_surface.assert_has_calls(calls)
        assert Graphics.draw_on_surface.call_count == len(calls)

    def test_draw_only_active(self, scene):
        self.draw_setup()
        win = Mock()
        scene._details[1].active = False  # disable D2
        scene.draw_all(win)

        calls = [
            call(win, None, (0, 0)),  # layer bg
            call(win, *self.draw_args(self.details['D1'])),
            call(win, *self.draw_args(self.details['D3'])),
        ]
        Graphics.draw_on_surface.assert_has_calls(calls)
        assert Graphics.draw_on_surface.call_count == len(calls)
        scene._details[1].active = True  # enable D2

    def test_draw_multi_layer(self, multi_scene):
        self.draw_setup()
        win = Mock()
        multi_scene.draw_all(win)

        calls = [
            call(win, None, (0, 0)),  # layer bg
            call(win, *self.draw_args(self.details['D1'])),
            call(win, *self.draw_args(self.details['D2'])),
            call(win, *self.draw_args(self.details['D3'])),
            call(win, None, (0, 0)),  # overlay bg
            call(win, *self.draw_args(self.overlay_details['D1'])),
            call(win, *self.draw_args(self.overlay_details['D2'])),
        ]
        Graphics.draw_on_surface.assert_has_calls(calls)
        assert Graphics.draw_on_surface.call_count == len(calls)




