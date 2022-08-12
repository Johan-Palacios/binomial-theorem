from theorem import combination, binomial_theorem
from utils import is_positive
import pytest


def test_combination():
    assert combination(10, 3) == 120
    assert combination(1, 1) == 1


def test_comination_n_zero():
    with pytest.raises(ValueError):
        combination(0, 3)


def test_binomiarl_theorem():
    assert binomial_theorem(16, 8, 2, -3) == 21616657920
    assert binomial_theorem(16, 13, 2, -3) == -7142567040


def test_is_positive():
    assert is_positive("----") == True
    assert is_positive("+++++") == False
    assert is_positive("-+-+") == True
    assert is_positive("adlkfja") == False


def test_theorem():
    test_combination()
    test_comination_n_zero()
    test_binomiarl_theorem()
    test_is_positive()


if __name__ == "__main__":
    test_theorem()
