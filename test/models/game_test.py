import doubles
import pytest
from doubles import InstanceDouble, allow

from app.models import Game

player = InstanceDouble('app.models.Player', name='test')
computer = InstanceDouble('app.models.Computer')

def test_it_can_be_initialize_with_a_player():
    game = Game(player, computer)

    assert game.player.name == 'test'
    doubles.verify()

    doubles.teardown()

def test_it_has_a_computer():
    game = Game(player, computer)

    assert game.computer
    doubles.verify()

    doubles.teardown()

def test_it_knows_rock_crushes_scissors():
    game = Game(player, computer)

    allow(player).choice.and_return('Rock')
    allow(computer).choice.and_return('Scissors')
    assert game.result() == 'Win'

    allow(player).choice.and_return('Scissors')
    allow(computer).choice.and_return('Rock')
    assert game.result() == 'Lose'

    doubles.verify()

    doubles.teardown()

def test_it_knows_scissors_cuts_paper():
    game = Game(player, computer)

    allow(player).choice.and_return('Scissors')
    allow(computer).choice.and_return('Paper')
    assert game.result() == 'Win'

    allow(player).choice.and_return('Paper')
    allow(computer).choice.and_return('Scissors')
    assert game.result() == 'Lose'

    doubles.verify()

    doubles.teardown()

def test_it_knows_rock_crushes_lizard():
    game = Game(player, computer)

    allow(player).choice.and_return('Rock')
    allow(computer).choice.and_return('Lizard')
    assert game.result() == 'Win'

    allow(player).choice.and_return('Lizard')
    allow(computer).choice.and_return('Rock')
    assert game.result() == 'Lose'

    doubles.verify()

    doubles.teardown()

def test_it_knows_lizard_poisons_spock():
    game = Game(player, computer)

    allow(player).choice.and_return('Lizard')
    allow(computer).choice.and_return('Spock')
    assert game.result() == 'Win'

    allow(player).choice.and_return('Spock')
    allow(computer).choice.and_return('Lizard')
    assert game.result() == 'Lose'

    doubles.verify()

    doubles.teardown()

def test_it_knows_spock_smashes_scissors():
    game = Game(player, computer)

    allow(player).choice.and_return('Spock')
    allow(computer).choice.and_return('Scissors')
    assert game.result() == 'Win'

    allow(player).choice.and_return('Scissors')
    allow(computer).choice.and_return('Spock')
    assert game.result() == 'Lose'

    doubles.verify()

    doubles.teardown()

def test_it_knows_scissors_decapitates_lizard():
    game = Game(player, computer)

    allow(player).choice.and_return('Scissors')
    allow(computer).choice.and_return('Lizard')
    assert game.result() == 'Win'

    allow(player).choice.and_return('Lizard')
    allow(computer).choice.and_return('Scissors')
    assert game.result() == 'Lose'

    doubles.verify()

    doubles.teardown()

def test_it_knows_lizard_eats_paper():
    game = Game(player, computer)

    allow(player).choice.and_return('Lizard')
    allow(computer).choice.and_return('Paper')
    assert game.result() == 'Win'

    allow(player).choice.and_return('Paper')
    allow(computer).choice.and_return('Lizard')
    assert game.result() == 'Lose'

    doubles.verify()

    doubles.teardown()

def test_it_knows_paper_disproves_spock():
    game = Game(player, computer)

    allow(player).choice.and_return('Paper')
    allow(computer).choice.and_return('Spock')
    assert game.result() == 'Win'

    allow(player).choice.and_return('Spock')
    allow(computer).choice.and_return('Paper')
    assert game.result() == 'Lose'

    doubles.verify()

    doubles.teardown()
