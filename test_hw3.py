import pytest


@pytest.fixture
def login_page(browser):
    print("Page of login!")


@pytest.fixture
def user():
    print("User!")
    return "username", "password"



def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"