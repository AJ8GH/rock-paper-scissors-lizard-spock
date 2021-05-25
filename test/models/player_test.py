import pytest

from app.models import Player

def test_it_has_a_name():
    player = Player('test')
    assert(player.name == 'test')

if __name__ == '__main__':
    pytest.main()
