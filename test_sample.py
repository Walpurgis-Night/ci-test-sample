import pytest

def add(a, b):
    return a + b


def test_add():
    assert add(1, 2) == 3

def test_add_negative():
    assert add(-1, 1) == 0

def test_add_type_error():
    with pytest.raises(TypeError):
        add("a", 1)