from dataclasses import dataclass


@dataclass
class Resource:
    amount: int
    on_hand: int
    on_hand_max: int


class Warehouse:
    def __init__(self):
        self.lvl = 1
        self.gold = Resource(1000, 0, 100)
        self.stone = Resource(1000, 0, 100)
        self.wood = Resource(1000, 0, 100)


class Kingdom:
    def __init__(self):
        self.cityhall = 1
        self.goldmine = 1
        self.stonemine = 1
        self.sawmill = 1
        self.trainingroom = 0


class Character:
    def __init__(self):
        self.lvl = 1
        self.exp = 0
        self.honor = 0
        self.mission = None


class Player:
    def __init__(self, username):
        self.user = username
        self.character = Character()
        self.kingdom = Kingdom()
        self.warehouse = Warehouse()

    def update(self):
        self.warehouse.gold.on_hand += self.kingdom.goldmine*10
        self.warehouse.stone.on_hand += self.kingdom.stonemine*10
        self.warehouse.wood.on_hand += self.kingdom.sawmill*10
        if self.warehouse.gold.on_hand > self.warehouse.gold.on_hand_max: self.warehouse.gold.on_hand = self.warehouse.gold.on_hand_max
        if self.warehouse.stone.on_hand > self.warehouse.stone.on_hand_max: self.warehouse.stone.on_hand = self.warehouse.stone.on_hand_max
        if self.warehouse.wood.on_hand > self.warehouse.wood.on_hand_max: self.warehouse.wood.on_hand = self.warehouse.wood.on_hand_max

    def to_json(self):
        return f'''{{
  "user": "{self.user}",
  "character": {{"lvl": {self.character.lvl},"exp": {self.character.exp},"honor": {self.character.honor},"mission": {{}},
  "kingdom": {{"cityhall": {self.kingdom.cityhall},"goldmine": {self.kingdom.goldmine},"stonemine": {self.kingdom.stonemine},"sawmill": {self.kingdom.sawmill},"trainingroom": {self.kingdom.trainingroom}}},
  "warehouse": {{
    "gold": {{"amount": {self.warehouse.gold.amount},"onhand": {self.warehouse.gold.on_hand},"onhandmax": {self.warehouse.gold.on_hand_max},"income": 10}},
    "stone": {{"amount": {self.warehouse.stone.amount},"onhand": {self.warehouse.stone.on_hand},"onhandmax": {self.warehouse.stone.on_hand_max},"income": 10}},
    "wood": {{"amount": {self.warehouse.wood.amount},"onhand": {self.warehouse.wood.on_hand},"onhandmax": {self.warehouse.wood.on_hand_max},"income": 10}}
  }}
}}'''


