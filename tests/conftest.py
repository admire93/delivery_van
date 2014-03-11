# -*- coding: utf-8 -*-

def pytest_addoption(parser):
    parser.addoption('--crawl',
                     action='store_true',
                     help='run tests that actually crawl bugs web page')
