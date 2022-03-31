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


class Client:
    def __init__(self):
        self.socket: zmq.Socket = None
        self.connect_to_server()

    def send_message(self, message: str):
        print(f"Sending {getsizeof(message)} bytes: {message}")
        msg = message.encode()
        self.socket.send(msg)
        ans = bytes(self.socket.recv()).decode()
        return ans

    def connect_to_server(self):
        print("Connecting to Server on port 5050")
        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.connect("tcp://127.0.0.1:5050")

    def req_create_player(self, username, password):
        message = f"msgId:0x01;desc:player_create;args:'{username}','{password}'"
        ans = self.send_message(message)
        return ans

    def req_player_update(self, username):
        message = f"msgId:0x02;player:{username}"
        ans = self.send_message(message)
        return ans


def main():
    client = Client()
    player_json = client.req_create_player("user123", "pass123")
    print(player_json)

    sleep(4)

    def update_players():
        ans = client.req_player_update("user123")
        print(ans)
    timer = Timer(1, True, update_players)
    while True:
        sleep(0.1)


if __name__ == '__main__':
    main()
