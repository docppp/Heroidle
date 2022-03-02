class ClickAction:

    @staticmethod
    def no_action(*args):
        pass

    # @staticmethod
    # def goto_blue(window):
    #     from scenes_details import SceneBlue, SceneBlueWindow
    #     window.active_scene = SceneMaker().create_scene(SceneBlue)
    #     window.draw()
    #     window.active_scene = SceneMaker().create_scene(SceneBlueWindow)


class TextFormatter:

    @staticmethod
    def seconds_since_startup():
        from your_game import YourGame
        sec = YourGame().second_timer.counter
        return f"Elapsed: {sec} sec"




