from inspect import signature

from pygame.time import Clock

from events import Timer
from gfx import SceneMaker
from gfx import TextManager
from gfx.scenes_details import SceneMain
from utils import Singleton
from wrapg import Events
from wrapg import Graphics


class MainWindow(metaclass=Singleton):
    def __init__(self, win_width, win_height):
        self.window = Graphics.main_window("dupa cicho", (win_width, win_height))
        self.FPS = 24
        self.clock = Clock()
        self.focused_detail = None
        self.second_timer = Timer(1)
        self.second_timer.run()
        self.active_scene = SceneMaker.create_scene(SceneMain)
        self.text_manager = TextManager()

    def draw(self):
        self.active_scene.draw_all(self.window)
        Graphics.update_display()

    def mainLoop(self):
        while True:
            self.clock.tick(self.FPS)
            self.draw()

            for event in Events.get_all():
                self.process_event(event)
            # sleep(0.025)
            # print(self.clock.get_fps())

    def process_event(self, event):
        try:
            from events.event_maps import function_event
            fun = function_event.get(event.get_id())
            sig = signature(fun)
            if str(sig) == '(window)':
                fun(self)
            elif str(sig) == '(window, event)':
                fun(self, event)
            else:
                raise NotImplementedError("Some kind of new event?")
        except TypeError:  # startup and some other pygame events
            pass

