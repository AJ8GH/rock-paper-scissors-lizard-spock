import pytest

from app.models import Player

def test_it_can_be_initialized_with_a_name():
    player = Player('test')
    assert(player.name == 'test')

def test_it_has_a_default_name():
    player = Player()
    assert(player.name == 'Human')

def test_it_can_make_a_choice():
    player = Player()
    player.choose('Rock')
    assert(player.get_choice() == 'Rock')

if __name__ == '__main__':
    pytest.main()
