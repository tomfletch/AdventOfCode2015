from day_08_1 import count_string_length

def test_empty_string_length():
    assert count_string_length(R'""') == 0

def test_string_without_escapes_length():
    assert count_string_length(R'"abc"') == 3

def test_double_backslash_escape_length():
    assert count_string_length(R'"\\"') == 1

def test_quote_escape_length():
    assert count_string_length(R'"\""') == 1

def test_hex_escape_length():
    assert count_string_length(R'"\x27"') == 1
