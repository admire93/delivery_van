# -*- coding: utf-8
from .crawl import crawl, html_select

class RecentAlbum(object):

    def __init__(self, url):
        self._page = (url + '?page={0}').format
        self.doc = {}

    def _load_doc(self, page, force=False):
        if force or not self.doc or page not in self.doc:
            a = crawl(self._page(page))
            self.doc[page] = a
        return self.doc[page]

    @property
    def newest(self):
        return self.parse(self._load_doc(1))

    def page(self, n):
        return self.parse(self._load_doc(n))

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
        return doc
