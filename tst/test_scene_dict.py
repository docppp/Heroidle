import unittest

from gfx.detail import Detail
from gfx.scene_dict import SceneDict


class TestSceneDict(unittest.TestCase):

    def test_relative_scene_position(self):
        sample_dict = SceneDict([
            ('bg', 'background.png'),
            ('start_pos', (300, 100)),
            ('details', [
                Detail(0, 0),
                Detail(100, 80),
            ]),
        ])
        self.assertEqual(sample_dict['details'][0].x, 300)
        self.assertEqual(sample_dict['details'][0].y, 100)
        self.assertEqual(sample_dict['details'][1].x, 400)
        self.assertEqual(sample_dict['details'][1].y, 180)

    def test_restore_scene(self):
        sample_dict = SceneDict([
            ('bg', 'background.png'),
            ('restorable', True),
            ('details', [
                Detail(0, 0),
                Detail(100, 80),
            ]),
        ])
        sample_dict['details'][0].change_pos_by((40, 30))
        sample_dict['details'][0].set_pos((10, 20))
        sample_dict.restore()
        self.assertEqual(sample_dict['details'][0].x, 0)
        self.assertEqual(sample_dict['details'][0].y, 0)
        self.assertEqual(sample_dict['details'][1].x, 100)
        self.assertEqual(sample_dict['details'][1].y, 80)

    def test_restore_scene_without_key(self):
        sample_dict = SceneDict([
            ('bg', 'background.png'),
            ('details', [Detail(0, 0)]),
        ])
        with self.assertRaises(KeyError):
            sample_dict.restore()


if __name__ == '__main__':
    unittest.main()
