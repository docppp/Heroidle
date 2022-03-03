import threading
from typing import TYPE_CHECKING

from pyclick.wrapg import Events

if TYPE_CHECKING:
    from pyclick.game_window import GameWindow


def default_send_timer_event_func():
    from .event_maps import custom_events
    Events.send_event_id(custom_events['timer_event'])


class Timer:

    def __init__(self, interval, auto_run=False, function=default_send_timer_event_func):
        self.interval = interval
        self.function = function
        self.stopped = threading.Event()
        self.counter = 0
        if auto_run:
            self.run()

    def wait_and_call(self):
        while not self.stopped.isSet():
            self.stopped.wait(self.interval)
            self.function()
            self.counter += 1

    def run(self):
        t = threading.Timer(0, self.wait_and_call)
        t.daemon = True
        t.start()

    def stop(self):
        self.stopped.set()

    @staticmethod
    def event_timer_passed(window: 'GameWindow'):
        # print(f"{datetime.now().time()} time to read shm!")
        pass



