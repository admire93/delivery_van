# -*- coding: utf-8 -*-
from dv.web.util import pager


def norm_list(p):
    return map(lambda x: x[0], p)

def test_small_pager():
    assert [1, 2, 3] == norm_list(pager(1, 15, 5))


def test_small2_pager():
    assert [1, 2, 3, 4, 5] == norm_list(pager(1, 25, 5))


def test_mid_pager():
    assert [1, 9, 10, 11, 12, 13, 14, 15, 30] == norm_list(pager(12, 150, 5))


def test_end_pager():
    assert [1, 26, 27, 28, 29, 30] == norm_list(pager(29, 150, 5))


def test_end2_pager():
    assert [1, 27, 28, 29, 30] == norm_list(pager(30, 150, 5))
