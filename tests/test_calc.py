import pytest
from src.calc import add, subtract, multiply, divide

# example for standalone test case with parametrize
@pytest.mark.parametrize("a,b,expected",
                         [(10, 5, 15),
                          (-1, 1, 0),
                          (-1, -1, -2)])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected",
                         [(10, 5, 15),
                          (-1, 1, 0),
                          (-1, -1, -2)])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected",
                         [(10, 5, 5),
                          (-1, 1, -2),
                          (-1, -1, 0)])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a,b,expected",
                         [(10, 5, 50),
                          (-1, 1, -1),
                          (-1, -1, 1)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a,b,expected",
                         [(10, 5, 2),
                          (-1, 1, -1),
                          (-1, -1, 1),
                          (-5, 2, -2.5)])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_subtract_exception():
    with pytest.raises(ValueError, match='Can not divide by zero!'):
        divide(10, 0)
