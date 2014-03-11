# -*- coding: utf-8 -*-
from pytest import mark, config

from crawler.crawl import crawl, html_select
from crawler.bugs import BugsRecentAlbum

crawlskip = mark.skipif(not config.getvalue('crawl'),
                        reason="crawl is not available")

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


@crawlskip
def test_crawl_bugs():
    bugs = BugsRecentAlbum()
    assert bugs.newest
