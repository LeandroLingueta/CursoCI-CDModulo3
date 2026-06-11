from src.parimpar import format_result


def test_parimpar_even_number():
    assert format_result(10) == "O numero é par."


def test_parimpar_odd_number():
    assert format_result(7) == "O numero é impar."
