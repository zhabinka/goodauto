from goodauto.wsgi import *
from sheduler.parser import pull_numbers
from bs4 import BeautifulSoup


def test_pull_numbers():
    assert pull_numbers(BeautifulSoup('12', 'lxml')) == 12
    assert pull_numbers(BeautifulSoup('1 300 seats', 'lxml')) == 1300
    assert pull_numbers(BeautifulSoup('0', 'lxml')) == 0
    assert pull_numbers(BeautifulSoup('-', 'lxml')) is None
    assert pull_numbers(BeautifulSoup('', 'lxml')) is None
    assert pull_numbers(BeautifulSoup(' ', 'lxml')) is None
