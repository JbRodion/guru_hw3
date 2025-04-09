import pytest


@pytest.fixture(scope="session")
def browser():
    print("Browser!")
    yield
    print("close browser")

