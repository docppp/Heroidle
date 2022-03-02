
def main():
    import pygame as pg  # cannot get rid of it due to init below
    pg.init()
    from your_game import YourGame

    game = YourGame()
    while True:
        game.mainLoop()


if __name__ == '__main__':
    main()
