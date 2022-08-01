from src.Pytest_tutorial.player import Player


def test_construction():
    g = Player('a', 'b')
    assert 'a' == g.first_name
