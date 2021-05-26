import doubles
import pytest
from doubles import InstanceDouble, allow

from app.models import Game

def test_it_can_be_initialize_with_a_player():
    player = InstanceDouble('app.models.Player', name='test')
    computer = InstanceDouble('app.models.Computer')
    game = Game(player, computer)

    assert game.player.name == 'test'
    doubles.verify()

    doubles.teardown()

def test_it_has_a_computer():
    player = InstanceDouble('app.models.Player', name='test')
    computer = InstanceDouble('app.models.Computer')
    game = Game(player, computer)

    assert game.computer
    doubles.verify()

    doubles.teardown()

def test_it_knows_who_wins():
    player = InstanceDouble('app.models.Player', name='test')
    computer = InstanceDouble('app.models.Computer')
    game = Game(player, computer)

    allow(player).choice.and_return('Rock')
    allow(computer).choice.and_return('Scissors')

    assert game.result() == 'Player'
    doubles.verify()

    doubles.teardown()
