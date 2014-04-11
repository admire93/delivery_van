# -*- coding: utf-8 -*-

def pager(current, len_, lim):
    page_len = len_ / lim
    for i in xrange(1, page_len + 1):
        if i == 1:
            r = (i, 'f')
        elif i == current:
            r = (i, 'c')
        elif (current - 4) < i < (current + 4):
            r = (i, 'n')
        elif page_len == i:
            r = (i, 'e')
        else:
            continue
        yield r
