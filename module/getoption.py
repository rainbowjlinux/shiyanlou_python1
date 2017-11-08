#!/usr/bin/env python3
#-*- coding:utf-8 -*-
############################
#File Name: getoption.py
#Created Time: 2017-11-06 19:11:17
#Author: rainbowjlinux
############################

from getopt import getopt
import sys

def main():
    argv = sys.argv[1:]
    parameters, _ = getopt(argv, 'c:d:o:')
    print(parameters)
    print(parameters[0])
    print(parameters[0][1])

    p = dict(parameters)
    print(p)
    print(p['-c'])

if __name__ == '__main__':
    main()
