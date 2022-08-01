from src.Pytest_tutorial.guardian import Guardian


def test_construction():
    g = Guardian('a', 'b')
    assert 'a' == g.first_name
