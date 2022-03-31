import settings

from pyclick import GameWindow as __GW
from pyclick.controls.timer import Timer


class GameWindow(__GW):
    def __init__(self):
        super().__init__(window_size=settings.WINDOW_SIZE, fps=settings.FPS)
        # self.second_timer = Timer(settings.MAIN_CLOCK, auto_run=True)



