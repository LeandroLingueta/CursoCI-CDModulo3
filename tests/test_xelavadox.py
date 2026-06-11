from src.xelavadox import format_result


def test_xelavadox_small_number():
    assert format_result(2) == "2 elevado a 2 é 4"


def test_xelavadox_three():
    assert format_result(3) == "3 elevado a 3 é 27"
