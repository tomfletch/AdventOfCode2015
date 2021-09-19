from day_11_1 import (
    increment_letter,
    increment_password,
    contains_increasing_letters,
    contains_iol,
    contains_two_pairs,
    get_next_valid_password
)

def test_increment_letter():
    assert increment_letter('a') == 'b'
    assert increment_letter('t') == 'u'
    assert increment_letter('z') == 'a'

def test_increment_password():
    assert increment_password('xx') == 'xy'
    assert increment_password('ya') == 'yb'

def test_contains_increasing_letters():
    assert contains_increasing_letters('abc')
    assert contains_increasing_letters('xyz')
    assert contains_increasing_letters('dbcde')

def test_not_contains_increasing_letters():
    assert not contains_increasing_letters('abd')
    assert not contains_increasing_letters('cba')

def test_contains_iol():
    assert contains_iol('i')
    assert contains_iol('aob')
    assert contains_iol('abcl')
    assert contains_iol('abiolc')

def test_not_contains_iol():
    assert not contains_iol('abc')
    assert not contains_iol('ghjkm')

def test_contains_two_pairs():
    assert contains_two_pairs('aabb')
    assert contains_two_pairs('xaaybb')
    assert contains_two_pairs('aaxaa')
    assert contains_two_pairs('aaaa')

def test_not_contains_two_pairs():
    assert not contains_two_pairs('a')
    assert not contains_two_pairs('aaa')
    assert not contains_two_pairs('xyxy')
    assert not contains_two_pairs('abxxba')

def test_next_valid_password():
    assert get_next_valid_password('abcdefgh') == 'abcdffaa'
    assert get_next_valid_password('ghijklmn') == 'ghjaabcc'
