import sys
import os
import subprocess
from datetime import datetime


# TODO:
#  - custom eventy          https://stackoverflow.com/questions/23571956/pygame-way-to-create-more-userevent-type-events
#  - pygame adapter?
#  - logging

# def check_quit(event):
#     if event.type == pygame.QUIT:
#         pygame.quit()
#         return False
#     return True
#
#
# def check_mouse(event):
#     if event.type == pygame.MOUSEBUTTONUP:
#         pos = pygame.mouse.get_pos()
#         print(pos)
#        cpp.stdin.write(f"mouse_event{pos[0]}:{pos[1]}\n")
# def draw(window):
#     window.fill((0, 0, 0))
#     pygame.draw.rect(window, (255, 0, 0), main_rects['red'])
#     pygame.draw.rect(window, (0, 255, 0), main_rects['green'])
#     pygame.draw.rect(window, (0, 0, 255), main_rects['blue'])
#     pygame.display.update()


def main():
    import pygame as pg
    pg.init()
    from main_window import MainWindow
    # cpp = subprocess.Popen(["MouseGetter.exe"],
    #                        stdin=subprocess.PIPE,
    #                        stdout=subprocess.PIPE,
    #                        bufsize=1,
    #                        universal_newlines=True,
    #                        shell=True)
    MainWindow(900, 600).mainLoop()








if __name__ == '__main__':
    main()

