import pytest

from app.models.computer import Computer

def test_computer_can_make_a_choice():
    computer = Computer()
    computer.choose()
    assert computer.choice == 'spock'

if __name__ == '__main__':
    pytest.main()
