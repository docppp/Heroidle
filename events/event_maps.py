from wrapg import Events
from .mouse import Mouse
from .timer import Timer

custom_events = {
    'timer_event': Events.user_event(1),
}

_callback_table = {
    Events.QUIT:                        Events.quit,
    Events.MOUSE_PRESS:                 Mouse.event_mouse_press,
    Events.MOUSE_RELEASE:               Mouse.event_mouse_release,
    Events.MOUSE_MOVE:                  Mouse.event_mouse_move,
    custom_events['timer_event']:       Timer.event_timer_passed,
}


def get_event_callback(event: Events.DefaultEvent):
    return _callback_table.get(event.get_id(), None)
