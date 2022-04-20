import settings
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from pyclick import GameWindow
from pyclick.controls.timer import Timer
from pyclick import SceneMaker
from scenes import s




class YourGame(GameWindow):
    def __init__(self):
        super(YourGame, self).__init__(window_size=settings.WINDOW_SIZE, fps=settings.FPS)
        self.second_timer = Timer(settings.MAIN_CLOCK, auto_run=True)
        self.active_scene = SceneMaker.create_scene(s)



