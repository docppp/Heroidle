from inspect import signature

from pygame.time import Clock

import settings
from events.event_maps import get_event_callback
from events.timer import Timer
from gfx.scene_maker import SceneMaker
from gfx.text_manager import TextManager
from scenes_details import SceneMain
from utils.singleton import Singleton
from wrapg import Events
from wrapg import Graphics


class MainWindow(metaclass=Singleton):
    def __init__(self):
        self.window = Graphics.main_window("dupa cicho", settings.WINDOW_SIZE)
        self.FPS = settings.FPS
        self.clock = Clock()
        self.focused_detail = None
        self.second_timer = Timer(settings.MAIN_CLOCK, True)
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
        fun = get_event_callback(event)
        if fun is None:
            return
        sig = signature(fun)
        if str(sig) == '(window)':
            fun(self)
        elif str(sig) == '(window, event)':
            fun(self, event)
        else:
            raise NotImplementedError("Some kind of new event?")

