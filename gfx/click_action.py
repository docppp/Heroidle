from .scene_maker import SceneMaker


class ClickAction:

    @staticmethod
    def no_action():
        pass

    @staticmethod
    def goto_red(window):
        from .scenes_details import SceneRed
        window.active_scene = SceneMaker().create_scene(SceneRed)

    @staticmethod
    def goto_green(window):
        from .scenes_details import SceneGreen
        window.active_scene = SceneMaker().create_scene(SceneGreen)

    @staticmethod
    def goto_blue(window):
        from .scenes_details import SceneBlue, SceneBlueWindow
        window.active_scene = SceneMaker().create_scene(SceneBlue)
        window.draw()
        window.active_scene = SceneMaker().create_scene(SceneBlueWindow)

    @staticmethod
    def goto_yellow(window):
        from .scenes_details import SceneYellow
        window.active_scene = SceneMaker().create_scene(SceneYellow)

    @staticmethod
    def goto_main(window):
        from .scenes_details import SceneMain
        window.active_scene = SceneMaker().create_scene(SceneMain.restore())

    @staticmethod
    def close_blue_window(window):
        from .scenes_details import SceneBlue
        window.active_scene = SceneMaker().create_scene(SceneBlue)


class TextFormatter:

    @staticmethod
    def seconds_since_startup():
        from main_window import MainWindow
        sec = MainWindow().second_timer.counter
        return f"Elapsed: {sec} sec"




