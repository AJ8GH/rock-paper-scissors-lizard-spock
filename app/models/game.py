from . import Computer, Player

class Game():
    WIN_MATRIX = {
        'Rock': {
            'Scissors': 'Win', 'Lizard': 'Win', 'Spock': 'Lose', 'Paper': 'Lose'
        },
        'Scissors': {
            'Rock': 'Lose', 'Paper': 'Win', 'Spock': 'Lose', 'Lizard': 'Win'
        },
        'Paper': {
            'Scissors': 'Lose', 'Lizard': 'Lose', 'Spock': 'Win', 'Rock': 'Win'
        },
        'Lizard': {
            'Rock': 'Lose', 'Spock': 'Win', 'Scissors': 'Lose', 'Paper': 'Win'
        },
        'Spock': {
            'Lizard': 'Lose', 'Scissors': 'Win', 'Paper': 'Lose', 'Rock': 'Win'
        },
    }

    def __init__(self, player, computer = Computer()):
        self.computer = computer
        self.player = player

    def result(self):
        if self.player.choice() == self.computer.choice():
            return 'Draw'
        return self.WIN_MATRIX[self.player.choice()][self.computer.choice()]
