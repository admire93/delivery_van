# -*- coding: utf-8 -*-
from .crawl import crawl, html_select, html_select_all


class XPathGenerator(object):
    """Help generate the xpath.
    """

    def __init__(self, base='//'):
        if isinstance(base, XPathGenerator):
            self.base = base.route + '//'
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
    def route_all(self):
        return self.base + '//'.join(self._route)

    @property
    def route(self):
        r = self.base + '//'.join(self._route)
        if r.startswith('//'):
            r = r[2:]
        return r


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
     * album name (`album > dl.albumInfo > dt > a.albumtitle`)
     * artist name (`album > dl.albumInfo > dd > a.artistname`)
    """

    url = u'http://music.bugs.co.kr/newest/album/total'

    def __init__(self):
        super(BugsRecentAlbum, self).__init__(self.url)

    def parse(self, doc):
        res = []
        base_g = XPathGenerator()
        base_g.find('div', class_='album')\
              .find('ul', id='idListNEWALBUM522')\
              .find('li', class_='listRow')
        g = XPathGenerator()
        g.find('div', class_='thumbnail', new=True)\
         .find('span', class_='albumImg')\
         .find('a')\
         .find('img')
        thumbnail_path = g.route
        album_g = XPathGenerator("dl[contains(@class, 'albumInfo')]//")
        album_g.find('dt')\
               .find('a', class_='albumtitle')
        albumtitle_path = album_g.route
        album_g.find('dd', new=True)\
               .find('a', class_='artistname')
        artistname_path = album_g.route
        li = html_select_all(doc, base_g.route_all)
        for elem in li:
            album = html_select(elem, albumtitle_path)
            artist_name = html_select(elem, artistname_path)
            item = {
                'thumbnail': html_select(elem, thumbnail_path).attrib['src'],
                'album_name': album.text_content(),
                'album_link': album.attrib['href'],
            }
            if artist_name is not None:
                item.update(
                    artist_name=artist_name.text_content(),
                    artist_link=artist_name.attrib['href'])
            else:
                item.update(
                    artist_name='Various Artists',
                    artist_link='http://bugs.co.kr')
            res.append(item)
        return res
