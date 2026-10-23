from playground.src.playground.add import add


def test_basic():
    assert add(1, 1) == 2

def test_basic_2():
    assert add(1, 1) == 2
    print("This is a test")


def test_basic_fail():
    assert add(1, 1) == 3
    print("This test is expected to fail")

def test_basic_fail_2():
    assert add(1, 1) == 4
    print("This test is also expected to fail")