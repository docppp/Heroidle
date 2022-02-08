import pytest

from gfx.detail import Detail


class TestDetail:

    @pytest.fixture
    def detail(self):
        return Detail(x=100, y=50, _width=10, _height=10)

    def test_change_position(self, detail):
        detail.change_pos_by((1, -1))
        assert detail.x == 101
        assert detail.y == 49

    def test_set_position(self, detail):
        detail.set_pos((1, 1))
        assert detail.x == 1
        assert detail.y == 1

    def test_focus(self, detail):
        assert detail.is_focused(99, 49) is False
        assert detail.is_focused(99, 51) is False
        assert detail.is_focused(99, 61) is False

        assert detail.is_focused(101, 49) is False
        assert detail.is_focused(101, 51) is True
        assert detail.is_focused(101, 61) is False

        assert detail.is_focused(111, 49) is False
        assert detail.is_focused(111, 51) is False
        assert detail.is_focused(111, 61) is False

    def test_inactive_focus(self, detail):
        detail.active = False
        assert detail.is_focused(101, 51) is False
