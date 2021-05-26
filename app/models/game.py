from . import Computer, Player

class Game():
    WIN_MATRIX = {
        'Rock': { 'Scissors': 'Win', 'Lizard': 'Win' },
        'Scissors': { 'Rock': 'Lose', 'Paper': 'Win', 'Spock': 'Lose' },
        'Paper': { 'Scissors': 'Lose' },
        'Lizard': { 'Rock': 'Lose', 'Spock': 'Win' },
        'Spock': { 'Lizard': 'Lose', 'Scissors': 'Win' },
    }

    def __init__(self, player, computer = Computer()):
        self.computer = computer
        self.player = player

    def result(self):
        return self.WIN_MATRIX[self.player.choice()][self.computer.choice()]
