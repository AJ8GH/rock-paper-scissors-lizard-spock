import pytest, random

from app.models.computer import Computer

def test_computer_can_make_a_choice():
    random.seed(0)
    computer = Computer()
    computer.choose()
    assert computer.choice == 'Lizard'

if __name__ == '__main__':
    pytest.main()
