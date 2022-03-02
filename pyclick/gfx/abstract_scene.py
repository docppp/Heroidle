from abc import ABC, abstractmethod


class AbstractScene(ABC):

    @abstractmethod
    def check_focus(self, mouse_pos: tuple[int, int]):
        pass

    @abstractmethod
    def check_focus_overlay(self, mouse_pos: tuple[int, int]):
        pass

    @abstractmethod
    def move_detail_by(self, detail, delta_pos, mouse_pos):
        pass

    @abstractmethod
    def draw_all(self, window):
        pass
