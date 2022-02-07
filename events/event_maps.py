from wrapg import Events
from .mouse import Mouse
from .timer import Timer


custom_event_ids = {
    'timer_event':  Events.user_event(1),
}

function_table = {
    Events.QUIT:                            Events.quit,
    Events.MOUSE_PRESS:                     Mouse.event_mouse_press,
    Events.MOUSE_RELEASE:                   Mouse.event_mouse_release,
    Events.MOUSE_MOVE:                      Mouse.event_mouse_move,
    custom_event_ids['timer_event']:        Timer.event_timer_passed,
}
