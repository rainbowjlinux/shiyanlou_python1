#!/usr/bin/env python3

############################
#File Name: enumerate.py
#Author: rainbowjlinux
#Mail: rainbowjlinux@gmail.com
#Created Time: 2017-10-23 15:18:40
############################

import sys

if __name__ == '__main__':
    for i, x in enumerate(sys.argv):
        if i == 0:
            print (x)
            continue
        print (i, x)
    l = [1,2,3,4]
    print (enumerate(l))
    for a, b in enumerate(l):
        print ('index:%s value:%s' % (a,b))
