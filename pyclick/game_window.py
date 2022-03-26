from pygame.time import Clock

from pyclick.utils import Singleton, get_types_of_function_args
from pyclick.wrapg import Events
from pyclick.wrapg import Graphics
from .controls.mouse import Mouse


class GameWindow(metaclass=Singleton):
    def __init__(self, window_size, fps):
        self.window = Graphics.main_window("dupa cicho", window_size)
        self.FPS = fps
        self.clock = Clock()
        self.focused_detail = None
        self.active_scene = None

    def mainLoop(self):
        self.clock.tick(self.FPS)
        self.draw()

        for event in Events.get_all():
            self.process_event(event)

    def draw(self):
        if self.active_scene:
            self.active_scene.draw_all(self.window)
        Graphics.update_display()

    def process_event(self, event):
        fun = self._get_event_callback(event)
        if fun is None:
            return

        fun_args_map = {
            GameWindow: self,
            Events.MouseEvent: event
        }

        param_types = get_types_of_function_args(fun)

        try:
            args = [fun_args_map[eval(param)] for param in param_types]
        except TypeError:
            print(f"Cannot eval params of {fun}: {param_types}")
            args = []

        fun(*args)

    __callback_table = {
        Events.QUIT: Events.quit,
        Events.MOUSE_PRESS: Mouse.event_mouse_press,
        Events.MOUSE_RELEASE: Mouse.event_mouse_release,
        Events.MOUSE_MOVE: Mouse.event_mouse_move,
    }

    @staticmethod
    def _get_event_callback(event: Events.DefaultEvent):
        return GameWindow.__callback_table.get(event.get_id(), None)
