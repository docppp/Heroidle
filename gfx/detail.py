from typing import Any

from dataclassy import dataclass


@dataclass(slots=True)
class Detail:
    x: int
    y: int
    on_click: 'Any' = object()
    topness: int = 1
    active: bool = True
    movable: bool = False
    mouse_hold: bool = False
    _width: int = None
    _height: int = None

    def change_pos_by(self, delta_pos: tuple[int, int]):
        self.x += delta_pos[0]
        self.y += delta_pos[1]

    def set_pos(self, new_pos: tuple[int, int]):
        self.x = new_pos[0]
        self.y = new_pos[1]

    def get_surface(self):
        raise NotImplementedError("No draw_impl in class derived from Detail")

    def is_focused(self, mouse_x: int, mouse_y: int):
        if self.active and (self.x < mouse_x < self.x + self._width) and (self.y < mouse_y < self.y + self._height):
            return True
        self.mouse_hold = False
        return False
