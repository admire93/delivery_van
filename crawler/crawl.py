# -*- coding: utf-8
from requests import get

import lxml.html


__all__ = 'crawl', 'html_select',


def crawl(url):
    r = get(url, headers={'User-Agent': u'Mozilla/5.0'
                                        u'(Windows NT 6.3; WOW64; rv:27.0) '
                                        u'Gecko/20100101 Firefox/27.0'})
    if r.status_code != 200 and 'text/html' not in r.headers['content-type']:
        return None
    return r.content


def html_select(doc, xpath='', special=None):
    if special is not None:
        if special == 'bugs':
            xpath = 'something'
    html = lxml.html.fromstring(doc)
    finds = html.xpath(xpath)
    return list(finds)
