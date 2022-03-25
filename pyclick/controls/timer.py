import threading


class Timer:

    def __init__(self, interval, auto_run=False, function=lambda: None):
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
