import pytest

# Setup and teardown

# option 1
from pytest import raises


@pytest.fixture(autouse=True)
def setup_method1():
    print("Setting up test")


def test_try1(setup_method1):
    print("executing test")
    assert True


def test_try2():
    print("executing test")
    assert True


# option 2
@pytest.fixture
def setup_method2():
    print("Setting up ..")
    yield
    print("Teardown...")


def test_try3(setup_method2):
    assert True


# Exception
def test_exc():
    with raises(ValueError):
        raise ValueError
