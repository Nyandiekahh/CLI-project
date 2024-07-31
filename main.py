#!/usr/bin/env python3
import pygame
from game_loop import NairobiPoliceGame
from multiplayer import MultiplayerManager

pygame.init()
pygame.mixer.init()

if __name__ == "__main__":
    game = NairobiPoliceGame()
    print("Do you want to play multiplayer? (y/n)")
    if input().lower() == 'y':
        multiplayer = MultiplayerManager(game)
        print("Do you want to (1) host or (2) join a game?")
        if input() == '1':
            multiplayer.host_game()
        else:
            multiplayer.join_game()
    game.start_game()