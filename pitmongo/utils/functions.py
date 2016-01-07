# -*- coding: utf-8 -*-
'''
Created on Jan 6, 2016

@author: rtorres
'''
import string, random


def generateKey(length=12):
    ret = []
    for i in range(0, length):
        if i % 3 == 0:
            ret.extend(random.sample(string.hexdigits, 1))
        else:
            ret.extend(random.sample(string.letters, 1))
    return ''.join(ret)
