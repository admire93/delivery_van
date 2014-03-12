# -*- coding: utf-8 -*-
from dv.crawl import XPathGenerator

def test_generator():
    g = XPathGenerator()
    g.find('a')\
     .find('span', class_='foo')\
     .find('div', id='bar')
    assert g.route_all
    assert "//a//span[contains(@class, 'foo')]//div[@id='bar']" == g.route_all
    assert "a//span[contains(@class, 'foo')]//div[@id='bar']" == g.route


def test_real_bugs_path():
    base_g = XPathGenerator()
    base_g.find('div', class_='album')\
          .find('ul', id='idListNEWALBUM522')
    assert "//div[contains(@class, 'album')]//ul[@id='idListNEWALBUM522']" == base_g.route_all
    assert "div[contains(@class, 'album')]//ul[@id='idListNEWALBUM522']" == base_g.route
