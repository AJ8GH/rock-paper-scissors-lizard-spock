import pytest

from app.models import Game

def test_it_has_a_computer():
    game = Game()
    assert game.computer
