from pyclick.wrapg import Graphics


class Detail:
    __slots__ = 'x', 'y', 'width', 'height', 'rect', 'topness', 'active', 'movable', 'mouse_hold', 'on_click'

    def __init__(self, x, y, width, height, topness=1, active=True, movable=False, on_click=lambda *args: None):
        # gfx properties
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = Graphics.create_rect(self.x, self.y, self.width, self.height)

        # behaviour
        self.topness = topness
        self.active = active
        self.movable = movable
        self.on_click = on_click

    def change_pos_by(self, delta_pos: tuple[int, int]):
        self.x += delta_pos[0]
        self.y += delta_pos[1]
        self.update_rect()

    def set_pos(self, new_pos: tuple[int, int]):
        self.x = new_pos[0]
        self.y = new_pos[1]
        self.update_rect()

    def get_surface(self):
        return self.rect

    def is_focused(self, mouse_x: int, mouse_y: int):
        if self.active and (self.x < mouse_x < self.x + self.width) and (self.y < mouse_y < self.y + self.height):
            return True
        self.mouse_hold = False
        return False

    def update_rect(self):
        # self.rect._pg_rect.update(self.x, self.y, self.width, self.height)
        self.rect = Graphics.create_rect(self.x, self.y, self.width, self.height)
