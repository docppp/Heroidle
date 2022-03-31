from sys import getsizeof
from time import sleep
import zmq

from pyclick.controls.timer import Timer
from server.player import Player


class Server:
    def __init__(self):
        print("Creating Server on port 5050")
        context = zmq.Context()
        self.socket: zmq.Socket = context.socket(zmq.REP)
        self.socket.bind("tcp://*:5050")
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
