from day_05_2 import (
    contains_duplicate_pair,
    contains_duplicate_letter,
    is_nice
)

def test_duplicate_pair():
    assert contains_duplicate_pair('qjhvhtzxzqqjkmpb')
    assert contains_duplicate_pair('xxyxx')
    assert contains_duplicate_pair('uurcxstgmygtbstg')

def test_not_duplicate_pair():
    assert not contains_duplicate_pair('ieodomkazucvgmuy')

def test_duplicate_letter():
    assert contains_duplicate_letter('qjhvhtzxzqqjkmpb')
    assert contains_duplicate_letter('xxyxx')
    assert contains_duplicate_letter('ieodomkazucvgmuy')

def test_not_duplicate_letter():
    assert not contains_duplicate_letter('uurcxstgmygtbstg')

def test_is_nice():
    assert is_nice('qjhvhtzxzqqjkmpb')
    assert is_nice('xxyxx')

def test_is_naughty():
    assert not is_nice('uurcxstgmygtbstg')
    assert not is_nice('ieodomkazucvgmuy')
