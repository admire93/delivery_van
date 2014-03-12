# -*- coding: utf-8 -*-
from threading import Timer


def do(f, time, *args):
    f(*args)
    Timer(time, lambda: do(f, time, *args)).start()
