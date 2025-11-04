from src.app import add

def test_add_positive():
    assert add(4,4)=6

def test_add_negative():
    assert add(-3, -2) == -5

