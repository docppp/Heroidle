from gfx.animation import Animation
from gfx.click_action import ClickAction
from gfx.image import Image
from gfx.label import Label
from gfx.scene_dict import SceneDict
from gfx.click_action import TextFormatter
from utils import COLORS

SceneMain = SceneDict([
    ('bg', 'bg_grey.png'),
    ('details', [
        Image(x=100, y=420, sprite='sorc_red.png', on_click=ClickAction.goto_red),
        Image(110, 430, 'sorc_red.png', ClickAction.no_action, topness=3, movable=True),
        Image(300, 420, 'sorc_green.png', ClickAction.goto_green, topness=2),
        Image(310, 430, 'sorc_green.png', ClickAction.goto_green),
        Image(500, 420, 'sorc_blue.png', ClickAction.goto_blue),
        Image(700, 420, 'sorc_yellow.png', ClickAction.goto_yellow),
        Animation(50, 50, "fire_gif", ClickAction.no_action, topness=4),
        Animation(75, 50, "fire_gif", ClickAction.no_action, topness=4, current_frame=2),
        Animation(100, 50, "fire_gif", ClickAction.no_action, topness=4, current_frame=4),
        Animation(125, 50, "fire_gif", ClickAction.no_action, topness=4, current_frame=6),
        Animation(150, 50, "fire_gif", ClickAction.no_action, topness=4, current_frame=8),
        Animation(175, 50, "fire_gif", ClickAction.no_action, topness=4, current_frame=10, movable=True),
        Animation(200, 50, "fire_gif", topness=4, current_frame=12),
    ]),
    ('restorable', True),
])

SceneRed = dict([
    ('bg', 'bg_red.png'),
    ('details', [
        Image(820, 520, 'back_arrow.png', ClickAction.goto_main),
    ])
])

SceneGreen = {
    'bg': 'bg_green.png',
    'details': [
        Image(820, 520, 'back_arrow.png', ClickAction.goto_main),
        Label(500, 20, COLORS.BLACK, font_type="monospace", font_size=15, text=TextFormatter.seconds_since_startup)
    ],
}

SceneBlue = {
    'bg': 'bg_blue.png',
    'details': [
        Image(820, 520, 'back_arrow.png', ClickAction.goto_main),
    ],
}

SceneBlueWindow = SceneDict([
    ('bg', 'blue_window_bg.png'),
    ('start_pos', (360, 100)),
    ('details', [
        Image(267, 53, 'blue_window_x.png', ClickAction.close_blue_window),
    ])
])

SceneYellow = SceneDict([
    ('bg', 'bg_yellow.png'),
    ('details', [
        Image(820, 520, 'back_arrow.png', ClickAction.goto_main),
    ]),
    ('overlays', [
        SceneBlueWindow
    ])
])


