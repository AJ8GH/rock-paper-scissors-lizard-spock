import random

class Computer:
    CHOICES = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    def __init__(self):
        self.choice = None

    def choose(self):
        self.choice = random.choice(self.CHOICES)

    def choice(self):
        return self.choice
