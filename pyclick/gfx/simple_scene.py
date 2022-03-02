import pygame

from pyclick.gfx.abstract_scene import AbstractScene
from pyclick.wrapg.graphics import Graphics


class SimpleScene(AbstractScene):
    __slots__ = 'bg', 'x', 'y', 'details', 'active', 'image', 'width', 'height', 'rect'

    def __init__(self, bg, x, y, details=None, active=True):
        self.bg = bg
        self.x = x
        self.y = y
        self.details = details if details is not None else []
        self.active = active
        self.image, (self.width, self.height) = Graphics.load_image(self.bg)
        self.rect = Graphics.create_rect(self.x, self.y, self.width, self.height)

    def check_focus(self, mouse_pos: tuple[int, int]):
        if self.active:
            pos_x, pos_y = mouse_pos[0] - self.x, mouse_pos[1] - self.y
            under_mouse = [det for det in self.details if det.is_focused(pos_x, pos_y)]
            if under_mouse:
                return max(under_mouse, key=lambda item: item.topness)
        return None

    def check_focus_overlay(self, mouse_pos: tuple[int, int]):
        if self.active and \
                (self.x < mouse_pos[0] < self.x + self.width) and \
                (self.y < mouse_pos[1] < self.y + self.height):
            return True
        return False

    def move_detail_by(self, detail, delta_pos, mouse_pos):
        det = [det for det in self.details if det is detail]
        if len(det) == 0 or self.check_focus_overlay(mouse_pos) is False:
            return
        det = det[0]
        x, y = mouse_pos[0] - self.x - det.width/2, mouse_pos[1] - self.y - det.height/2
        det.set_pos((x, y))
        if det.y < 0: det.set_pos((det.x, 0))
        if det.x < 0: det.set_pos((0, det.y))
        if det.y > self.height - det.height: det.set_pos((det.x, self.height - det.height))
        if det.x > self.width - det.width: det.set_pos((self.width - det.width, det.y))

    def draw_all(self, window: Graphics.Surface):
        if self.active:
            Graphics.draw_on_surface(window, self.image, (self.x, self.y))
            surf = self._prepare_detailed_surface()
            Graphics.draw_on_surface(window, surf, (self.x, self.y))

    def _prepare_detailed_surface(self):
        surf = Graphics.Surface(pygame.Surface((self.width, self.height), flags=pygame.SRCALPHA))
        self.details.sort(key=lambda item: item.topness)
        for det in self.details:
            if det.active:
                Graphics.draw_on_surface(surf, det.get_surface(), (det.x, det.y))
        return surf
