import threading

from wrapg import Events


def default_send_timer_event_func():
    from .event_maps import custom_events
    Events.send_event_id(custom_events['timer_event'])


class Timer:

    def __init__(self, interval, function=default_send_timer_event_func):
        self.interval = interval
        self.function = function
        self.stopped = threading.Event()
        self.counter = 0

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
    def event_timer_passed(window):
        # print(f"{datetime.now().time()} time to read shm!")
        pass




