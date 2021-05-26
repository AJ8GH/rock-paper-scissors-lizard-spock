from . import Computer, Player

class Game():
    WIN_MATRIX = {
        'Rock': { 'Scissors': 'Win', 'Lizard': 'Win' },
        'Scissors': { 'Rock': 'Lose', 'Paper': 'Win' },
        'Paper': { 'Scissors': 'Lose' },
        'Lizard': { 'Rock': 'Lose' },
    }

    def __init__(self, player, computer = Computer()):
        self.computer = computer
        self.player = player

    def result(self):
        return self.WIN_MATRIX[self.player.choice()][self.computer.choice()]
