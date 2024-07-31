#!/usr/bin/env python3
import socket
import threading


class MultiplayerManager:
    def _init_(self, game):
        self.game = game
        self.server = None
        self.client = None

    def host_game(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", 9999))
        self.server.listen(1)
        print("Waiting for a player to join...")
        self.client, _ = self.server.accept()
        print("Player joined! Starting the game...")
        self.start_multiplayer_game()

    def join_game(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("localhost", 9999))
        print("Connected to the host! Starting the game...")
        self.start_multiplayer_game()

    def start_multiplayer_game(self):
        threading.Thread(target=self.handle_client, args=(self.client,)).start()
        self.game.start_game()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if data:
                    print(f"Received: {data.decode()}")
            except:
                print("Connection lost.")
                break