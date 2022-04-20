from sys import getsizeof
from time import sleep
import zmq

import threading


class Timer:

    def __init__(self, interval, auto_run=False, function=lambda: None):
        self.interval = interval
        self.function = function
        self.stopped = threading.Event()
        self.counter = 0
        if auto_run:
            self.run()

    def wait_and_call(self):
        while not self.stopped.isSet():
            self.stopped.wait(self.interval)
            self.function()
            self.counter += 1

    def run(self):
        t = threading.Timer(0, self.wait_and_call)
        t.daemon = True
        t.start()

    def stop(self):
        self.stopped.set()
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


class Server:
    def __init__(self):
        print("Creating Server on port 5050")
        context = zmq.Context()
        self.socket: zmq.Socket = context.socket(zmq.REP)
        self.socket.bind("tcp://127.0.0.1:5050")
        self.players = []
        self.timer = Timer(1, True, self.update_players)

    def update_players(self):
        for player in self.players:
            print("update")
            player.update()

    def receive_loop(self):
        while True:
            rec = self.socket.recv()
            print(f"Received {getsizeof(rec)} bytes: {rec}")
            rec_msg = bytes(rec).decode()
            msgId = rec_msg.split(";")[0].split(":")[1]
            print(f"msgId {msgId}")
            ans = ""
            if msgId == "0x01":
                ans = self.handle_msg_create_player(rec_msg)
            if msgId == "0x02":
                ans = self.handle_msg_update_player(rec_msg)

            print(f"Sending {getsizeof(ans)} bytes: {ans}")
            self.socket.send(ans.encode())

    def handle_msg_create_player(self, msg):
        new_player = Player("user123")
        self.players.append(new_player)
        return new_player.to_json()

    def handle_msg_update_player(self, msg):
        return self.players[0].to_json()


def main():
    server = Server()
    server.receive_loop()


if __name__ == '__main__':
    main()
