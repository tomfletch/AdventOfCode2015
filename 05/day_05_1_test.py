from day_05_1 import (
    contains_three_vowels,
    contains_duplicate_letter,
    contains_bad_strings,
    is_nice
)

def test_vowels():
    assert contains_three_vowels('ugknbfddgicrmopn')

def test_dupliate_letter():
    assert contains_duplicate_letter('ugknbfddgicrmopn')

def test_bad_strings():
    assert not contains_bad_strings('ugknbfddgicrmopn')

def test_1():
    assert is_nice('ugknbfddgicrmopn')

def test_2():
    assert is_nice('aaa')

def test_3():
    assert not is_nice('jchzalrnumimnmhp')

def test_4():
    assert not is_nice('haegwjzuvuyypxyu')

def test_5():
    assert not is_nice('dvszwmarrgswjxmb')
