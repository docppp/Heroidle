from inspect import signature

from pygame.time import Clock

from pyclick.utils import Singleton
from pyclick.wrapg import Events
from pyclick.wrapg import Graphics
from .events.event_maps import get_event_callback
from .gfx.text_manager import TextManager


class GameWindow(metaclass=Singleton):
    def __init__(self, window_size, fps):
        self.window = Graphics.main_window("dupa cicho", window_size)
        self.FPS = fps
        self.clock = Clock()
        self.focused_detail = None
        self.active_scene = None
        self.text_manager = TextManager()

    def mainLoop(self):
        self.clock.tick(self.FPS)
        self.draw()

        for event in Events.get_all():
            self.process_event(event)

    def draw(self):
        self.active_scene.draw_all(self.window)
        Graphics.update_display()

    def process_event(self, event):
        # TODO:
        # shieeeeet
        fun = get_event_callback(event)
        if fun is None:
            return
        sig = signature(fun)
        print(sig)
        if str(sig) == "(window: 'GameWindow')":
            fun(self)
        elif str(sig) == "(window: 'GameWindow', event: pyclick.wrapg.events.Events.MouseEvent)":
            fun(self, event)
        else:
            raise NotImplementedError("Some kind of new event?")
