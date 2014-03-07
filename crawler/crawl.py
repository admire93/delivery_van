# -*- coding: utf-8
from requests import get

import lxml.html


__all__ = 'crawl', 'html_select',


def crawl(url):
    r = get(url)
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
