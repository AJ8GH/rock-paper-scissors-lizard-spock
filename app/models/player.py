class Player:
    def __init__(self, name = 'Human'):
        self.name = name
        self.choice = None

    def choose(self, choice):
        self.choice = choice

    def choice(self):
        return self.choice
