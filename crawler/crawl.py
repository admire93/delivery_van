# -*- coding: utf-8
from requests import get
from lxml.html import HtmlElement

import lxml.html


__all__ = 'crawl', 'html_select', 'html_select_all',


def crawl(url):
    r = get(url, headers={'User-Agent': u'Mozilla/5.0'
                                        u'(Windows NT 6.3; WOW64; rv:27.0) '
                                        u'Gecko/20100101 Firefox/27.0'})
    if r.status_code != 200 and 'text/html' not in r.headers['content-type']:
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
