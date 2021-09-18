from day_10_1 import look_and_say

def test_1():
    assert look_and_say('1') == '11'

def test_2():
    assert look_and_say('11') == '21'

def test_3():
    assert look_and_say('21') == '1211'

def test_4():
    assert look_and_say('1211') == '111221'

def test_5():
    assert look_and_say('111221') == '312211'
