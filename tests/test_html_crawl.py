# -*- coding: utf-8 -*-
from crawler.crawl import crawl, html_select

def test_crawl():
    r = crawl('http://example.com')
    assert r
    assert '<title>Example Domain</title>' in r


def test_html_select():
    doc = crawl('http://example.com')
    assert doc
    assert '<title>Example Domain</title>' in doc
    r = html_select(doc, xpath='//title')
    assert r
