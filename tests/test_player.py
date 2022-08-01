from src.Pytest_tutorial.player import *


def test_construction():
    g = Player('a', 'b')
    assert 'a' == g.first_name
    assert 'b' == g.last_name
