from game.nairobi_police_game import NairobiPoliceGame
from network.multiplayer import MultiplayerManager

def display_nairobi_police_quest():
    # Remove the 'r' before the string to interpret escape sequences correctly
    print("\033[36m")
    print(r"""
  _   _    _    ___ ____   ___  ____ ___   ____   ___  _     ___ ____ _____    ___  _   _ _____ ____ _____ 
 | \ | |  / \  |_ _|  _ \ / _ \| __ |_ _| |  _ \ / _ \| |   |_ _/ ___| ____|  / _ \| | | | ____/ ___|_   _|
 |  \| | / _ \  | || |_) | | | |  _ \| |  | |_) | | | | |    | | |   |  _|   | | | | | | |  _| \___ \ | |  
 | |\  |/ ___ \ | ||  _ <| |_| | |_) | |  |  __/| |_| | |___ | | |___| |___  | |_| | |_| | |___ ___) || |  
 |_| \_/_/   \_|___|_| \_\\___/|____|___| |_|    \___/|_____|___\____|_____|  \__\_\\___/|_____|____/ |_|  
    """)
    print("\033[0m")
    print("\nWelcome to the Nairobi Police Quest!")
    print("Press 'h' for help during the game")
    print("Press 'q' to quit the game at any instance. \033[91m(NOTE: Your progress won't be saved)\033[0m")


if __name__ == "__main__":
    display_nairobi_police_quest()
    game = NairobiPoliceGame()
    print("Do you want to play multiplayer? (y/n)")
    choice = game.get_player_input("Enter your choice: ").lower()
    if choice == 'y':
        player_name = game.get_player_input("Enter your name: ")
        multiplayer = MultiplayerManager(game, player_name)
        print("Do you want to (1) host or (2) join a game?")
        host_or_join = game.get_player_input("Enter your choice (1/2): ")
        if host_or_join == '1':
            multiplayer.host_game()
        else:
            multiplayer.join_game()
    else:
        game.start_game()
