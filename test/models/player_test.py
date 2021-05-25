import pytest

from app.models import Player

def test_it_can_be_initialized_with_a_name():
    player = Player('test')
    assert(player.name == 'test')

def test_it_has_a_default_name():
    player = Player()
    assert(player.name == 'Human')

if __name__ == '__main__':
    pytest.main()
