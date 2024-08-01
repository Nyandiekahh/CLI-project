import socket
import threading
from game.nairobi_police_game import NairobiPoliceGame

class MultiplayerManager:
    def __init__(self, game, player_name):
        self.game = game
        self.player_name = player_name  # Store the player's name
        self.server = None
        self.client = None

    def host_game(self):
        print(f"{self.player_name} is hosting the game.")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("0.0.0.0", 9999))
        self.server.listen(1)
        print("Waiting for a player to join...")
        self.client, _ = self.server.accept()
        self.client.sendall(self.player_name.encode())
        opponent_name = self.client.recv(1024).decode()
        print(f"Player '{opponent_name}' joined! Starting the game...")
        self.start_multiplayer_game()

    def join_game(self):
        print(f"{self.player_name} is joining a game.")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("localhost", 9999))
        opponent_name = self.client.recv(1024).decode()
        self.client.sendall(self.player_name.encode())
        print(f"Connected to host '{opponent_name}'! Starting the game...")
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
