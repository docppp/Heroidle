from pyclick.gfx.abstract_scene import AbstractScene
from pyclick.gfx.complex_scene import ComplexScene
from pyclick.gfx.scrollable import Scrollable
from pyclick.gfx.simple_scene import SimpleScene


class SceneMaker:

    @staticmethod
    def create_scene(params) -> AbstractScene:
        if 'start_pos' in params:
            pos_x, pos_y = params['start_pos']
        else:
            pos_x, pos_y = 0, 0

        if params['type'] is SimpleScene:
            return SimpleScene(bg=params['bg'], x=pos_x, y=pos_y, details=params['details'])

        elif params['type'] is Scrollable:
            scene = SimpleScene(bg=params['bg'], x=pos_x, y=pos_y, details=params['details'])
            return Scrollable(scene, params['scroll'])

        elif params['type'] is ComplexScene:
            scenes = [SceneMaker.create_scene(layer) for layer in params['layers']]
            return ComplexScene(scenes)

        raise KeyError(f"Scene type {params['type']} not known")




