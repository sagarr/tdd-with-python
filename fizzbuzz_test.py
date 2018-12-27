def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    if n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'
    return n


def test_print_number():
    result = fizzbuzz(1)
    assert result == 1


def test_print_another_number():
    res = fizzbuzz(2)
    assert res == 2

    res = fizzbuzz(29)
    assert res == 29


def test_print_fizz():
    res = fizzbuzz(3)
    assert res == 'fizz'

    res = fizzbuzz(9)
    assert res == 'fizz'

    res = fizzbuzz(24)
    assert res == 'fizz'


def test_print_buzz():
    res = fizzbuzz(5)
    assert res == 'buzz'

    res = fizzbuzz(10)
    assert res == 'buzz'


def test_print_fizzbuzz():
    res = fizzbuzz(15)
    assert res == 'fizzbuzz'

    res = fizzbuzz(30)
    assert res == 'fizzbuzz'
