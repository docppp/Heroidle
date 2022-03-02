from pyclick.gfx.abstract_scene import AbstractScene
from pyclick.gfx.detail import Detail
from pyclick.wrapg.graphics import Graphics


class Scrollable(AbstractScene):
    def __init__(self, scene, scroll_max):
        self.scene = scene
        self.scroll_max = scroll_max
        self.current_scroll = 0
        self.scroll_bar = Detail(self.scene.width-7, 0, 7, int(self.scene.height**2/(self.scroll_max+self.scene.height)))

    def check_focus(self, mouse_pos: tuple[int, int]):
        return self.scene.check_focus(mouse_pos)

    def check_focus_overlay(self, mouse_pos: tuple[int, int]):
        return self.scene.check_focus_overlay(mouse_pos)

    def move_detail_by(self, detail, delta_pos, mouse_pos):
        det = [det for det in self.scene.details if det is detail]
        if len(det) == 0 or self.check_focus_overlay(mouse_pos) is False:
            return
        det = det[0]
        det.change_pos_by(delta_pos)
        if det.y < -self.scroll_max: det.set_pos((det.x, -self.scroll_max))
        if det.x < 0: det.set_pos((0, det.y))
        if det.y > self.scene.height - det.height: det.set_pos((det.x, self.scene.height - det.height))
        if det.x > self.scene.width - det.width: det.set_pos((self.scene.width - det.width, det.y))

    def draw_all(self, window: Graphics.Surface):
        self.scene.details.append(self.scroll_bar)
        self.scene.draw_all(window)
        self.scene.details.pop()

    def scroll_by(self, mouse_pos, dy):
        if self.check_focus_overlay(mouse_pos) is False:
            return
        if self.current_scroll + dy > self.scroll_max or self.current_scroll + dy < 0:
            return
        self.current_scroll += dy
        self.scroll_bar.change_pos_by((0, dy*(self.scene.height/(self.scroll_max+self.scene.height))))
        for det in self.scene.details:
            self.move_detail_by(det, (0, -dy), mouse_pos)
