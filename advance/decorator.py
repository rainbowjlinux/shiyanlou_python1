#!/usr/bin/env python3

############################
#File Name: decrator.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-25 17:18:00
############################

from datetime import datetime

BIRTH_TABLE = {
        'xiaoshumiao' : 2014,
        'xiaopingguo' : 2015
        }

class Baby(object):
    '''
    def __init__(self, year):
        self._birth = year
    '''
    def _baby_birth(self, name):
        return BIRTH_TABLE[name]

    @property
    def xiaoshumiao_birth(self):
        return self._baby_birth('xiaoshumiao')

    @property
    def xiaopingguo_birth(self):
        return self._baby_birth('xiaopingguo')

    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

def log(func):
    def decrator(*args, **kwargs):
        print(func.__name__,'has been called at',datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return func(*args, **kwargs)
    return decrator

def main():
    @log
    def add(x, y):
        return x+y

    add(1,2)

    bb = Baby()
    print(bb.xiaoshumiao_birth)
    print(bb.xiaopingguo_birth)

    bb.birth=1987
    print(bb.age)

if __name__ == '__main__':
    main()
