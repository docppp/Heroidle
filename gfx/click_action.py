from utils import static_class
from .scene_maker import SceneMaker


@static_class
class ClickAction:

    def no_action():
        pass

    def goto_red(window):
        from .scenes_details import SceneRed
        window.active_scene = SceneMaker().create_scene(SceneRed)

    def goto_green(window):
        from .scenes_details import SceneGreen
        window.active_scene = SceneMaker().create_scene(SceneGreen)

    def goto_blue(window):
        from .scenes_details import SceneBlue, SceneBlueWindow
        window.active_scene = SceneMaker().create_scene(SceneBlue)
        window.draw()
        window.active_scene = SceneMaker().create_scene(SceneBlueWindow)

    def goto_yellow(window):
        from .scenes_details import SceneYellow
        window.active_scene = SceneMaker().create_scene(SceneYellow)

    def goto_main(window):
        from .scenes_details import SceneMain
        window.active_scene = SceneMaker().create_scene(SceneMain.restore())

    def close_blue_window(window):
        from .scenes_details import SceneBlue
        window.active_scene = SceneMaker().create_scene(SceneBlue)


@static_class
class TextFormatter:

    def seconds_since_startup():
        from main_window import MainWindow
        sec = MainWindow().second_timer.counter
        return f"Elapsed: {sec} sec"




