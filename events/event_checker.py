from inspect import signature

from wrapg.events import Events


class EventChecker:

    def __init__(self, window):
        self.window = window

    def process_event(self, event):
        try:
            from .event_maps import function_event
            fun = function_event.get(event.get_id())
            sig = signature(fun)
            if str(sig) == '(window)':
                fun(self.window)
            elif str(sig) == '(window, event)':
                fun(self.window, event)
            else:
                raise NotImplementedError("Some kind of new event?")

        except TypeError:  # startup and some other pygame events
            pass

    def check_quit(window):
        Events.quit()
        exit()






