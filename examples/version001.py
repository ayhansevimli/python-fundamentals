# -*- coding: utf-8 -*-
import sys

_2x_metni = u"""
Python'in 2.x surumlerinden birini kullaniyorsunuz.
Programi calistirabilmek icin sisteminizde Python'in
3.x surumlerinden biri kurulu olmali!!!"""

_3x_metni = "Programa hoşgeldiniz."


if sys.version_info.major < 3 :
    print(_2x_metni)
else:
    print(_3x_metni)
