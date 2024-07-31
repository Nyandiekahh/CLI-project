#!/usr/bin/env python3
import json
from player import Player  # Import the Player class
from game_state import GameState
from events import Events
from player_actions import PlayerActions
from game_updates import GameUpdates

class NairobiPoliceGame:
    def __init__(self):
        self.game_state = GameState()
        self.events = Events(self.game_state)
        self.player_actions = PlayerActions(self.game_state)
        self.game_updates = GameUpdates(self.game_state)
        self.load_high_score()
        self.locations = ["CBD", "Kibera", "Mathare", "Uhuru Park", "City Hall", "Nairobi Hospital"]
        self.current_day = 1
        self.max_days = 30

    def load_high_score(self):
        try:
            with open("high_score.json", "r") as f:
                self.game_state.high_score = json.load(f)["high_score"]
        except FileNotFoundError:
            self.game_state.high_score = 0

    def save_high_score(self):
        with open("high_score.json", "w") as f:
            json.dump({"high_score": max(self.game_state.high_score, self.game_state.score)}, f)

    def start_game(self):
        self.character_creation()
        self.main_game_loop()

    def character_creation(self):
        print("Welcome to the Nairobi Police and Citizens Protests Adventure!")
        print("Choose your character background:")
        print("1. Veteran Officer")
        print("2. Rookie Officer")
        print("3. Community Liaison")
        print("4. Tactical Expert")

        while True:
            choice = input("Enter your choice (1-4): ")
            if choice in ["1", "2", "3", "4"]:
                backgrounds = ["Veteran Officer", "Rookie Officer", "Community Liaison", "Tactical Expert"]
                self.game_state.player = Player(backgrounds[int(choice) - 1])
                print(f"\nYou have chosen: {self.game_state.player.background}")
                print("Strengths:", ", ".join(self.game_state.player.strengths))
                print("Weaknesses:", ", ".join(self.game_state.player.weaknesses))
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def main_game_loop(self):
        while self.current_day <= self.max_days:
            print(f"\n--- Day {self.current_day} of {self.max_days} ---")
            self.display_game_state()
            self.events.handle_location_event()
            self.events.handle_random_event()
            self.player_actions.handle_player_action()
            self.game_updates.update_game_state()
            if self.game_updates.check_game_over():
                break
            self.current_day += 1
        self.game_updates.end_game()

    def display_game_state(self):
        print(f"\nCurrent Location: {self.game_state.current_location}")
        print(f"Score: {self.game_state.score}")
        print("Resources:")
        for resource, value in self.game_state.resources.items():
            print(f"  {resource.capitalize()}: {value}")
