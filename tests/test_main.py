import pytest
from main import *


def test_is_palindrome():
    assert is_palindrome("kajak") is True
    assert is_palindrome("Kobyła ma mały bok") is True
    assert is_palindrome("python") is False
    assert is_palindrome("") is True


def test_fibonacci():
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_count_vowels():
    assert count_vowels("Python") == 2
    assert count_vowels("Próba żółwia") == 7


def test_calculate_discount():
    assert calculate_discount(100, 0.2) == 80.0
    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)


def test_flatten_list():
    assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]


def test_word_frequencies():
    assert word_frequencies("To be or not to be") == {
        "to": 2,
        "be": 2,
        "or": 1,
        "not": 1,
    }


def test_is_prime():
    assert is_prime(97) is True
    assert is_prime(4) is False
