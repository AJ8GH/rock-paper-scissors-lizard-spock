import pytest, random

from app.models import Computer

def test_computer_can_make_a_choice():
    random.seed(0)
    computer = Computer()
    computer.choose()
    assert computer.get_choice() == 'Lizard'

if __name__ == '__main__':
    pytest.main()
