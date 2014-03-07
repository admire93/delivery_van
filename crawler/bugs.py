# -*- coding: utf-8
from .crawl import crawl, html_select

class RecentAlbum(object):

    def __init__(self, url):
        self._page = (url + '?page={0}').format

    @property
    def newest(self):
        doc = crawl(self._page(1))
        return parse(doc)

    def page(self, n):
        doc = crawl(self._page(n))
        return parse(crawl)

    def parse(self, doc):
        raise NotImplemented()


class BugsRecentAlbum(RecentAlbum):
    """In bugs web page, some of usuable css selector is

     * new album list (`div.album > ul#idListNEWALBUM522 > li.listRow`)
     * thumbnail location (`album > div.thumbnail > span.albumImg > a > img`)
     * artist name (`album > dl.albumInfo > dt > a.artistname`)
     * track title (`album > dl.albumInfo > dd > a.tracktitle`)
    """

    url = u'http://music.bugs.co.kr/newest/album/total'

    def __init__(self):
        super(BugsRecentAlbum, self).__init__(self.url)

    def parse(self, doc):
        return {'album_name': 'abc',
                'album_art_url': 'http://aa.com',
                'artists': []}
