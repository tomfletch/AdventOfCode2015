from day_12_1 import sum_numbers

def test_sum_empty():
    assert sum_numbers([]) == 0
    assert sum_numbers({}) == 0

def test_sum_array():
    assert sum_numbers([1,2,3]) == 6

def test_nested_array():
    assert sum_numbers([[[3]]]) == 3
    assert sum_numbers([[2,1],[3,4]]) == 10

def test_object_values():
    assert sum_numbers({"a":2,"b":4}) == 6

def test_mixed():
    assert sum_numbers({"a":[-1,1]}) == 0
    assert sum_numbers([-1,{"a":1}]) == 0
