# -*- coding: utf-8 -*-
from .crawl import crawl, html_select


class XPathGenerator(object):
    """Help generate the xpath.
    """

    def __init__(self, base='//'):
        if isinstance(base, XPathGenerator):
            self.base = base.route
        elif isinstance(base, basestring):
            self.base = base
        self._route = []

    def find(self, elem, class_=None, id=None, new=False):
        if new:
            self._route = []
        path = ''
        if id is not None:
            path = elem + "[@id='%s']" % id
        elif class_ is not None:
            path = elem + "[contains(@class, '%s')]" % class_
        else:
            path = elem
        self._route.append(path)
        return self

    @property
    def route(self):
        return self.base + '//'.join(self._route)


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
