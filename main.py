# TODO:
#  - custom eventy          https://stackoverflow.com/questions/23571956/pygame-way-to-create-more-userevent-type-events
#  - pygame adapter?
#  - logging
import settings
from client import Client
from game import GameWindow

import pygame as pg  # cannot get rid of it due to init below

from pyclick.controls.timer import Timer

pg.init()
update_req = False


def main():
    global update_req
    game = GameWindow()
    client = Client()
    client.connect_to_server()
    client.req_create_player("user123", "pass123")

    def get_update():
        global update_req
        update_req = True

    second_timer = Timer(settings.MAIN_CLOCK, auto_run=True, function=get_update)
    while True:
        game.mainLoop()
        if update_req:
            ans = client.req_player_update()
            update_req = False


if __name__ == '__main__':
    main()
