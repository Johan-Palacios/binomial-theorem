from theorem import combination, binomial_theorem
from utils import add_plus
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


def test_add_plus():
    assert add_plus("----") == True
    assert add_plus("+++++") == False
    assert add_plus("-+-+") == True
    assert add_plus("adlkfja") == False


def test_theorem():
    test_combination()
    test_comination_n_zero()
    test_binomiarl_theorem()
    test_add_plus()


if __name__ == "__main__":
    test_theorem()
