from . import Computer

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
        if self.player.get_choice() == self.computer.get_choice():
            return 'Draw'

        player_matrix = self.WIN_MATRIX[self.player.get_choice()]
        return player_matrix[self.computer.get_choice()]
