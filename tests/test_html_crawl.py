# -*- coding: utf-8 -*-
from pytest import mark, config

from crawler.crawl import crawl, html_select
from crawler.bugs import BugsRecentAlbum

crawlskip = mark.skipif(not config.getvalue('crawl'),
                        reason="crawl is not available")

def test_crawl():
    r = crawl('http://example.com')
    assert r is not None
    assert '<title>Example Domain</title>' in r


def test_html_select():
    doc = crawl('http://example.com')
    assert doc
    assert '<title>Example Domain</title>' in doc
    r = html_select(doc, xpath='//title')
    assert r is not None


@crawlskip
def test_crawl_bugs():
    bugs = BugsRecentAlbum()
    assert bugs.newest


def test_asset_bugs(f_page):
    bugs = BugsRecentAlbum()
    bugs.doc[1] = f_page
    assert bugs.newest
    assert isinstance(bugs.newest, list)
    assert 'thumbnail' in bugs.newest[0]
    assert 'album_name' in bugs.newest[0]
    assert 'artist_name' in bugs.newest[0]
