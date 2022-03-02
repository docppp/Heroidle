from click_action import TextFormatter, ClickAction
from pyclick import Animation
from pyclick import ComplexScene
from pyclick import Detail
from pyclick import Label
from pyclick import SceneDict
from pyclick import Scrollable
from pyclick import SimpleScene
from pyclick.utils import COLORS

s1 = SceneDict([
    ('type', SimpleScene),
    ('bg', 'test_bg.png'),
    ('details', [
        Detail(x=100, y=100, width=50, height=50, movable=True),
        Detail(x=-20, y=-20, width=50, height=50, movable=True),
        Label(500, 20, COLORS.BLACK, font_type="monospace", font_size=15, dynamic_txt=TextFormatter.seconds_since_startup),
        Animation(175, 50, "fire_gif", on_click=ClickAction.no_action, topness=4, movable=True),
    ]),
])

s2 = SceneDict([
    ('type', Scrollable),
    ('bg', 'test_layer.png'),
    ('start_pos', (300, 100)),
    ('details', [
        Detail(x=100, y=100, width=50, height=50, movable=True)
    ]),
    ('scroll', 150),
])

s = SceneDict([
    ('type', ComplexScene),
    ('layers', [s1, s2]),
])
