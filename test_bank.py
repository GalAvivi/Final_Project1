from main import *
import pytest



def test_Deposit():
    login(url1,driver1)
    actual = deposit1(250,driver1)
    expected = 5346
    assert actual == expected


def test_withrawing_depositing():
    login(url1,driver1)
    actual = deposit_plus_withraw(1000, 250, driver1)
    expected = 6096
    assert actual == expected


def test_text_Illegal_N():
    login(url1, driver1)
    actual = not_text('shalom', driver1)
    expected = ''
    assert actual == expected


def test_Has_an_account_been_created():
    opensite(url1, driver1)
    add_customer(driver1, 'dani', 'din', 123123)
    time.sleep(1)
    actual = if_customer_exist('dani','din',123123 , driver1)
    expected = True
    assert actual == expected

