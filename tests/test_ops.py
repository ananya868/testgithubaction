from src.math_ops import add, subtract


def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(-1, 1) == 0
    assert add(-100, -200) == -300


def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(1, -1) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(-1, 1) == -2
    assert subtract(-100, -200) == 100


