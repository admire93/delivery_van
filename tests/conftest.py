# -*- coding: utf-8 -*-
from pytest import fixture

def pytest_addoption(parser):
    parser.addoption('--crawl',
                     action='store_true',
                     help='run tests that actually crawl bugs web page')


@fixture
def f_page():
    with open('./tests/assets/test.html', 'r') as f:
        return f.read()

