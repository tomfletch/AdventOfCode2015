from day_08_2 import encode_string

def test_encode_empty_string():
    assert encode_string(R'""') == R'"\"\""'

def test_encode_string():
    assert encode_string(R'"abc"') == R'"\"abc\""'

def test_encode_string_with_quote():
    assert encode_string(R'"aaa\"aaa"') == R'"\"aaa\\\"aaa\""'

def test_encode_hex():
    assert encode_string(R'"\x27"') == R'"\"\\x27\""'