import pygame as pg


class Events:

    class DefaultEvent:
        __slots__ = '_pg_event'

        def __init__(self, event: pg.event.Event):
            self._pg_event = event

        def get_id(self) -> int:
            return self._pg_event.type

    class MouseEvent(DefaultEvent):
        __slots__ = 'button', 'pos'

        def __init__(self, event: pg.event.Event):
            super().__init__(event)
            self.button = event.button
            self.pos = event.pos

    @staticmethod
    def get_all() -> list[DefaultEvent]:
        events = []
        for event in pg.event.get():
            if event.type in [Events.MOUSE_PRESS, Events.MOUSE_RELEASE]:
                events.append(Events.MouseEvent(event))
            else:
                events.append(Events.DefaultEvent(event))
        return events

    @staticmethod
    def send_event_id(event_id: int) -> None:
        event_to_send = pg.event.Event(event_id)
        pg.event.post(event_to_send)

    @staticmethod
    def user_event(event_id: int) -> int:
        return pg.USEREVENT + event_id

    @staticmethod
    def get_mouse_pos() -> tuple[int, int]:
        return pg.mouse.get_pos()

    @staticmethod
    def quit(window):
        pg.display.quit()
        pg.quit()
        exit()

    QUIT = pg.QUIT
    MOUSE_PRESS = pg.MOUSEBUTTONDOWN
    MOUSE_RELEASE = pg.MOUSEBUTTONUP
    MOUSE_MOVE = pg.MOUSEMOTION
    BUTTON_LEFT = 1
    BUTTON_WHEEL_UP = 4
    BUTTON_WHEEL_DOWN = 5
