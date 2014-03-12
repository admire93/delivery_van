# -*- coding: utf-8
from requests import get
from lxml.html import HtmlElement

import lxml.html


__all__ = 'crawl', 'html_select', 'html_select_all', 'XPathGenerator',


def crawl(url):
    r = get(url, headers={'User-Agent': u'Mozilla/5.0'
                                        u'(Windows NT 6.3; WOW64; rv:27.0) '
                                        u'Gecko/20100101 Firefox/27.0'})
    if r.status_code != 200 or 'text/html' not in r.headers['content-type']:
        return None
    return r.content


def html_select_all(doc, xpath=''):
    if isinstance(doc, basestring):
        html = lxml.html.fromstring(doc)
    elif isinstance(doc, HtmlElement):
        html = doc
    finds = html.xpath(xpath)
    return list(finds)


def html_select(doc, xpath=''):
    r = html_select_all(doc, xpath)
    return None if not r else r[0]


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
