class Player:
    def _init_(self, background):
        self.background = background
        self.strengths = []
        self.weaknesses = []
        self.set_traits()
    def set_traits(self):
        if self.background == "Veteran Officer":
            self.strengths = ["Leadership", "Experience"]   
            self.weaknesses = ["Rigid Thinking", "Health Issues"]
        elif self.background == "Rookie Officer":
            self.strengths = ["Energy", "Adaptability"]
            self.weaknesses = ["Inexperience", "Impulsiveness"] 
        elif self.background == "Community Liaison":
            self.strengths = ["Communication", "Empathy"]
            self.weaknesses = ["Lack of Authority", "Overly Trusting"]
        elif self.background == "Tactical Expert":
            self.strengths = ["Strategic Planning", "Physical Fitness"]
            self.weaknesses = ["Overconfidence", "Narrow Focus"]

