#!/usr/bin/env python3

############################
#File Name: decrator.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-25 17:18:00
############################

from datetime import datetime

if __name__ == '__main__':

    def log(func):
        def decrator(*args, **kwargs):
            print(func.__name__,'has been called at',datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            return func(*args, **kwargs)
        return decrator
    @log
    def add(x, y):
        return x+y

    print(add(1,2))
