# -*- coding: utf-8 -*-
from crawler.bugs import XPathGenerator

def test_generator():
    g = XPathGenerator()
    g.find('a')\
     .find('span', class_='foo')\
     .find('div', id='bar')
    assert g.route
    assert "//a//span[contains(@class, 'foo')]//div[@id='bar']" == g.route
