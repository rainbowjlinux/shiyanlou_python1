#!/usr/bin/env python3

############################
#File Name: threadd.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-26 20:11:47
############################

import threading

def func(name):
    print('thread name:', name)
    print('child thread:', threading.get_ident())

if __name__ == '__main__':
    t = threading.Thread(target=func, args=('wang', ))
    t.start()
    t.join()
    print('main thread', threading.get_ident())
