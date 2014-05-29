# -*- coding: utf-8 -*-
from math import ceil

from flask import request


def pager(current, len_, lim):
    page_len = int(ceil(len_ / float(lim)))
    for i in xrange(1, page_len + 1):
        if i == current:
            r = (i, 'c')
        elif i == 1:
            r = (i, 'f')
        elif page_len == i:
            r = (i, 'e')
        elif (current - 4) < i < (current + 4):
            r = (i, 'n')
        else:
            continue
        yield r

def bind_page(post_per_page=15):
    page = request.args.get('page', 1, type=int)
    o = (page - 1) * post_per_page
    return page, o, post_per_page
