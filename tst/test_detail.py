import unittest

from gfx.detail import Detail


class TestDetail(unittest.TestCase):

    def setUp(self):
        self.detail = Detail(x=100, y=50, _width=10, _height=10)

        self.test_params = [
            {'name': 'top-left', 'pos': (99, 49), 'focus': False},
            {'name': 'top-mid', 'pos': (101, 49), 'focus': False},
            {'name': 'top-right', 'pos': (111, 49), 'focus': False},

            {'name': 'mid-left', 'pos': (99, 51), 'focus': False},
            {'name': 'mid-mid', 'pos': (101, 51), 'focus': True},
            {'name': 'mid-right', 'pos': (111, 51), 'focus': False},

            {'name': 'down-left', 'pos': (99, 61), 'focus': False},
            {'name': 'down-mid', 'pos': (101, 61), 'focus': False},
            {'name': 'down-right', 'pos': (111, 61), 'focus': False},
        ]

    def test_change_position(self):
        self.detail.change_pos_by((1, -1))
        self.assertEqual(self.detail.x, 101)
        self.assertEqual(self.detail.y, 49)

    def test_set_position(self):
        self.detail.set_pos((1, 1))
        self.assertEqual(self.detail.x, 1)
        self.assertEqual(self.detail.y, 1)

    def test_focus(self):
        for param in self.test_params:
            with self.subTest(param):
                self.assertEqual(self.detail.is_focused(*param['pos']), param['focus'])

    def test_inactive_focus(self):
        self.detail.active = False
        for param in self.test_params:
            with self.subTest(param):
                self.assertEqual(self.detail.is_focused(*param['pos']), False)


if __name__ == '__main__':
    unittest.main()
