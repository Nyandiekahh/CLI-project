#!/usr/bin/env python3
class GameState:
    def __init__(self):
        self.resources = {
            "public_support": 50,
            "equipment": 50,
            "personnel": 50,
            "morale": 50
        }
        self.current_location = "CBD"
        self.score = 0
        self.player = None
        self.high_score = 0

    def update_location(self, new_location):
        self.current_location = new_location
