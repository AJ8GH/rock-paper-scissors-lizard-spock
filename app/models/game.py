from . import Computer, Player

class Game():
    def __init__(self, player, computer = Computer()):
        self.computer = computer
        self.player = player

    def result(self):
        return 'Player'
