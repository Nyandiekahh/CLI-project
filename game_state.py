class GameState:
    def _init_(self):
        self.resources = {
            "public_support": 50,
            "equipment": 50,
            "personnel": 50
        }
        self.current_location = "CBD"
        self.score = 0
        self.player = None

    def update_location(self, new_location):
        self.current_location = new_location

