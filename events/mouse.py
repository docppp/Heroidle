from operator import sub

from wrapg.events import Events


class Mouse:
    _mouse_pressed = False
    _mouse_press_pos = (0, 0)

    @staticmethod
    def event_mouse_press(window, event):
        print(f'pressed at {event.pos}')
        Mouse._mouse_press_pos = event.pos
        Mouse._mouse_pressed = True
        if event.button == Events.BUTTON_LEFT:
            if window.focused_detail is not None:
                window.focused_detail.mouse_hold = True

    @staticmethod
    def event_mouse_release(window, event):
        if event.button == Events.BUTTON_LEFT:
            Mouse.left_click(window, event.pos)

        elif event.button == Events.BUTTON_WHEEL_UP:
            Mouse.wheel_up(window, event.pos)

        elif event.button == Events.BUTTON_WHEEL_DOWN:
            Mouse.wheel_down(window, event.pos)

    @staticmethod
    def event_mouse_move(window):
        if window.focused_detail is not None:
            focus_check = not (Mouse._mouse_pressed and window.focused_detail.movable)
            move_check = window.focused_detail.movable and window.focused_detail.mouse_hold
        else:
            focus_check = True
            move_check = False
        if focus_check:
            Mouse.check_hover(window)
        if move_check:
            Mouse.move_detail(window.focused_detail)

    @staticmethod
    def check_hover(window):
        pos = Events.get_mouse_pos()
        focused = window.active_scene.check_focus(pos[0], pos[1])
        if window.focused_detail != focused:
            print(f'{focused} focused')
        window.focused_detail = focused

    @staticmethod
    def move_detail(detail):
        pos = Events.get_mouse_pos()
        dx, dy = map(sub, pos, Mouse._mouse_press_pos)
        detail.x += dx
        detail.y += dy
        Mouse._mouse_press_pos = pos

    @staticmethod
    def left_click(window, pos):
        print(f'released at {pos}')
        Mouse._mouse_pressed = False
        detail = window.focused_detail
        if detail is not None and detail.mouse_hold:
            print(detail)
            detail.mouse_hold = False
            detail.on_click(window)

    @staticmethod
    def wheel_up(window, pos):
        print('u')

    @staticmethod
    def wheel_down(window, pos):
        print('d')
