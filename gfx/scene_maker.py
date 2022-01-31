from gfx.scene import Scene
from .scene_dict import SceneDict


class SceneMaker:

    @staticmethod
    def create_scene(params: SceneDict) -> Scene:
        try:
            start_pos_x, start_pos_y = params['start_pos']
            scene = Scene(params['bg'], start_pos_x, start_pos_y)
        except KeyError:  # no start_pos defined
            scene = Scene(params['bg'])

        scene._details += params['details']  # intentional use of protected member

        if 'overlays' in params:
            for overlay in params['overlays']:
                layer = SceneMaker.create_scene(overlay)
                scene._overlays.append(layer)  # intentional use of protected member

        return scene



